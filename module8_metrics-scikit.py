#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    num_samples = int(input("Enter the number of data points (positive integer): "))
    if num_samples <= 0:
        print("Error: Number of data points must be positive.")
        return

    actual_labels = np.empty(num_samples, dtype=int)
    predicted_labels = np.empty(num_samples, dtype=int)

    print(f"Please provide {num_samples} pairs of labels (actual then predicted, each 0 or 1):")
    for i in range(num_samples):
        true_val = int(input(f"  Record #{i+1} – actual class (0 or 1): "))
        pred_val = int(input(f"  Record #{i+1} – predicted class (0 or 1): "))
        actual_labels[i] = true_val
        predicted_labels[i] = pred_val

    precision = precision_score(actual_labels, predicted_labels)
    recall = recall_score(actual_labels, predicted_labels)

    print(f"\nPrecision: {precision:.2f}")
    print(f"Recall: {recall:.2f}")

if __name__ == "__main__":
    main()


# In[ ]:




