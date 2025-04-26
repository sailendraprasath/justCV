import numpy as np
from numpy import genfromtxt

data = genfromtxt('data_banknote_authentication.txt', delimiter=',')
print(data)

labels = data[:,4]
print(labels)
features = data[:,0:4]
print(features)
print(labels,features,data)