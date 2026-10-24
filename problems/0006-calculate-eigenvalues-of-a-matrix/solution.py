import numpy as np
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	matrix =np.array(matrix)
	det=np.linalg.det(matrix)
	trace=np.trace(matrix)
	temp=np.sqrt(trace**2-4*det)
	eigenvalues=(trace+np.array([-temp,temp]))/2
	
	return sorted(eigenvalues.tolist(),reverse=True)