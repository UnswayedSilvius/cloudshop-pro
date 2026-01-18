#!/bin/bash
set -e

kubectl delete -f k8s/
kubectl delete -f monitoring/prometheus.yaml