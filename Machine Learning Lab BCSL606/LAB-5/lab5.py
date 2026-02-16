# Develop a program to implement k-Nearest Neighbour algorithm to classify the randomly generated 100 values of x in the range of [0,1]. Perform the following based on dataset generated. a. Label the first 50 points {x1,……,x50} as follows: if (xi ≤ 0.5), then xi ∊ Class1, else xi ∊ Class1 b. Classify the remaining points, x51,……,x100 using KNN. Perform this for k=1,2,3,4,5,20,30

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Generate random data
data = np.random.rand(100)

# Label first 50 points
labels = ["Class1" if x <= 0.5 else "Class2" for x in data[:50]]

# Euclidean distance (1D case)
def euclidean_distance(x1, x2):
    return abs(x1 - x2)

# k-NN classifier
def knn_classifier(train_data, train_labels, test_point, k):
    distances = [
        (euclidean_distance(test_point, train_data[i]), train_labels[i])
        for i in range(len(train_data))
    ]
    distances.sort(key=lambda x: x[0])
    k_nearest_neighbors = distances[:k]
    k_nearest_labels = [label for _, label in k_nearest_neighbors]
    return Counter(k_nearest_labels).most_common(1)[0][0]

# Split dataset
train_data = data[:50]
train_labels = labels
test_data = data[50:]
k_values = [1, 2, 3, 4, 5, 20, 30]
print("--- k-Nearest Neighbors Classification ---")
print("Training dataset: First 50 points labeled based on rule (x <= 0.5 → Class1, x > 0.5 → Class2)")
print("Testing dataset: Remaining 50 points\n")
results = {}

# Classification
for k in k_values:
    print(f"\nResults for k = {k}:")
    classified_labels = [
        knn_classifier(train_data, train_labels, test_point, k)
        for test_point in test_data
    ]
    results[k] = classified_labels
    for i, label in enumerate(classified_labels):
        print(f"Point x{i+51} (value: {test_data[i]:.4f}) → {label}")
print("\nClassification complete.\n")

# Visualization
for k in k_values:
    classified_labels = results[k]
    class1_points = [
        test_data[i] for i in range(len(test_data))
        if classified_labels[i] == "Class1"
    ]
    class2_points = [
        test_data[i] for i in range(len(test_data))
        if classified_labels[i] == "Class2"
    ]
    plt.figure(figsize=(10, 6))

    # Training data
    plt.scatter(
        train_data,
        [0] * len(train_data),
        c=["blue" if label == "Class1" else "red" for label in train_labels],
        label="Training Data",
        marker="o"
    )

    # Test data
    plt.scatter(class1_points, [1] * len(class1_points),
                label="Class1 (Test)", marker="x")
    plt.scatter(class2_points, [1] * len(class2_points),
                label="Class2 (Test)", marker="x")
    plt.title(f"k-NN Classification Results for k = {k}")
    plt.xlabel("Data Value")
    plt.ylabel("Level (0 = Train, 1 = Test)")
    plt.legend()
    plt.grid(True)
    plt.show()