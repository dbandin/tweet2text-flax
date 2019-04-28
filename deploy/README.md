Tha application is uploaded to docker, so, the only necessary thing for the deployment is to have the "tweet2text.yaml" file present in this repository.

From the control instance the application can be launched within the kubernetes cluster with the following command.
```
kubectl apply -f tweet2text.yaml
```
