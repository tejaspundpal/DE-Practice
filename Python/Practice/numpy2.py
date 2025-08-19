import numpy as np

arr = [1,2,3,4]

numpy_arr = np.array(arr)
print(numpy_arr,type(numpy_arr))
print("\n")

arr1 = [[1,2,3],[4,5,6],[7,8,9]]

numpy_arr1 = np.array(arr1)
print(numpy_arr1,type(numpy_arr))
print("\n")

ones_arr = np.ones(5)
print(ones_arr)
print("\n")


seq = np.arange(10)
print(seq)
print("\n")


seq1 = np.arange(12)
seq1_ndarray = seq1.reshape([3,4])

print(seq1_ndarray)
print("\n")