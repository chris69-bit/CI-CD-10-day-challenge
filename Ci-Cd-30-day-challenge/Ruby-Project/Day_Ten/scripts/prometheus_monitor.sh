#!/bin/bash

echo "Deploying Prometheus..."
kubectl apply -f kubernetes/prometheus/prometheus-deployment.yaml
kubectl apply -f kubernetes/prometheus/prometheus-service.yaml

echo "Deploying Grafana..."
kubectl apply -f kubernetes/grafana/grafana-deployment.yaml
kubectl apply -f kubernetes/grafana/grafana-service.yaml

echo "Deploying Alertmanager..."
kubectl apply -f kubernetes/alertmanager/alertmanager-deployment.yaml
kubectl apply -f kubernetes/alertmanager/alertmanager-service.yaml
