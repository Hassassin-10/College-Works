# Develop a program to implement the Naive Bayesian classifier considering Olivetti Face Data set for training. Compute the accuracy of the classifier, considering a few test data sets.

import numpy as np 
from sklearn.datasets import fetch_olivetti_faces 
from sklearn.model_selection import train_test_split, cross_val_score 
from sklearn.naive_bayes import GaussianNB 
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix 
import matplotlib.pyplot as plt

data = fetch_olivetti_faces(shuffle=True, random_state=42) 
X = data.data 
y = data.target 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, 
random_state=42) 
gnb = GaussianNB() 
gnb.fit(X_train, y_train) 
y_pred = gnb.predict(X_test) 
accuracy = accuracy_score(y_test, y_pred)

print(f'Accuracy: {accuracy * 100:.2f}%') 
print("\nClassification Report:") 
print(classification_report(y_test, y_pred, zero_division=1)) 
print("\nConfusion Matrix:") 
print(confusion_matrix(y_test, y_pred)) 
cross_val_accuracy = cross_val_score(gnb, X, y, cv=5, scoring='accuracy') 
print(f'\nCross-validation accuracy: {cross_val_accuracy.mean() * 100:.2f}%') 
fig, axes = plt.subplots(3, 5, figsize=(12, 8)) 
for ax, image, label, prediction in zip(axes.ravel(), X_test, y_test, y_pred): 
    ax.imshow(image.reshape(64, 64), cmap=plt.cm.gray) 
    ax.set_title(f"True: {label}, Pred: {prediction}") 
    ax.axis('off') 
plt.show()