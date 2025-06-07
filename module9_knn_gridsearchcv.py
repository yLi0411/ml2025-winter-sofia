#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, KFold
from sklearn.metrics import accuracy_score

def main():
    training_count = int(input("How many training samples? "))
    if training_count <= 0:
        print("Error: number of training samples must be positive.")
        return
    if training_count < 2:
        print("Error: need at least 2 samples to run k-NN.")
        return

    training_features = np.empty((training_count, 1), dtype=float)
    training_labels = np.empty(training_count, dtype=int)

    print(f"Enter {training_count} training pairs (feature X then label Y):")
    for i in range(training_count):
        x_val = float(input(f"  Sample #{i+1} — feature X: "))
        y_val = int(input(f"  Sample #{i+1} — class label Y: "))
        training_features[i, 0] = x_val
        training_labels[i] = y_val

    test_count = int(input("How many test samples? "))
    if test_count <= 0:
        print("Error: number of test samples must be positive.")
        return

    test_features = np.empty((test_count, 1), dtype=float)
    test_labels = np.empty(test_count, dtype=int)

    print(f"Enter {test_count} test pairs (feature X then label Y):")
    for i in range(test_count):
        x_val = float(input(f"  Sample #{i+1} — feature X: "))
        y_val = int(input(f"  Sample #{i+1} — class label Y: "))
        test_features[i, 0] = x_val
        test_labels[i] = y_val

    cv_folds = min(5, training_count)
    cv = KFold(n_splits=cv_folds, shuffle=True, random_state=0)

    max_k = min(10, training_count - 1)
    param_grid = {'n_neighbors': list(range(1, max_k + 1))}

    grid_search = GridSearchCV(
        KNeighborsClassifier(),
        param_grid,
        cv=cv,
        scoring='accuracy',
        n_jobs=-1
    )
    grid_search.fit(training_features, training_labels)

    best_k = grid_search.best_params_['n_neighbors']
    best_model = grid_search.best_estimator_
    predictions = best_model.predict(test_features)
    test_accuracy = accuracy_score(test_labels, predictions)

    print(f"\nOptimal k: {best_k}")
    print(f"Test set accuracy: {test_accuracy:.2f}")

if __name__ == "__main__":
    main()


# In[ ]:





# In[ ]:




