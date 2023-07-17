# Installation

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

```
sudo apt  install awscli
mlflow sagemaker build-and-push-container --build --push -c for-sagemaker-deployment
```

```
helm repo add superset http://apache.github.io/superset/


helm upgrade --install --values my-values.yaml superset superset/superset
```