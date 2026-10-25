import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0])!=len(b):
        return -1
	#Manual
    # product= [[0]*len(b[0]) for _ in range(len(a))]
    # for i in range(len(a)):
    #     for j in range(len(b[0])):
    #         product[i][j]=sum([a*b for a,b in zip(a[i],[row[j] for row in b])])
    
    # return product

    #Numpy
    return (np.array(a) @ np.array(b)).tolist()
