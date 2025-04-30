import numpy as np
from numpy import genfromtxt

data = genfromtxt('data_banknote_authentication.txt', delimiter=',')


labels = data[:,4]
features = data[:,0:4]


x = features
y = labels


from sklearn.model_selection import train_test_split 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)
# print(len(x_train))
# print(len(x))
# print(len(x_test))

from sklearn.preprocessing import MinMaxScaler

scaler_object = MinMaxScaler
scaler_object.fit(x_train)

scaled_x_train = scaler_object.transform(x_train)
scaled_x_test = scaler_object.transform(x_test)
scaled_x_train.max()

from keras.models import Sequential
from keras.layers import Dense 

print(Sequential)
print(Dense)
print(Sequential)







