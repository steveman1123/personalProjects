#a general ML test for CSV style data. Specify the data file path, column names, and Y name (dependent variable column name)


# Load libraries
import sys, sklearn, os
import scipy, numpy, pandas

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

from sklearn.utils._testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning


@ignore_warnings(category=ConvergenceWarning)
def main():
  # Load dataset
  #dependent variable should always be the last column of names

  #filepath="./datasets/adult/adult.data"
  #names = ['age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','class']

  #filepath="./datasets/breast-cancer/breast-cancer-wisconsin.data"
  #names = ['id', 'clump-thickness', 'cell-size-uniformity', 'cell-shape-uniformity', 'marginal-adhesion','single-cell-size','bare-nuclei','bland-chromatin','normal-nucleoli','mitosis','class']

  #filepath = "./datasets/iris/iris.data"
  #names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']

  #filepath = "./datasets/mushroom/agaricus-lepiota.data"
  #names = ["class","cap-shape", "bruises?", "cap-color", "cap-surface", "gill-attachment", "gill-color", "gill-size", "gill-spacing", "habitat", "odor", "population", "ring-number", "ring-type", "spore-print-color", "stalk-color-above-ring", "stalk-color-below-ring", "stalk-root", "stalk-shape", "stalk-surface-above-ring", "stalk-surface-below-ring", "veil-color", "veil-type"]
  
  filepath="./datasets/wines/winequality-red.csv"
  names=["fixed acidity","volatile acidity","citric acid","residual sugar","chlorides","free sulfur dioxide","total sulfur dioxide","density","pH","sulphates","alcohol","quality"]

  Yname = "quality" #name of the dependent variable column (what we're solving for. Usually the last column)

  #ensure that the file exists
  if(not os.path.exists(filepath)):
    print("file not found:",filepath)
    sys.exit()
  
  
  dataset = pandas.read_csv(filepath, names=names)
  
  print("using data from",filepath)
  
  #convert strings of the independent variables to integers (to be classified better)
  for c in dataset.loc[:,dataset.columns!=Yname]:
    if(dataset[c].dtype=="object"):
      for i,e in enumerate(set(dataset[c])):
        dataset[c].replace(e,i, inplace=True)


  verbose=False
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
    print("group data by dependent classes")
    print(dataset.groupby(Yname).size())
    print('\n')


  # Split-out validation dataset
  print("splitting dependent from independents")
  X = dataset.loc[:,dataset.columns!=Yname].values
  Y = dataset.loc[:,dataset.columns==Yname][Yname].values

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
  print("model\tmean\t\tstdev")
  for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed, shuffle=True)
    
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    
    results.append(cv_results)
    names.append(name)
    msg = "%s:\t%f\t%f" % (name, cv_results.mean(), cv_results.std())
    print(msg)




  # Make predictions on validation dataset
  print("\nmake predictions")
  knn = KNeighborsClassifier()
  knn.fit(X_train, Y_train)
  predictions = knn.predict(X_validation)
  print("Accuracy score: ",accuracy_score(Y_validation, predictions))
  print("\nconfusion matrix","\n",confusion_matrix(Y_validation, predictions))
  print("\nclassification report","\n",classification_report(Y_validation, predictions))




if(__name__=='__main__'):
  main()
