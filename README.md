# Kubescape Operator

The Kubescape charm deploys the Kubescape in-cluster components on Kubernetes to enhance the security of a running cluster.

## Usage

Before you deploy Kubescape, please:

- Make sure you have access to a Charmed Kubernetes cluster you want to secure.

- Sign up for an account at ARMO Cloud for Kubescape (https://armosec.io/).
Kubescape will use it to give you insight into your cluster’s security.

- Copy your account ID.

After that, you may deploy the Kubescape charm via Juju by running the following command:

```
juju add-model kubescape
juju deploy --trust kubescape --config clusterName=`kubectl config current-context` --config account=<YOUR_CLOUD_ACCOUNT_ID>
```

