#!/usr/bin/env python3
# Copyright 2022 v.klokun
# See LICENSE file for licensing details.
#
# Learn more at: https://juju.is/docs/sdk

"""Charm the service.

Deploys the Kubescape Cloud Operator in a Juju model.
"""

import logging
import uuid

from ops.charm import CharmBase
from ops.main import main
from ops.model import BlockedStatus

import lightkube as lk
from lightkube import codecs
from lightkube.core.exceptions import ApiError

import pydantic as pyd

# Log messages can be retrieved using juju debug-log
logger = logging.getLogger(__name__)

# A path to the Kubescape resources template file
_KUBESCAPE_RESOURCES_TEMPLATE_PATH = "./src/kubescape.yaml"


class StrUUID(str):
    """A string that is a valid UUID."""

    @classmethod
    def __get_validators__(cls):
        """Return validators for the type."""
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not isinstance(v, str):
            return TypeError("string required")

        # Raises a ValidationError if `v` is not a valid UUID
        uuid.UUID(v)

        return cls(v)


class TemplateValues(pyd.BaseModel):
    """Values used to render the Kubescape resources templates."""

    clusterName: str
    account: StrUUID
    namespace: str

    class Config:
        extra = pyd.Extra.forbid


class KubescapeCharmedCharm(CharmBase):
    """Charm the service."""

    def __init__(self, *args):
        super().__init__(*args)

        self.framework.observe(self.on.install, self._handle_install_event)

    @property
    def _namespace(self) -> str:
        """Return the current Kubernetes namespace."""
        with open("/var/run/secrets/kubernetes.io/serviceaccount/namespace", "r") as f:
            return f.read().strip()

    def _handle_install_event(self, _):
        """Handles the Charm installation event.

        Renders the Kubescape templates and creates them in the current
        namespace of the K8s cluster.
        """
        try:
            tv = TemplateValues(**self.model.config, namespace=self._namespace)
        except pyd.ValidationError as exc:
            self.unit.status = BlockedStatus(
                    f"Invalid config. Please fix it and try again.\nDetails: {exc}"
            )
            return

        k8s_client = lk.Client()

        with open(_KUBESCAPE_RESOURCES_TEMPLATE_PATH) as f:
            for resource in codecs.load_all_yaml(f, context=tv.dict()):
                try:
                    k8s_client.create(resource)
                except ApiError as e:
                    if e.status.code == 409:
                        logger.info("replacing resource: %s.", str(resource.to_dict()))
                        k8s_client.replace(resource)
                    else:
                        logger.debug("failed to create resource: %s.", str(resource.to_dict()))
                        raise


if __name__ == "__main__":  # pragma: nocover
    main(KubescapeCharmedCharm)
