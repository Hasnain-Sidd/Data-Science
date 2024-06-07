import pandas as pd 
import numpy as np 
from sklearn import linear_model
import matplotlib.pyplot as plt


def Read_Excel(path):
    df=pd.read_csv(path)
    player=df.groupby(df["Player"])
    #for player_name,player_data in player:
          #print(player_name)
          #print(player_data)
    YuV=player.get_group('Yuvraj Singh')
    YV_SR=YuV['SR'].mean()
    VR=player.get_group('Virender Sehwag')
    VR_SR=VR['SR'].mean()
    VK=player.get_group('Virat Kohli')
    VK_SR=VK["SR"].mean()
    SuR=player.get_group('Suresh Raina')
    SuR_SR=SuR["SR"].mean()
    SN=player.get_group("Sunil Narine")
    SN_SR=SN["SR"].mean()
    SW=player.get_group("Shane Watson")
    SW_SR=SW["SR"].mean()
    RS=player.get_group("Rohit Sharma")
    RS_SR=RS["SR"].mean()
    
    plt.xlabel("Players")
    plt.ylabel("Strike Rate")
    plt.title("Ipl Career Strike Rate")
    plt.bar(YuV['Player'],YV_SR,color='red',width=0.5,label='Yuvraj Singh')
    plt.bar(VR['Player'],VR_SR,color='blue',width=0.5,label='virender Sehwag')
    plt.bar(VK['Player'],VK_SR,color='orange',width=0.5,label='Virat Kohli')
    plt.bar(SuR['Player'],SuR_SR,color='gray',width=0.5,label='Suresh Raina')
    plt.bar(SN['Player'],SN_SR,color='yellow',width=0.5,label='Sunil Narine')
    plt.bar(SW['Player'],SW_SR,color='purple',width=0.5,label='Shane Watson')
    plt.bar(RS['Player'],RS_SR,color='maroon',width=0.5,label='Rohit Sharma')
    plt.col
    plt.subplots_adjust(bottom=0.2)
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),shadow=True)
    plt.show()

def Most_Runs(path):
    df=pd.read_csv(path)
    Player_name=df.groupby(['Player'])
    #for Player,Player_Data in Player_name:
     #   print(Player)
      #  print(Player_Data)
    RS=Player_name.get_group("Rohit Sharma")
    RS_Runs=RS['Runs'].sum()
    VK=Player_name.get_group("Virat Kohli")
    VK_Runs=VK["Runs"].sum()
    SKY=Player_name.get_group("Suryakumar Yadav")
    SKY_Runs=SKY['Runs'].sum()
    SS=Player_name.get_group("Steve Smith")
    SS_Runs=SS['Runs'].sum()
    SI=Player_name.get_group("Shreyas Iyer")
    SI_Runs=SI['Runs'].sum()
    RP=Player_name.get_group('Rishabh Pant')
    RP_Runs=RP['Runs']
    AB=Player_name.get_group('AB de Villiers')
    AB_Runs=AB['Runs']
    DW=Player_name.get_group("David Warner")
    fig=plt.subplot()
    fig.patch.set_facecolor('red')
    DW_Runs=DW['Runs']
    plt.xlabel("Runs")
    plt.ylabel("Player")
    plt.title("Ipl Career Runs")
    color={'blue'}
    plt.barh(RS['Player'],RS_Runs,color=color)
    plt.barh(VK['Player'],VK_Runs)
    plt.barh(SKY['Player'],SKY_Runs,color=color)
    plt.barh(SS['Player'],SS_Runs,color=color)
    plt.barh(SI['Player'],SI_Runs,color=color)
    plt.barh(RP['Player'],RP_Runs,color=color)
    plt.barh(AB['Player'],AB_Runs,color=color)
    plt.barh(DW['Player'],DW_Runs,color=color)
    plt.show()
    


    




path1="C:\\Users\\PMLS\\Downloads\\archive\\IPL - Player Performance Dataset\\All Seasons Combined\\Most Runs All Seasons Combine.csv"
path="C:\\Users\\PMLS\\Downloads\\archive\\IPL - Player Performance Dataset\\All Seasons Combined\\Most Runs Per Over All Seasons Combine.csv"
#Read_Excel(path=path)
Most_Runs(path=path1)
