import numpy as np
from sklearn import linear_model
import pandas as pd
import math

def gradient_descent(x,y):
    path="C:\\Users\\PMLS\\Desktop\\Data_Sets\\test_scores.csv"
    df=pd.read_csv(path)
    m_curr=0
    b_curr=0
    iterations=500
    n=len(x)
    learning_rate=0.0001
    for i in range(iterations):
        
         y_predicted=m_curr * x + b_curr
         cost=(1/n) * sum((y-y_predicted)**2)
         md=-(2/n)*sum((x*(y-y_predicted)))
         bd=-(2/n)*sum(y-y_predicted)
         m_curr=m_curr - learning_rate *md
         b_curr=b_curr - learning_rate *bd
         print("m {}, b {}, cost {}, iterations {}".format(m_curr,b_curr,cost,i))
         if i > 0 and abs(prev_cost - cost) < 1e-6:
            print(f"Stopping early at iteration {i+1} with cost {cost}")
            break
         prev_cost = cost

        

    

path="C:\\Users\\PMLS\\Desktop\\Data_Sets\\test_scores.csv"
df=pd.read_csv(path)
gradient_descent(df['math'],df['cs'])

# m 1.0445228751752675, b 0.01691985520723526, cost 31.81138094480272, iterations 99