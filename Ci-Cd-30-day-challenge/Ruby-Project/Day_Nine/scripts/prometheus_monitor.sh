#!/bin/bash

echo "Deploying Prometheus..."
kubectl apply -f k8s/prometheus/prometheus-deployment.yaml
kubectl apply -f k8s/prometheus/prometheus-service.yaml

echo "Deploying Grafana..."
kubectl apply -f k8s/grafana/grafana-deployment.yaml
kubectl apply -f k8s/grafana/grafana-service.yaml

echo "Deploying Alertmanager..."
kubectl apply -f k8s/alertmanager/alertmanager-deployment.yaml
kubectl apply -f k8s/alertmanager/alertmanager-service.yaml
