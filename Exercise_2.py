import numpy as np
import matplotlib.pyplot as plt 
#Arr=np.array([[56,98,21],[32,71,74],[10,0,97],[38,30,18]])
#positions=np.argwhere(Arr>20)
#greater=np.argwhere(Arr[:,1]<20)
#Where=np.where(Arr[:,1]>10,Arr[:,2],Arr[:,2]*2)
#print("Positions of elements in second columns where elements are greter than 20\n",Arr[greater])
#print("Positions where element is not equal to zero ",positions)
#print(Where)
#ex1=np.argwhere(Arr[:,1]==98)
#ex2=np.argwhere(Arr[:,2]>21)
#print(ex1," ",ex2)
#print("Values:", Arr[ex1], Arr[ex2])
#Where=np.where(Arr[:,1]>12,Arr[:,2]>=21,Arr[:,2]*0)
#print(Arr[Where])

#*****Random Numbers*********
#np.random.seed(100)
#arr=np.random.random(size=(4,3)).round(3)
#print(arr)
#uniform distribution
ran_uni=np.random.uniform(1,50,size=10).round(2)
#plt.hist(ran_uni)
#print(ran_uni)
#plt.show()
#Normal Distribution
arr=np.random.normal(10,3,size=(100)).round(3)

print(arr)
#plt.hist(arr[:10])
#plt.show()
#Random Sampling
#arr1=np.arange(100)
#print(np.random.choice(arr1,size=20,replace=False))
#plt.hist(np.random.choice(arr1,size=20,replace=False))
#plt.show()
#**************Bnomial Distribution************
#binomial=np.random.binomial(n=3,p=0.2,size=10)
#Mean=np.mean(binomial)
#print(binomial)
#plt.hist(binomial,bins=5)
#print("Mean  of Binomial Distribution Experiment:",Mean)
#splt.show()
#union=np.union1d(A,B) returns the union of two arrays
#intersect=np.intersect1d(A,B) returns the intersection of two arrays
#diff=np.setdiff1d(A,B) returns the difference between two arrays
np.random.seed(100)
alphabets=list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
A=np.random.choice(alphabets,10,)
B=np.random.choice(alphabets,20)
C=np.random.choice(alphabets,5)
#print("Elements that are present in array A:",A)
#print("Elements that are present in array B:",B)
#print("Elements that are present in arrays C:",C)
intersect=np.intersect1d(A,B)
diff=np.setdiff1d(intersect,C)
#print("Intersection between A and B:",intersect)
#print("Elemenents That are present in A and B but not present in C",diff)
diff3=np.setdiff1d(A,B,C)
#print(diff3)