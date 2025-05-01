import numpy as np
from numpy import genfromtxt

# Load the dataset
data = genfromtxt('data_banknote_authentication.txt', delimiter=',')

# Split data into features and labels
labels = data[:, 4]
features = data[:, 0:4]

x = features
y = labels

# Split data into training and testing sets
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)

# Scale the feature data
from sklearn.preprocessing import MinMaxScaler

scaler_object = MinMaxScaler()
scaler_object.fit(x_train)

scaled_x_train = scaler_object.transform(x_train)
scaled_x_test = scaler_object.transform(x_test)

# Build the neural network model
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(4, input_dim=4, activation='relu'))  # Input layer
model.add(Dense(8, activation='relu'))               # Hidden layer
model.add(Dense(1, activation='sigmoid'))            # Output layer for binary classification

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(scaled_x_train, y_train, epochs=50, batch_size=2)

# Evaluate the model
from sklearn.metrics import classification_report, confusion_matrix

predictions = model.predict(scaled_x_test)


# Print evaluation metrics
# print(confusion_matrix(y_test, predictions))
print(classification_report(y_test, predictions))

model.save('bank_note_model.h5')

from keras.models import load_model
newmodel = load_model('bank_note_model.h5')
newmodel.predict_classes(scaled_x_test)

