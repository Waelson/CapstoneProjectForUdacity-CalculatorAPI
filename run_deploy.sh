#!/bin/bash
krane deploy $1 $(kubectl config current-context) -f ./descriptors-k8s
kubectl get services -o wide --namespace $1
kubectl -n $1 set image deployments/flask-backend-deployment flask-app=thedevices/calculator-api:$2
