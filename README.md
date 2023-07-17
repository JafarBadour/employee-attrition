# Structure

```
.
├── data
│   ├── 20230216_mle_assignment.md
│   └── employee-attrition.csv
├── deployment
│   ├── k8s-cpu
│   │   ├── deployment.yaml
│   │   ├── grafana.yaml
│   │   ├── README.md
│   │   └── svc_elb.yaml
│   ├── mlflow
│   │   ├── build-and-push.sh
│   │   ├── Dockerfile
│   │   ├── README.md
│   │   └── run.sh
│   └── terraform
│       ├── cluster
│       │   ├── ecr.tf
│       │   ├── eks.tf
│       │   ├── iam_policy.json
│       │   ├── main.tf
│       │   ├── node-groups.tf
│       │   ├── README.md
│       │   ├── remote-state.tf
│       │   ├── terraform.tfstate
│       │   ├── terraform.tfstate.backup
│       │   └── vars.tf
│       └── iam_policy.json
├── docs
│   ├── HOWTO-host-deploy-svm-for-employee-attrition.md
│   └── HOWTO-train-svm-for-employee-attrition.md
├── notebooks
│   └── employee-attr-train-valid.ipynb
├── README.md
├── requirements
│   └── cpu-requirements.txt
└── src
    ├── data
    │   └── SVCmodel
    │       ├── conda.yaml
    │       ├── MLmodel
    │       ├── model.pkl
    │       ├── python_env.yaml
    │       └── requirements.txt
    ├── models
    │   └── svm.py
    └── monitor
        └── sqlpusher.py
```
# Installation
One needs to install following version of awscli and kubectl as well as terraform

| tool | version |  
| terraform | v1.4.2 |  
| aws | aws-cli/2.13.1 |  
| kubectl | v5.0.1 |


with conda 
```bash
conda create -p ./venv python==3.7
conda activate ./venv
```
then

```
pip install -r requirements/dev-requirements.txt
```

```
curl https://pyenv.run | bash
python -m  pip install virtualenv
PATH="$HOME/.pyenv/bin:$PATH"


``` 

Check `docs/HOWTO-train-svm-for-employee-attrition.md` for more information on how to train 
and `docs/HOWTO-host-deploy-svm-for-employee-attrition.md` for hosting and deployment