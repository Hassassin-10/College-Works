# For a given set of training data examples stored in a .CSV file, implement and demonstrate the Find-S algorithm to output a description of the set of all hypotheses consistent with the training examples.

import pandas as pd

def find_s_algorithm(file_path):
    data = pd.read_csv(file_path)

    print("Training data:")
    print(data)

    attributes = data.columns[:-1]      # All columns except last
    class_label = data.columns[-1]      # Last column is target

    # Initialize hypothesis with most specific values
    hypothesis = ['?' for _ in attributes]

    for index, row in data.iterrows():
        if row[class_label] == 'Yes':   # Consider only positive examples
            for i, value in enumerate(row[attributes]):
                if hypothesis[i] == '?' or hypothesis[i] == value:
                    hypothesis[i] = value
                else:
                    hypothesis[i] = '?'
    return hypothesis

file_path = "C:\\H-ASSASSIN\\Codeing\\College Works\\Machine Learning Lab BCSL606\\LAB-4\\training_data.csv"
hypothesis = find_s_algorithm(file_path)
print("\nThe final hypothesis is:", hypothesis)