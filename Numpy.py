import numpy as np

a=np.array([[5,9],[3,19],[45,32],[23,87],[21,94]])

print("Dimension of an Array:",a.ndim)
print("Size of data in bytes:",a.itemsize)
print("Type of elements are present in an array:",a.dtype)
print("Number of elements present in an array:",a.size)
print("Shape of an array:",a.shape)
b=np.zeros((4,5))
c=np.ones((4,3))
print("Indexing of an array:",a[1:4])
print("Elements of the seconnd column:",a[:,1])
print("Elements of the first column:",a[:,0])
print("Elements of the seconnd row:",a[1,:])
print("Array having all elements equals to zero:",b)
print("Array having all elements qual to one:",c)
d=np.arange(1,5)
print("Array is made by using arange function:",d)
e=np.arange(1,10,2)
print("Array is made by using arange but having the gap of two numbers:",e)
f=np.linspace(1,100,18)
print("Array having 18 elements between 1 to 100 having linearly sapced:",f)
g=a.reshape(2,5)
print("Array after reshaping becomes:",g)
print("Flatened the existing array into one dimension:",np.ravel(g))
print("Minimum value of the array A:",np.min(a))
print("Maximum value in the array A:",np.max(a))
print("Total sum of an array A:",np.sum(a))
print("Total sum of column of an array A:",a.sum(axis=0))
print("Total sum of rows of an array A:",a.sum(axis=1))
print("Square root of every element in the array:",np.sqrt(a))
print("Standard Deviation of the array:",np.std(a))