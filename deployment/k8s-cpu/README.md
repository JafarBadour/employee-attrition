# Structure

```
.
├── deployment.yaml
├── grafana.yaml
└── svc_elb.yaml
```

- ├── deployment.yaml

Contains the eks configs for mlflow replicas

- ├── grafana.yaml

Contains the eks configs for the signle replica (can be increased) grafana dashboarding app


- └── svc_elb.yaml

Information about load balancers for each of the deployments