import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
#file_Path="C:\\Users\\PMLS\\Documents\\Stats.txt"
path="C:\\Users\\PMLS\\Documents\\Virat_Kohli.txt"

arr=np.genfromtxt(path)
df=pd.DataFrame(arr)
#NAN=arr[np.isnan(arr[:,2]),:]

#print(df.max(axis=0)) #axis=0 means column wise and axis=1 means row wise
#print(df.mean(axis=0))
Where=np.where(arr[:,2]==1, arr[:,4], arr[:,4]/2)
print(Where)
#arr=np.genfromtxt(file_Path)
#df=pd.DataFrame(arr)

#NAN=np.isnan(df)
##INF=np.isinf(df)
#print(NAN)
#print(INF)
#print(np.isnan(df) | np.isinf(df)) # It is used for combine checking for both infinity and nan value in dataset
#df[np.isnan(df) | np.isinf(df)] = 0 # It is used for assigning the value to both nan  and infinity combinely 
#print(df)
#second_col=arr[:,2]==1
#NO=arr[second_col,:]
#df1=pd.DataFrame(NO)
##fifth_col=arr[:,5]>50
#AVG=arr[fifth_col,:]
#df2=pd.DataFrame(AVG)
#print(df1)
#print(df2)
#second_col=(arr[:,1]>2015) and (arr[:,1]<=2023)
#fifth_col=arr[:,5]>50
#AVG=arr[fifth_col,:]
#df1=pd.DataFrame(AVG)

#print(df1)
#x1=arr[:,0]
#x2=arr[:,5]
#plt.scatter(x1,x2,s=10,c='blue')
#plt.hist(x1,weights=x2,bins=5)
#plt.xticks(x1)
#plt.yticks(x2)
#plt.show()
#file_path="C:\\Users\\PMLS\\Downloads\\Virat_kohli.csv"
#read_csv=np.genfromtxt(file_path,delimiter=",",dtype="object")
#df=pd.DataFrame(read_csv)
#eight_col=read_csv[:,8]=90
#SR=read_csv[eight_col,:]
#df1=pd.DataFrame(SR)
#print(df1)