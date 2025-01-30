import random
import pandas as pd
import matplotlib.pyplot as plt

class KMeans:
    def __init__(self, data: pd.DataFrame, k: int, max_iterations=100, tol=1e-4):
        self.data = data
        self.k = k
        self.max_iterations = max_iterations
        self.tol = tol
        self.centroids = self.data.sample(n=k, random_state=42).to_numpy()
        
    def assign_clusters(self):
        distances = []
        for centroid in self.centroids:
            distances.append(((self.data - centroid) ** 2).sum(axis=1))
        distances = pd.DataFrame(distances).T  
        cluster_assignments = distances.idxmin(axis=1)
        return cluster_assignments
            
    def update_centroids(self, cluster_assignments) -> pd.DataFrame:
        new_centroids = []
        for cluster in range(self.k):
            cluster_points = self.data[cluster_assignments == cluster]
            if not cluster_points.empty:
                new_centroids.append(cluster_points.mean().to_numpy())
            else:
                new_centroids.append(data.sample(n=1).to_numpy().flatten())
        
        new_centroids = pd.DataFrame(new_centroids)
        return new_centroids
    
    def check_convergance(self, new_centroids : pd.DataFrame) -> bool:
        if all((new_centroids - pd.DataFrame(self.centroids)).pow(2).sum(axis=1) < self.tol):
            return True
        return False
    
    def run_iterations(self):
        for iteration in range(self.max_iterations):
            cluster_assignments = self.assign_clusters()
            new_centroids = self.update_centroids(cluster_assignments)
            if self.check_convergance(new_centroids):
                break
            self.centroids = new_centroids.to_numpy()
        
        return self.compute_WCSS(cluster_assignments)
    
    def compute_WCSS(self, cluster_assignments):
        wcss = 0
        for cluster in range(self.k):
            cluster_points = self.data[cluster_assignments == cluster]
            if not cluster_points.empty:
                wcss += ((cluster_points - self.centroids[cluster]) ** 2).sum().sum()

        return cluster_assignments, pd.DataFrame(self.centroids, columns=self.data.columns), wcss
        
    def calculate_silhoutte(self, cluster_assignments):
        silhouette_scores = []
        for i, point in self.data.iterrows():
            own_cluster = cluster_assignments[i]

            own_cluster_points = self.data[cluster_assignments == own_cluster].drop(index=i, errors='ignore')
            a_i = ((own_cluster_points - point) ** 2).sum(axis=1).mean() if not own_cluster_points.empty else 0

            b_i = float('inf')
            for cluster in range(self.k):
                if cluster != own_cluster:
                    other_cluster_points = self.data[cluster_assignments == cluster]
                    b_i = min(b_i, ((other_cluster_points - point) ** 2).sum(axis=1).mean() if not other_cluster_points.empty else float('inf'))

            silhouette_scores.append((b_i - a_i) / max(a_i, b_i) if a_i and b_i else 0)

        silhouette_scores = pd.Series(silhouette_scores, index=self.data.index)

        return silhouette_scores


            