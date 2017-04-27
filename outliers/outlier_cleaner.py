#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    from sklearn.metrics import mean_squared_error
    index = 0
    for item in ages:
        y_true = [net_worths[index]]
        y_pred = [predictions[index]]
        error = mean_squared_error(y_true, y_pred)
        itemtuple = (item, y_true, error)
        cleaned_data.append(itemtuple)
        index += 1
    
    cleaned_data.sort(key=lambda x: x[2])
    cleaned_data = cleaned_data[:80]
    return cleaned_data

