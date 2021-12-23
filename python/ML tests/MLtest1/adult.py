# Load libraries
import sys, sklearn, os
import scipy, numpy, pandas

from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
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

verbose=False


# Load dataset
filepath="./datasets/adult/adult.data"
names = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','class']
#dependent variable should always be the last column


if(not os.path.exists(filepath)):
  print("local file not found")
  filepath = "http://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

dataset = pandas.read_csv(filepath, names=names)

for c in dataset:
  #print(dataset[c].dtype)
  if(dataset[c].dtype=="object"):
    for i,e in enumerate(set(dataset[c])):
      dataset[c].replace(e,i, inplace=True)
#sys.exit()

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
  print("group data by classes")
  print(dataset.groupby('class').size())
  print('\n')


# Split-out validation dataset
print("splitting dependent from independents")
array = dataset.values
X = array[:,0:-1]
Y = array[:,-1]


#print("X","\n",X[:10])
#print("Y","\n",Y[:10])

print("splitting training and validation data")
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size, random_state=seed)



# Test options and evaluation metric
seed = 7
scoring = 'accuracy'


# Spot Check Algorithms
print("assigning algorithms")
models = [
  ('LR', LogisticRegression(max_iter=150)),
  ('LDA', LinearDiscriminantAnalysis()),
  ('KNN', KNeighborsClassifier()),
  ('CART', DecisionTreeClassifier()),
  ('NB', GaussianNB()), #gaussian naive bayes
  ('SVM', SVC()) #support vector machine/classification - https://stackoverflow.com/questions/31681373/making-svm-run-faster-in-python
]

# evaluate each model in turn
print("evaluating models")
results = []
names = []
print("mdl\tmean\t\tstdev")
for name, model in models:
	kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffle=True)
	
	cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
	
	results.append(cv_results)
	names.append(name)
	msg = "%s:\t%f\t(%f)" % (name, cv_results.mean(), cv_results.std())
	print(msg)


# Compare Algorithms
'''
fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
#print("algorithm comparison")
# plt.show()
'''


# Make predictions on validation dataset
print("make predictions")
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print("Accuracy score: ",accuracy_score(Y_validation, predictions))
print("confusion matrix","\n",confusion_matrix(Y_validation, predictions))
print("classification report","\n",classification_report(Y_validation, predictions))

