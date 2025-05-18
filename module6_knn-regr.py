#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

class NearestNeighborRegressor:
    def __init__(self, neighbors_count):
        self.neighbors_count = neighbors_count
        self.feature_array = None
        self.label_array = None

    def train(self, feature_list, label_list):
        self.feature_array = np.array(feature_list, dtype=float)
        self.label_array = np.array(label_list, dtype=float)

    def estimate(self, query_point):
        distances = np.abs(self.feature_array - query_point)
        nearest_idx = np.argsort(distances)[:self.neighbors_count]
        return np.mean(self.label_array[nearest_idx])

def main():
    total_records = int(input("How many data points would you like to enter? "))
    if total_records <= 0:
        print("Error: Please enter a positive number of data points.")
        return
    k_neighbors = int(input(f"Enter the number of neighbors (k), between 1 and {total_records}: "))
    if k_neighbors < 1 or k_neighbors > total_records:
        print(f"Error: k must be at least 1 and at most {total_records}.")
        return
    feature_list = []
    label_list = []
    print(f"Please input your {total_records} points (first x, then y):")
    for idx in range(1, total_records + 1):
        x_val = float(input(f"  Point #{idx} – x coordinate: "))
        y_val = float(input(f"  Point #{idx} – y coordinate: "))
        feature_list.append(x_val)
        label_list.append(y_val)
    model = NearestNeighborRegressor(k_neighbors)
    model.train(feature_list, label_list)
    query_x = float(input("Enter an X value to predict its Y: "))
    predicted_y = model.estimate(query_x)
    print(f"Predicted Y for x = {query_x}: {predicted_y}")
if __name__ == "__main__":
    main()


# In[ ]:




