import numpy as np
def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	# Your code here
	n=len(vectors)
	num_samples=len(vectors[0])
	vectors=np.array(vectors)
	mean=np.mean(vectors,axis=1)
	mean_centered = vectors - mean[:,None]
	cov = mean_centered @ mean_centered.T
	return (cov/(num_samples-1)).tolist()

