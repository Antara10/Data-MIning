
import numpy as np
import matplotlib.pyplot as plt

def initialize_clusters(data, k):
    # Randomly pick k data points as initial cluster centroids
    centroids = data[np.random.choice(data.shape[0], k, replace=False), :]
    return centroids

def assign_points_to_clusters(data, centroids):
    # Compute distances between each data point and the centroids
    distances = np.sqrt(((data - centroids[:, np.newaxis])**2).sum(axis=2))
    # Assign each data point to the closest cluster
    cluster_assignment = np.argmin(distances, axis=0)
    return cluster_assignment

def update_clusters(data, k, cluster_assignment):
    # Update each cluster's centroid to be the mean of all assigned data points
    centroids = np.zeros((k, data.shape[1]))
    for i in range(k):
        centroids[i, :] = np.mean(data[cluster_assignment == i, :], axis=0)
    return centroids

def kmeans(data, k, max_iterations):
    # Initialize cluster centroids
    centroids = initialize_clusters(data, k)
    # Iterate until convergence or maximum number of iterations reached
    for i in range(max_iterations):
        # Assign data points to nearest cluster
        cluster_assignment = assign_points_to_clusters(data, centroids)
        # Update centroids based on assigned data points
        centroids = update_clusters(data, k, cluster_assignment)
    return centroids, cluster_assignment

# Get user input
num_data_points = int(input("Enter the number of data points: "))
num_features = int(input("Enter the number of features: "))
k = int(input("Enter the number of clusters: "))
max_iterations = int(input("Enter the maximum number of iterations: "))

# Generate random data points
data = np.random.randn(num_data_points, num_features)

# Run K-Means clustering on data
centroids, cluster_assignment = kmeans(data, k, max_iterations)

# Plot the data points and cluster centroids
colors = ['r', 'g', 'b', 'y', 'c', 'm']
fig, ax = plt.subplots()
for i in range(k):
    points = data[cluster_assignment == i]
    ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i%len(colors)])
    ax.scatter(centroids[i, 0], centroids[i, 1], s=200, marker='*', c=colors[i%len(colors)])
plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.show()

