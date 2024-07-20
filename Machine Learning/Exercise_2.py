import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn import linear_model

def Life_Prediction():

         Temp_In_C=np.array([[10,20,30,
                     40,50,60,
                     70,80,90]]).reshape(-1,1)
         No_hours_Life=np.array([[420,365,285
                         ,220,176,117,
                         69,34,5]]).reshape(-1,1)
         Model=linear_model.LinearRegression()
         plt.xlabel("Tempertaure in Celsius")
         plt.ylabel("Life Time in Hours")
         plt.scatter(Temp_In_C,No_hours_Life,color='blue')
         fig=plt.subplot()
         fig.patch.set_facecolor('black')
         plt.grid()
         plt.show()
         Model.fit(Temp_In_C,No_hours_Life)
         Q1=Model.predict(np.array([[15]]).reshape(-1,1))
         print("People That will stay alive at 15 degree Celsius:",Q1)

def Electricity_Usuage():
        Month=np.array([['January','February','March','April','May','June','July','August','September','October','November','December']]).reshape(-1,1)
        Production=np.array([[4.51,3.58,4.31,5.06,5.64,4.99,5.29,5.83,4.70,5.61,4.90,4.20]]).reshape(-1,1)
        Electricity_Usuage=np.array([2.48,2.26,2.47,2.77,2.99,3.05,3.18,3.46,3.03,3.26,2.67,2.53]).reshape(-1,1)
        
        fig=plt.subplot()
        fig.set_facecolor('black')
        Model=linear_model.LinearRegression()
        Model.fit(Production,Electricity_Usuage)
        Q2=Model.predict(np.array([[5.91]]))
        plt.xlabel("Production")
        plt.ylabel("Electricity Usuage")
        plt.grid()
        plt.scatter(Production,Electricity_Usuage,color='red',marker='*')
        plt.plot(Production,Model.predict(Production),color='blue',linewidth=4)
        print("Amount of Electricity used in $5.67 Million: ",Q2)
        plt.show()



Electricity_Usuage()
#Life_Prediction()