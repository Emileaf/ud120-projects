#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
    enron_data["LASTNAME FIRSTNAME"]["feature_name"]
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"]["feature_name"]

What is the total value of the stock belonging to James Prentice?
Wesley Colwell to POI
What’s the value of stock options exercised by Jeffrey K Skilling?
quantified salary
known email address
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))
missingtotal = 0
total = 0
jamesdict = enron_data["PRENTICE JAMES"]
for (person, data) in enron_data.items():    
        if data["total_payments"] == "NaN":
            missingtotal += 1
        total += 1
percent = float(missingtotal)/total
print "missingtotal: ", missingtotal, " percentage: ", percent
print "total: ", len(enron_data)
print "poi total: ", total
#print jamesdict["total_stock_value"]
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]

# print len((enron_data.items()[0])[1])

