import sklearn
from sklearn import datasets
from sklearn.datasets import load_iris
iris = load_iris()

#splitting train and test datasets
from sklearn.model_selection import train_test_split
x,y,z,a = train_test_split(iris.data, iris.target, test_size=0.1)
#x is train_iris {all features values counting 90%}
#y is remaining test_iris {10% of features}
#z is train_target {All tables containing 90% of iris target}
#a is test_target {remaning 10% of iris target}


#calling decision tree classifier
from sklearn import tree
dsclf = tree.DecisionTreeClassifier()

#now training data with decision
trained = dsclf.fit(x, z)

#now time for prediction
output = trained.predict(y)
print(output)

#checking accuracy %age
from sklearn.metrics import accuracy_score
check_pct = accuracy_score(a,output)
print(check_pct)
