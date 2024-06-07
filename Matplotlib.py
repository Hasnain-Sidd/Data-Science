import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def Line_Plot(path):
    df=pd.read_csv(path)
    teams=df["Opponents"]
    Avg=df["Avg"]
    Strike_rate=df['SR']
    Matches=df["Matches"]
    df.fillna(0,inplace=True)
    plt.xticks(fontsize=12,rotation=45)
    plt.subplots_adjust(bottom=0.3)
    plt.xlabel("Opponents")
    plt.ylabel("Averages/ Strike Rates")
    plt.title("Virat Kohli ODI Averages/ ODI Strike Rates")
    plt.plot(teams,Avg,label="Avg",color='Blue',marker=".")
    plt.plot(teams,Strike_rate,label="SR",color='red',marker="*")
    plt.plot(teams,Matches,label="Matches",color='black',marker="+")
    plt.legend(loc="best",shadow=True)
    plt.grid()
    plt.show()

def Match_Scorcard():
      Ind=np.array([7,10,26,31,144,158,np.nan,np.nan])
      Pak=np.array([1,15,91,96,98,115,120,151])
      Overs=np.array([2,4,6,10,12,14,16,20])
      fig, ax = plt.subplots()
      ax.set_xlabel("Overs",color='white')
      ax.set_ylabel("Runs",color="white")
      ax.set_title("Pak vs Ind ",color="white")
      ax.tick_params(axis='x', colors='white') 
      ax.tick_params(axis='y', colors='white')
      plt.plot(Overs,Ind,label="Ind",color='blue',marker=".")
      plt.plot(Overs,Pak,label="Pak",color="green",marker=".")
      plt.legend(loc="best",shadow=True)
      fig.patch.set_facecolor('black')  
      ax.set_facecolor('lightyellow') 
      plt.grid()
      plt.subplots_adjust(bottom=0.2)
      plt.show()
def Bar_Graph(path):
     df=pd.read_csv(path)
     df.fillna(0,inplace=True)
     Teams=np.arange(len(df["Opponents"]))
     Runs=df["Runs"]
     Strike_Rate=df["SR"]
     Avg=df["Avg"]
     
     fig, ax = plt.subplots()
     ax.set_xlabel("Opponents")
     ax.set_ylabel("Avg/SR")
     ax.set_title("Virat Kohli ODI AVG/SR")
     ax.set_xticks(Teams)
     ax.set_xticklabels(df["Opponents"],fontsize=10,rotation=45)
     fig.patch.set_facecolor('gray')  
     ax.set_facecolor('lightyellow') 
     ax.bar(Teams-0.2,Strike_Rate,color='blue',width=0.4,label="SR")
     ax.bar(Teams+0.2,Avg,color='orange',width=0.4,label="Avg")
     plt.legend(loc='best',shadow=True)
     plt.subplots_adjust(bottom=0.3)
     plt.grid()
     plt.show()
def Histogram(arr):
     arr2=np.array([2,8,18,13,7,1,1])
     arr3=np.arange(len(arr2))
     plt.yticks(arr3,arr2)
     plt.hist(arr,color='green',rwidth=0.95,bins=8,)
     plt.xlabel("Values")
     plt.ylabel("Frequency")
     plt.title("Stats Problem")
     plt.show()
def Pie_Charts(path):
      df=pd.read_csv(path)
      df.dropna(inplace=True)
      Runs=df["Runs"]
      Opponents=df["Opponents"]
      plt.pie(Runs,labels=Opponents,radius=3,autopct="%0.2f%%")
      plt.bar_label(fontsize=12)
      plt.axis("equal")
      plt.show()



path="C:\\Users\\PMLS\\Desktop\\Virat_Kohli.csv"
#Line_Plot(path=path)
Pie_Charts(path=path)
#Match_Scorcard()
#Bar_Graph(path=path)
#arr=np.array([99.5,104.5,109.5,114.5,119.5,124.5,129.5,134.5])
#Histogram(arr=arr)