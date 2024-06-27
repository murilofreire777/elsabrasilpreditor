import pickle
from sklearn import tree, ensemble
from sklearn.neighbors import KNeighborsClassifier
#pip install pandas
#pip install scikit-learn==1.2.2

class Predictor:

    def __init__(self) -> None:
        self.hipertension_pkl_filename = "hipertension_model_rf.pkl"
        self.diabetes_pkl_filename = "diabetes_model_knn.pkl"
        with open(self.hipertension_pkl_filename, 'rb') as file:
            self.hipertension_model = pickle.load(file)
        with open(self.diabetes_pkl_filename, 'rb') as file:
            self.diabetes_model = pickle.load(file)

    def PredictHipertension(self, data):
        #print(self.hipertension_model.feature_names_in_)
        return self.hipertension_model.predict(data)

    def PredictDiabetes(self, data):
        return self.diabetes_model.predict(data)

    def GetPredictProbaHipertension(self, data):
        return self.hipertension_model.predict_proba(data)
    
    def GetPredictProbaDiabetes(self, data):
        pass

#ht_pkl_filename = "hipertension_model_rf.pkl"

#with open(ht_pkl_filename, 'rb') as file:
#    hipertension_model = pickle.load(file)

XH_test_filename = "XH_test.pkl"
#yH_test_filename = "yH_test.pkl"

with open(XH_test_filename, 'rb') as file:
    XH_test = pickle.load(file)

#with open(yH_test_filename, 'rb') as file:
#    yH_test = pickle.load(file)

#dia_pkl_filename = "diabetes_model.pkl"
#with open(dia_pkl_filename, 'rb') as file:
#    diabetes_model = pickle.load(file)

#print(XH_test)
#score = hipertension_model.score(XH_test, yH_test)
#print(score)