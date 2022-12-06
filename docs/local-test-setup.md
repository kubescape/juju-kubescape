# Local Demo Setup for the Kubescape Charm

To play around with the Kubescape Charm, you would need:

- A running Kubernetes cluster. Minikube, MicroK8s or anything else will do for local.
- A working Juju OLM installation.
A simple Snap install will do, as demonstrated later.
However, if you want more details, you can find the installation instructions [here](https://juju.is/docs/olm/get-started-with-juju#heading--install-the-juju-cli-client).

Start out by installing the Juju OLM:
```
sudo snap install juju --classic
```

When you have the Juju OLM installed, you have to configure an appropriate Juju controller for your cloud.
In our case, the “cloud” is a local Minikube cluster, so make sure your cluster is running:

```
minikube start
```

Then set up a controller for your Minikube cluster by running the following command:

```
juju bootstrap minikube
```

Now your Juju CLI should be ready to work with your running cluster.
So to deploy the Kubescape Charm, it’s time to create a model and deploy the Charm by following the steps in the [README](../README.md).
