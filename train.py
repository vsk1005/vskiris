import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import joblib

# Load original Iris dataset (150 records)
iris = load_iris()
X_original = iris.data

# Load new data from CSV (your added records)
new_data = pd.read_csv("new_dataset.csv").values

# Combine old + new data
X = np.vstack((X_original, new_data))

# Train K-Means model
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

model.fit(X)

# Evaluation
score = silhouette_score(X, model.labels_)

print("Total Records Used:", len(X))
print("Clusters:", model.n_clusters)
print("Silhouette Score:", score)

# Save updated model
joblib.dump(model, "iriskmeansml.pkl")