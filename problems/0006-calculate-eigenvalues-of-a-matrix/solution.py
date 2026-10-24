import torch

def calculate_eigenvalues(matrix: torch.Tensor) -> torch.Tensor:
    """
    Compute eigenvalues of a 2x2 matrix using PyTorch.
    Input: 2x2 tensor; Output: 1-D tensor with the two eigenvalues in descending order (highest to lowest).
    """
    # return torch.sort(torch.linalg.eigvals(matrix).real,descending=True).values
    det=torch.linalg.det(matrix)
    trace=torch.trace(matrix)

    temp=torch.sqrt(trace**2 - (4*det))
    eigenvalues=(trace+torch.stack([temp,-temp]))/2
    return torch.sort(eigenvalues.real,descending=True).values