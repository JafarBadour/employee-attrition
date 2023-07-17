# training

Put the csv for training data in data

Then checkout the notebook in `notebooks/employee-attr-train-valid.ipynb`

We dont focus on training but for what its worth we have an SVM with L1 loss

# Mlflow

Mlflow is chosen to host the model as it is fast ... easy to package the model and easy to upload to ecr.

It also has the ability to expand to the full lifecycle of the ML pipeline via training however using a notebook instead of SVM  is more than enough.

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
# installing software
To install the software

```bash
aws eks update-kubeconfig --region eu-west-2 --name  attr-eks-cluster
cd deployment/k8s-cpu/
kubectl apply -f .
```

This will spawn grafana and mlflow replicas

to test one can check the test section in the `notebooks/employee-attr-train-valid.ipynb`
