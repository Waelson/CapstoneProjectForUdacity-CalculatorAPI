#!/bin/bash
krane deploy $1 $(kubectl config current-context) -f ./descriptors-k8s
kubectl get services -o wide --namespace $1
