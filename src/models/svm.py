
import mlflow
from sklearn.svm import LinearSVC
from sklearn.preprocessing import OneHotEncoder
from datetime import datetime
import mlflow.pyfunc


# Define the model class



class SVMFlow(mlflow.pyfunc.PythonModel):
    def __init__(self, penalty, loss, dual, tol,):
        self.penalty = penalty
        self.loss = loss
        self.tol = tol
        self.dual = dual
        self._svc = LinearSVC(penalty=penalty, loss=loss, dual=dual, tol=tol)
        self._enc =  OneHotEncoder(handle_unknown='ignore')


    def fit(self, X, y):
        data=  self._enc.transform(X)
        return self._svc.fit(data, y)
        
    
    def fit_transform(self,X):

        
        self._enc.fit(X)
        return self._enc.transform(X)
    
    def predict(self, X):
        data=  self._enc.transform(X)

        pred = self._svc.predict(data)
        X["prediction"] = pred
        X.to_csv(f"./{datetime.utcnow().strftime('%Y-%m-%dT%H-%M-%S.%s')}.csv")
        return pred
    def save_model(self, path="./src/data/SVCmodel"):
        mlflow.sklearn.save_model(self._svc, path)


