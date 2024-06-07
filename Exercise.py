### Q1.  Create a 2x2x2 3-D array containing total 8 elements.
import numpy as np

#a=np.array([[[3,5],[2,5]],[[10,3],[98,21]],[[45,71],[291,871]]])
#Q2.  Replace the 1st element of the above 3-D array with 10
#a[0,0,0]=10
#print(a)
#b=np.array([[4,3],[5,7],[9,21]])
#url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
#iris_arr = np.genfromtxt(url, delimiter=',', dtype='object')
#print(iris_arr)
#print("Shape of the array is:",a.shape)

#a=np.array([5,6,3,7,10,43,29])
#i=0
#while i<a.size :
#    if a[i]==0:
#     print("Array contain a 0 value!")
#    else:
#      print("Array does not contain a zero value!")
#i+=1

# convert List into one dimensional array
#list=[12.23, 13.32, 100, 36.32]
#arr=np.array(list)
#print(type(arr))


#4. Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.
#[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#Update sixth value to 11
#[ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]
#zeros=np.zeros(10)
#zeros[6]=11
#print(zeros) 

#5. Write a NumPy program to create an array with values ranging from 12 to 38.
#Expected Output:
#[12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

arr=np.arange(12,38)
arr2=arr
i=arr2.size-1
while i>=0:
    print(arr2[i])
    i-=1