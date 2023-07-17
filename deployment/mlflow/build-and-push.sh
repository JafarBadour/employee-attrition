#/bin/bash
mkdir temp
cp -r ../../src/data/SVCmodel temp/
cp -r ../../src/ temp/src/
cp -r ../../requirements/cpu-requirements.txt temp/cpu-requirements.txt
cp ../../.env temp/.env
sudo docker build -t mlflow-attr:latest .
rm -r temp
aws ecr get-login-password --region eu-west-2 | sudo docker login --username AWS --password-stdin 466956024587.dkr.ecr.eu-west-2.amazonaws.com
sudo docker tag  mlflow-attr:latest 466956024587.dkr.ecr.eu-west-2.amazonaws.com/attrition-repo:latest
sudo docker push 466956024587.dkr.ecr.eu-west-2.amazonaws.com/attrition-repo:latest