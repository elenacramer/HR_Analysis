from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf
import pandas as pd 


log_clf = LogisticRegression()
rnd_clf = RandomForestClassifier()
svm_clf = SVC()
clf_list = [log_clf, rnd_clf, svm_clf]

def ml_clf(X_train, y_train, X_test, y_test, clf_list=clf_list):
  score=[]
  name=[]
  score_frame=pd.DataFrame()
  for clf in clf_list:
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    # adding to the lists
    score.append(accuracy_score(y_test, y_pred))
    name.append(clf.__class__.__name__)
  score_frame["name"]=name
  score_frame["score"]=score
  return score_frame.sort_values(by=["score"])

def dl_clf(X_train, y_train, X_test, y_test, epoch_n, batch_n):
  input_dim = X_train.shape[0]
  layer_unit = input_dim*2
  hidden = int(input_dim / 2)
  # early stopping
  es = tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=1)
  # create model
  model = Sequential()
  model.add(Dense(layer_unit, input_dim=input_dim, activation="relu"))
  model.add(Dense(hidden, activation="relu"))
  model.add(Dense(1, activation="sigmoid"))
  # compile model
  model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
  # fit
  history = model.fit(X_train, y_train, epochs=epoch_n, batch_size=batch_n, validation_data=(X_test, y_test),callbacks=[es])
  return history 