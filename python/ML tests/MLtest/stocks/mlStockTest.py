#use this to analyze stock prices

#set whether the program should be verbose in the output or not
verbose=True


# Load libraries
if(verbose): print("importing modules")
import sys, sklearn, os
import pandas as pd
import numpy as np
import datetime as dt
from getData import getData
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
if(verbose): print("done importing")

# Load dataset
if(len(sys.argv)==2):
  symb = sys.argv[1]
else:
  raise ValueError("Must have exactly 1 argument of the stock symbol")


filepath = f"./stockdata/{symb}.csv"

if(not os.path.isfile(filepath)):
  if(verbose): print(f"data file for {symb} does not exist. Generating data...")
  getData(symb,verbose)

#names = ["Date", "Close/Last", "Volume", "Open", "High", "Low", "class"]

if(not os.path.exists(filepath)):
  if(verbose): print("local file not found")
  raise ValueError("No local file found. Possibly bad file path specified")

dataset = pd.read_csv(filepath)
#clean the data some more
#TODO: this may need to change

#convert datetime strings to integer seconds
dataset['date'] = (pd.to_datetime(dataset['date']) - dt.datetime(1970,1,1)).dt.total_seconds()
#set the date as the index
dataset.set_index("date",inplace=True)
#ensure that all NaN values are 0 (just in case something's wrong in the data file)
#dataset.replace(np.NaN,0,inplace=True)




if(verbose):
  print("dataset shape")
  print(dataset.shape)
  print('\n')

  print("dataset head")
  print(dataset.head(10))
  print('\n')

  print("dataset description")
  print(dataset.describe())
  print('\n')

  # class distribution
  # print("group data by classes")
  # print(dataset.groupby('class').size())
  # print('\n')

# Split-out validation dataset
print("splitting training and validation data")
array = dataset.values
X = array[:,1:-1]
Y = array[:,-1].astype("str")

if(verbose):
  print("X","\n",X[:10])
  print("Y","\n",Y[:10])

validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)

# Test options and evaluation metric
seed = 7
scoring = 'accuracy'


# Spot Check Algorithms
print("assigning models")
models = [
  # ('LR', LogisticRegression(max_iter=128),
  ('LDA', LinearDiscriminantAnalysis()),
  ('KNN', KNeighborsClassifier()),
  ('CART', DecisionTreeClassifier()),
  ('NB', GaussianNB()), #gaussian naive bayes
  ('SVM', SVC()) #support vector machine/classification
]

# evaluate each model in turn
print("evaluating models")
results = []
names = []
print("mdl\tmean\t\tstdev")
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffle=True)
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring, error_score='raise')
	results.append(cv_results)
	names.append(name)
	msg = "%s:\t%f\t(%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)


# Make predictions on validation dataset
print("make predictions")
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print("Accuracy score: ",accuracy_score(Y_validation, predictions))
print("confusion matrix","\n",confusion_matrix(Y_validation, predictions))
print("classification report","\n",classification_report(Y_validation, predictions))