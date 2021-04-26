
# coding: utf-8

# In[ ]:
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import roc_curve, roc_auc_score, accuracy_score, cohen_kappa_score
import pandas as pd

import matplotlib.pyplot as plt
#%matplotlib inline

def logistic_regression(df):

    
    dmsc5r = df.copy()

    del dmsc5r['12 or less']
    del dmsc5r['8 or less']

    columns = dmsc5r.columns

    data_cols = [c for c in columns if c != "10 or less"]
    X = dmsc5r[data_cols].values
    y = dmsc5r["10 or less"].values
    x_train, x_test, y_train, y_test = train_test_split(X, y,)

    model = LogisticRegression(solver="lbfgs", class_weight="balanced")
    model.fit(x_train, y_train)

    print("Acc score: {:.2f}".format(accuracy_score(y_test, model.predict(x_test))))
    print("Cohen's Kappa: {:.2f}".format(cohen_kappa_score(y_test, model.predict(x_test))))
    positive_class_prediction = model.predict_proba(x_test)[:,1]
    fpr, tpr, _ = roc_curve(y_test, positive_class_prediction)
    auc = roc_auc_score(y_test, positive_class_prediction)

    plt.plot(fpr, tpr, label="Logistic Regression: AUC = {:.2f}".format(auc), lw=2)
    plt.ylabel("True Positive Rate")
    plt.xlabel("False Positive Rate")
    plt.legend()

