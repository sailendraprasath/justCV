import numpy as np
from numpy import genfromtxt

data = genfromtxt('data_banknote_authentication.txt', delimiter=',')


labels = data[:,4]
features = data[:,0:4]


x = features
y = labels

print(features)
print(labels)