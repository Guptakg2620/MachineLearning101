#!/usr/bin/python

""" 
    Used a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################


from sklearn.svm import SVC
clf = SVC(kernel="rbf", C = 10000.0)



t0 = time()
clf.fit(features_train, labels_train)
print "Fit training time:", round(time()-t0, 3), "s"


t0 = time()
pred = clf.predict(features_test)
print "Pred training time:", round(time()-t0, 3), "s"
print('Number of events predicted in Chris class is', sum(clf.predict(features_test) ==1))
from sklearn.metrics import accuracy_score
acc = accuracy_score(pred, labels_test)

print acc



#########################################################


