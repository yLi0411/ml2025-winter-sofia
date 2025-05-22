#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from sklearn.neighbors import KNeighborsRegressor

def main():
    total_records = int(input("How many data points? "))
    if total_records <= 0:
        print("Error: must be positive."); return

    k_neighbors = int(input(f"Enter k (1–{total_records}): "))
    if not (1 <= k_neighbors <= total_records):
        print("Error: k out of range."); return

    feature_array = np.empty(total_records, dtype=float)
    label_array   = np.empty(total_records, dtype=float)

    print(f"Enter {total_records} points:")
    for i in range(total_records):
        feature_array[i] = float(input(f" x#{i+1}: "))
        label_array[i]   = float(input(f" y#{i+1}: "))

    variance_labels = np.var(label_array)
    print(f"Variance of labels: {variance_labels}")

    X_train = feature_array.reshape(-1, 1)
    y_train = label_array

    model = KNeighborsRegressor(n_neighbors=k_neighbors)
    model.fit(X_train, y_train)

    query_x = float(input("Enter X to predict Y: "))
    y_pred  = model.predict([[query_x]])[0]
    print(f"Predicted Y: {y_pred}")

if __name__ == "__main__":
    main()


# In[ ]:




