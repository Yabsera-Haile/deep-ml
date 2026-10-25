import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
	x = np.zeros(b.shape)


	for _ in range(n):
		diag=np.diag(A)
		x=(b - ((A @ x) - (diag*x)))/diag
	
	return x