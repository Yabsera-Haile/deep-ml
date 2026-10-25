import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x = np.zeros(b.shape)


	diag=np.diag(A)
	for _ in range(n):
		x=(b - ((A @ x) - (diag*x)))/diag
	
	return x