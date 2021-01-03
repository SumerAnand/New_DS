import numpy as np
mat1=np.array([[2,3,2],[1,0,3],[2,2,3]])
mat2=np.array([1,2,3])
print(np.linalg.solve(mat1,mat2))

a=np.array([[-4,10],[2,-5]])
b=np.array([6,3])
print(np.linalg.det(a))