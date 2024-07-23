import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
 
def Count_Plot():
     path="C:\\Users\\PMLS\\Desktop\\Linear-Regression-and-Logistic-Regression-in-Python\\Data Files\\Linear Regression\\House_Price.csv"
     df=pd.read_csv(path)
     Mean=df['n_hos_beds'].mean()
     df['n_hos_beds'].fillna(Mean,inplace=True)
     df['waterbody'].fillna('River',inplace=True)
     ax=sns.countplot(data=df,x=df['waterbody'],palette=['blue','lightblue','green'],width=0.3)
     for bars in ax.containers:
       ax.bar_label(bars)
     ax.legend(labels=['River','Lake','Lake and River'],shadow=True)
     ax.set_facecolor('gray')
     plt.show()
def Scatter():
     path="C:\\Users\\PMLS\\Desktop\\Linear-Regression-and-Logistic-Regression-in-Python\\Data Files\\Linear Regression\\House_Price.csv"
     df=pd.read_csv(path)
     df['crime_rate']=np.log(1+df['crime_rate'])
     plt.scatter(df['crime_rate'],df['price'],color='blue')
     #plt.plot(df['crime_rate'],df['price'],color='red')
     plt.xlabel("Crime Rate")
     plt.ylabel('Price')
     plt.title("Crime Rate V/s Price")
     fig=plt.subplot()
     fig.patch.set_facecolor('black')
     plt.grid()
     df['Avg_Dist']=(df['dist1']+df['dist2']+df['dist3']+df['dist4'])/4
     
     df=df.drop(['dist1'],axis=1)
     df=df.drop(['dist2'],axis=1)
     df=df.drop(['dist3'],axis=1)
     df=df.drop(['dist4'],axis=1)
     df=df.drop(['bus_ter'],axis=1)
     print(df.head())
     plt.show()
def Bar():
    path="C:\\Users\\PMLS\\Desktop\\Linear-Regression-and-Logistic-Regression-in-Python\\Data Files\\Linear Regression\\House_Price.csv"
    df=pd.read_csv(path)
    Mean=df['n_hos_beds'].mean()
    df['n_hos_beds'].fillna(Mean,inplace=True)
    df['waterbody'].fillna('River',inplace=True)
    Mean=df['n_hot_rooms'].mean()
    print(Mean)
    df.loc[df['n_hot_rooms'] > 50, 'n_hot_rooms'] = Mean
    df['Avg_Dist']=(df['dist1']+df['dist2']+df['dist3']+df['dist4'])/4
    df=df.drop(['dist1'],axis=1)
    df=df.drop(['dist2'],axis=1)
    df=df.drop(['dist3'],axis=1)
    df=df.drop(['dist4'],axis=1)
    df=df.drop(['bus_ter'],axis=1)
        
    
    

    plt.xlabel("Rooms Numbers")
    plt.ylabel("Price")
    plt.title("Rooms vs Price")
    plt.grid(axis='y', linestyle='-', linewidth=0.7, color='white')  # Only horizontal lines
    plt.grid(axis='x', linestyle=' ', linewidth=0)
    fig=plt.subplot()
    fig.patch.set_facecolor('black')
    df=pd.get_dummies(df)
    
    df=df.drop(['airport_NO'],axis=1)
    df=df.drop(['waterbody_Lake and River'],axis=1)
    #print(df.head())
   # print(df.corr())
    df=df.drop(['parks'],axis=1)
    model=linear_model.LinearRegression()
    model.fit(df[['room_num']],df['price'])
    plt.scatter(df['room_num'],df['price'],color='red')
    
    plt.plot(df['room_num'],model.predict(df[['room_num']]),color='blue',linewidth=4)
    #print(df.head())
    #print(df.corr())
    plt.show()
#Scatter()
Bar()