import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from word2number import w2n
def Single_Variant():
     path="C:\\Users\\PMLS\\Downloads\\canada_per_capita_income.csv"
     df=pd.read_csv(path)
     plt.xlabel("Year")
     plt.ylabel("Per Capita Income($US)")
     plt.subplots_adjust(bottom=0.2)
     plt.title("Linear Model")
     plt.scatter(df["year"],df["per capita income (US$)"],color='green')
     Linear=linear_model.LinearRegression()
     X= df["year"].values.reshape(-1, 1)
     y = df["per capita income (US$)"].values
     Linear.fit(X,y)
     Predict=Linear.predict([[2024]])
     print(Predict)
     plt.scatter(df["year"],df["per capita income (US$)"],color='green')
     plt.plot(df['year'],Linear.predict(df[['year']]),color='blue', linewidth=4)
     coef=Linear.coef_
     Intercept=Linear.intercept_
     Capita_per_Year=coef*2024+Intercept
     print(Capita_per_Year)
     plt.show()

def Multi_Variant(path):
     df=pd.read_csv(path)
     
     Exp=df["experience"]
     def convert_word_number(Exp):
         try: 
           return w2n.word_to_num(Exp)
         except:
            return None
    
     df['experience']=df['experience'].apply(convert_word_number)
     df["experience"].fillna(0,inplace=True)
     Median=df["test_score(out of 10)"].median()
     df["test_score(out of 10)"].fillna(Median,inplace=True)
     Model=linear_model.LinearRegression()
     Model.fit(df[['experience','test_score(out of 10)','interview_score(out of 10)']],df['salary($)'])
     Q1=Model.predict([[2,9,6]])
     print("Salary of a person having 2 years experience, 9 test score and 6 interview score:",Q1)
     Q2=Model.predict([[12,10,10]])
     print("Salary of a person having 12 years experience, 10 test score and 10 interview score:",Q2)
   #print(df)
    
     

path="C:\\Users\\PMLS\\Downloads\\hiring.csv"
Multi_Variant(path=path)
#Single_Variant()