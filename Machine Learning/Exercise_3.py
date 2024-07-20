import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split

path="C:\\Users\\PMLS\\Desktop\\Data_Sets\\carprices.csv"
df=pd.read_csv(path)

def Exercise_Question():
     df=pd.get_dummies(df)
     df=df.drop(['Car Model_Mercedez Benz C class'],axis='columns')
     Model=linear_model.LinearRegression()
     Model.fit(df[['Mileage','Age(yrs)','Car Model_Audi A5','Car Model_BMW X5']],df['Sell Price($)'])
     Q1=Model.predict([[45000,4,0,0]])
     print(Q1)
     Q2=Model.predict([[86000,7,0,1]])
     print(Q2)
     Q3=Model.score(df[['Mileage','Age(yrs)','Car Model_Audi A5','Car Model_BMW X5']],df['Sell Price($)'])
     print(Q3)
     plt.scatter(df['Sell Price($)'],df['Mileage'],color='red')
     plt.plot(df["Sell Price($)"],Model.predict(df[['Mileage','Age(yrs)','Car Model_Audi A5','Car Model_BMW X5']]),color='blue')
     plt.xlabel("Prices")
     plt.ylabel('Mileage')
     plt.legend(loc='best')
     plt.grid()
     fig=plt.subplot()
     fig.patch.set_facecolor('gray')

     plt.title("Car Prices")
     print(df)
     plt.show()

def Testing_Data():
     path="C:\\Users\\PMLS\\Desktop\\Data_Sets\\carprices.csv"
     df=pd.read_csv(path)
     df=df.drop(['Car Model'],axis='columns')
     print(df)
     X_train,X_test,Y_train,_Y_test=train_test_split(df[['Mileage','Age(yrs)']],df['Sell Price($)'],test_size=0.15,random_state=10)
     Model=linear_model.LinearRegression()
     print(Y_train)
     Model.fit(X_train,Y_train)
     print(_Y_test)
     Test=Model.predict(X_test)
     print(Test)
     Score=Model.score(df[['Mileage','Age(yrs)']],df['Sell Price($)'])
     print("Accuracy of our model is:",Score)


Testing_Data()
