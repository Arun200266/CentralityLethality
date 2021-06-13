import pandas as pd
import xgboost
from xgboost import XGBClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import precision_score, f1_score, roc_auc_score

# reading data from files
X_train = pd.read_csv('X_train.csv', index_col='index')
y_train = pd.read_csv('y_train.csv', index_col='index')
X_test = pd.read_csv('X_test.csv', index_col='index')
y_test = pd.read_csv('y_test.csv', index_col='index')

# Scaling the features
X_train_cols = list(X_train.columns)
X_test_cols = list(X_test.columns)
scaler = StandardScaler().fit(X_train.values)

X_train = pd.DataFrame(scaler.transform(X_train.values), columns=X_train_cols)
X_test = pd.DataFrame(scaler.transform(X_test.values), columns=X_test_cols)

# training a XgBoost Classifier on the train set
model = XGBClassifier()
model.fit(X_train, y_train)

# predicting on test set
y_pred = model.predict(X_test)

precision_score(y_test, y_pred)  # 0.6482412060301508
f1_score(y_test, y_pred)  # 0.4307178631051753
roc_auc_score(y_test, y_pred)  # 0.6510903483309144

# plotting importance of each feature
xgboost.plot_importance(model)
