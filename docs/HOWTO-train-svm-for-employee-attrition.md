# training

Put the csv for training data in data

Then checkout the notebook in `notebooks/employee-attr-train-valid.ipynb`

We dont focus on training but for what its worth we have an SVM with L1 loss

# Mlflow

Mlflow is chosen to host the model as it is fast ... easy to package the model and easy to upload to ecr.

It also has the ability to expand to the full lifecycle of the ML pipeline via training however using a notebook instead of SVM  is more than enough.

