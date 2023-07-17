# Hosting

After packaging the model we can easily deploy on an EKS cluster and have it send info to an RDS. This will be visualized by a dashboard that also is hosted on the cluster `grafana`.

# Installation

with conda 
```bash
conda create -p ./venv python==3.7
conda activate ./venv
```
then

```
pip install -r requirements/cpu-requirements.txt
```

```
curl https://pyenv.run | bash
python -m  pip install virtualenv
PATH="$HOME/.pyenv/bin:$PATH"


``` 

```
sudo apt  install awscli
mlflow models serve -m MODEL_PATH -h 0.0.0.0 -p 3008
```

After installing terraform/aws/kubectl as denoted in `deployment/terraform/cluster/README.md`
# installing infrastructure
```bash
cd deployment/terraform/cluster
terraform init
terraform apply

```

After the infra steps are finished we can push the required ECR images to the ecr repo just created
# installing software

```
cd deployment/mlflow/
bash deployment/mlflow/build-and-push.sh

docker tag grafana/grafana-enterprise ECR-ACCNT.dkr.ecr.REGION.amazonaws.com/REPO-NAME:grafana

# as an example
docker tag grafana/grafana-enterprise 466956024587.dkr.ecr.eu-west-2.amazonaws.com/attrition-repo:grafana
docker push 466956024587.dkr.ecr.eu-west-2.amazonaws.com/attrition-repo:grafana

```

To install the software

```bash
aws eks update-kubeconfig --region eu-west-2 --name  attr-eks-cluster
cd deployment/k8s-cpu/
kubectl apply -f .
```

This will spawn grafana and mlflow replicas

to test one can check the test section in the `notebooks/employee-attr-train-valid.ipynb`


We ca see the external urls for grafana and the mlflow replica load balancers using 

```kubectl get svc```

```
NAME              TYPE           CLUSTER-IP      EXTERNAL-IP                                                              PORT(S)                         AGE
attrflow-elb      LoadBalancer   10.100.18.128   ae446d0141fbd4037aef4fe5fcd3a5d8-402455921.eu-west-2.elb.amazonaws.com   5000:32550/TCP,5001:31203/TCP   166m
example-service   LoadBalancer   10.100.70.25    a592b1c302eca4583b7f6eba7fef2c2f-129797025.eu-west-2.elb.amazonaws.com   3000:30723/TCP                  91m
grafana-elb       LoadBalancer   10.100.55.138   abe3fd8ee81d84b16a262a1d59b4ca99-697322696.eu-west-2.elb.amazonaws.com   3000:32050/TCP,5000:31656/TCP   97m
kubernetes        ClusterIP      10.100.0.1      <none>                                                                   443/TCP                         167m
```

