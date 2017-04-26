#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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
### your code goes here ###

from sklearn.svm import SVC
clf = SVC(C=10000, kernel="rbf")
print "classifier created"
t0 = time()

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100]

### info on the data
print "no. of Chris training emails:", sum(labels_train)
print "no. of Sara training emails:", len(labels_train)-sum(labels_train)
    
print "starting fit..."
clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"

t1= time()
pred = clf.predict(features_test)
print "predicting time:", round(time()-t1, 3), "s"

print "Number of predicted Christ emails:", sum(pred)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, pred, True)
print accuracy

#########################################################


