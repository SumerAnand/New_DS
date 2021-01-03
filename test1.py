import numpy as np
na=np.array([[1,2,3,4],
            [5,6,7,8]])
xa=np.cumsum(na,axis=1)
print(xa)

xm=np.mean(na,axis=0)
print(xm)

print(np.diag([4,5,6],k=1))

a1=np.array([1,4,7,8,6,4,2])
condition=np.logical_and(a1>2,a1<6)
a2=np.select([~condition,condition],[a1,-a1])
print(a2)
mat = np.array([[1,21,3],[5,4,2],[56,12,4]])
print(mat)

a3=np.arange(9)*2
print(a3)