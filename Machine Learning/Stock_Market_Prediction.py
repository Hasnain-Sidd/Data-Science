import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import chart_studio.plotly as py
import plotly.graph_objs as  go
from plotly.offline import plot 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error as msc
from sklearn.metrics import r2_score as rs
from sklearn.linear_model import LinearRegression
def Stock_Prediction(path):
    df=pd.read_csv(path)
   
    
    df['Date']=pd.to_datetime(df['Date'])
    print(df.info())
    print( f"Stock Prices are in between: {df['Date'].min()} {df['Date'].max()}")
    print(f"Total Days: {(df['Date'].max()-df['Date'].min())}")
    df[['Open','High','Low','Close','Adj Close']].plot(kind='box')
    layout=go.Layout(title='Stock Prediction for Tesla Company',xaxis=dict( title='Date',titlefont=dict(family='Courier New, monospace',size=18,color='black' )),
        yaxis=dict(title='Price',titlefont=dict(family='Courier New, monospace', size=18,color='black' ))
    )
    tesla_data=[{'x':df['Date'],'y':df['Close']}]
    plot=go.Figure(data=tesla_data, layout=layout)
    X=np.array(df.index).reshape(-1,1)
    Y=df['Close']
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3,random_state=101)
    scalar=StandardScaler().fit(X_train)
    Model=LinearRegression()
    Model.fit(X_train,Y_train)
    trace0=go.Scatter(
        x=X_train.T[0],
        y=Y_train,
        mode='markers',
        name='Actual'
    )
    trace1=go.Scatter(
        x=X_train.T[0],
        y=Model.predict(X_train),
        mode='markers',
        name='Predicted'

    )
    Tesla_Data=[trace0,trace1]
    layout.xaxis.title.text= 'Day'
    plot2=go.Figure(data=Tesla_Data,layout=layout)
    Mean=msc(Y_test,Model.predict(X_test))
    R2C=rs(Y_test,Model.predict(X_test))
    Mean2=msc(Y_train,Model.predict(X_train))
    R2C2=rs(Y_train,Model.predict(X_train))
    print(Mean)
    print(R2C)
    print(Mean2)
    print(R2C2)
    
    plot.show()
    plot2.show()
    plt.show()


path="C:\\Users\\PMLS\\Desktop\\Data_Sets\\datasetsandcodefilesstockmarketprediction\\tesla.csv"
Stock_Prediction(path=path)
