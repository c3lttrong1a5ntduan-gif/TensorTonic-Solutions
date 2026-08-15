import numpy as np
def k_means_assignment(points, centroids):
    """
    Assign each point to the nearest centroid.
    """
    # Write code here
    result = []
    for p in points:
        best_d = float("inf")
        best_j = 0
        for i,c in enumerate(centroids):
            
            dis = sum((p[dim] - c[dim])**2 for dim in range(len(p)))
            if dis < best_d:
                best_d = dis
                best_j = i 
        result.append(best_j)
    return result
    