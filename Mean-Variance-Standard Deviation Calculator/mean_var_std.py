import numpy as np

def calculate(list):
    # Convert the list to a numpy array.
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    n_array = np.array(list).reshape(3,3)
    calculations = {}

    # Calculate the mean, variance, standard deviation, max, min, sum. 
    calculations['mean'] = [n_array.mean(axis=0).tolist(), n_array.mean(axis=1).tolist(), n_array.mean().tolist()]
    calculations['variance'] = [n_array.var(axis=0).tolist(), n_array.var(axis=1).tolist(), n_array.var().tolist()]
    calculations['standard deviation'] = [n_array.std(axis=0).tolist(), n_array.std(axis=1).tolist(), n_array.std().tolist()]
    calculations['max'] = [n_array.max(axis=0).tolist(), n_array.max(axis=1).tolist(), n_array.max().tolist()] 
    calculations['min'] = [n_array.min(axis=0).tolist(), n_array.min(axis=1).tolist(), n_array.min().tolist()]
    calculations['sum'] = [n_array.sum(axis=0).tolist(), n_array.sum(axis=1).tolist(), n_array.sum().tolist()]
    
    return calculations