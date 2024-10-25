#!/bin/bash

sudo -u aswinvilasp bash <<EOF
kubectl apply -f deployment-django.yml
kubectl apply -f service-django.yml
kubectl apply -f deployment-flask.yml
kubectl apply -f service-flask.yml
kubectl apply -f deployment-nginx.yml
kubectl apply -f service-nginx.yml
kubectl apply -f ingress.yml
EOF
