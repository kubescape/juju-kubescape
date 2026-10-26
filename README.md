# Kubescape Juju charm — deprecated

This Juju charm is deprecated and is being retired. Do not use it for new
deployments. This retirement applies only to the Juju charm, not to the
Kubescape project or its Operator.

Deprecation was announced on **26 October 2026**. The migration window ends on
**25 November 2026**, after which this repository is planned to be archived.
New deployments should use the maintained installation method below.

Use the maintained [Kubescape Operator installation instructions](https://kubescape.io/docs/install-operator/)
to deploy with Helm or Argo CD. For on-demand scans, see the
[Kubescape CLI installation instructions](https://kubescape.io/docs/install-cli/).

## Existing deployments

The published charm contains old dependencies and Kubescape components.
Dependency security advisories remain unresolved. Deprecation, closing Charmhub
channels, and archiving this repository do not patch or remove existing
installations.

Plan a migration to the maintained installation method. Record your existing
configuration and cloud connection settings, inventory the cluster resources
created by the charm, and test the replacement before removing the old
deployment. The Helm installation instructions describe a new installation;
they are not an automated migration from this charm.

If you currently use this charm, report your migration needs through the
[repository issue tracker](https://github.com/kubescape/juju-kubescape/issues)
before the repository is archived. Do not include credentials or other secrets.

