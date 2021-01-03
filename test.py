import numpy as np



arr1 = np.array ([25, 56, 12, 85, 34, 75], dtype=int)
print(arr1)
arr2=np.array([42,3,86,32,856,46],dtype=int)
print(arr2)
narr=np.random.rand(5)
print(narr)
arr1=arr1.astype(complex)
print(arr1)
arr1_mat=arr1.reshape(2,3)
print(arr1_mat)
arr2_mat=arr2.reshape(2,3)
print(arr2_mat)

print(np.add(arr1_mat,arr2_mat)-np.subtract(arr1_mat,arr2_mat)/np.subtract(arr1_mat,arr2_mat))

ar3=np.arange(0,12,2)
print(ar3)

print(np.linspace(10,99,7))

np.random.seed(2)
print(np.random.choice(a=[2,4,7,3,8,9], size=3))


