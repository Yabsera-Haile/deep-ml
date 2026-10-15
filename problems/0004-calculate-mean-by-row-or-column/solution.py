import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	axis= 1 if mode =='row' else 0
	matrix=np.array(matrix)
	means=matrix.mean(axis=axis)
	return means