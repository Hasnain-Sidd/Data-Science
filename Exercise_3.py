import numpy as np 

#Question#01
two_D=np.random.random(size=(5,3))
two_D=5+two_D*5
two_D=two_D.round(2)
#print(two_D)
#Question#02

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
position=np.arange(10,150,20)
i=0
while i<20:
    iris_2d[position]=np.nan
    
    i+=1
 #Question#3    
#print(iris_2d)
missing_value=np.isnan(iris_2d)

#print(missing_value)
#Question#04
position=np.argwhere(np.isnan(iris_2d)==True)
#print(position)
#Qustion#05
No_Nan=np.argwhere(np.isnan(iris_2d)==False)
#print(No_Nan)
#Question#07
Mean=np.mean(iris_2d,axis=1)

#print(Mean)
#print(Mean.shape)
#Question#08
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
intersect=np.intersect1d(a,b)
#print(intersect)

#Question#09
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
diff=np.setdiff1d(a,b)
print(diff)