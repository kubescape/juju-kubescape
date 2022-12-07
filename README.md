# Kubescape Operator

The Kubescape charm deploys the Kubescape in-cluster components on Kubernetes to enhance the security of a running cluster.

## Usage

Before you deploy Kubescape, please:

- Make sure you have access to a Kubernetes cluster you want to secure.

- Sign up for an account at ARMO Cloud for Kubescape (https://armosec.io/). Kubescape will use it to give you an insight into your cluster’s security.

- Copy your account ID.

After that, you may deploy the Kubescape charm via Juju by running the following command:

```
juju add-model kubescape
juju deploy --trust kubescape --config clusterName=`kubectl config current-context` --config account=<YOUR_CLOUD_ACCOUNT_ID>
```

## Documentation

More documentation on using Kubescape is available at our [Kubescape User Hub](https://hub.armosec.io/docs) and in our [Kubescape Cloud Operator](https://github.com/kubescape/helm-charts/blob/master/charts/kubescape-cloud-operator/README.md) repository.
