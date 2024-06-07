import pandas as pd
def Read_CSV(path):
    df=pd.read_csv(path)
    df.fillna(1,inplace=True)# fill all NAN values in our data set with 0
    print(df[["Opponents","Runs"]])
    print(df[df["Avg"] >= 53][["Avg", "Opponents","Matches"]])
    print(df[df["Runs"]>=500][["Runs","Opponents","Avg"]])
    print(df[["Opponents","Matches","Avg"]])
    df.set_index("Avg",inplace=True)
    df.reset_index(inplace=True)
    print(df)
    print("Complete Statistical data of data frame:",df.describe())

def create_df(dict):
    df=pd.DataFrame(dict)
    print(df)
    print(df[1:4])

def ops_csv(path):
    df=pd.read_csv(path,nrows=5,na_values=[0])#--> na_values equals all values of zeroes to NAN values
    df.to_csv("Selective.csv",columns=["Opponents","Matches","Avg","SR"],index=False)
    print(df)

def Read_Excel(path):
    df=pd.read_excel(path, "Sheet1")
    df.replace('-',0,inplace=True)
    print(df)
def read_csv(path):
    df=pd.read_csv(path,parse_dates=["Span"])
    print(df[df["Span"]>2010 & df["Span"]<2019])
def Group_By(path):
    df=pd.read_excel(path)
    
    group_by=df.groupby(["City"])
    for Group_Name,Group_Data in group_by:
        print(Group_Name)
        print(Group_Data)
    
    
    #print(group_by.mean())
    Texas=group_by.get_group("Texas")
    print(Texas)        
     



path="C:\\Users\\PMLS\\Desktop\\Virat_Kohli.csv"
path1="C:\\Users\\PMLS\\Desktop\\Virat_kohli.xlsx"
path2="C:\\Users\\PMLS\\Desktop\\Ticket_Sales.xlsx"
#Read_CSV(path=path)
dict={"Name":["Babar Azam","Klaasen","Buttler","Virat","Rohit"],"Matches":[110,76,154,251,231],"Odi Avg":[56.87,49.91,44.32,54.32,48.98],
      "Strike Rate":[93.21,120.21,110.56,92.23,98.71],"HS":[158,174,143,183,264]}
#create_df(dict=dict)
#ops_csv(path=path)
#Read_Excel(path=path1)
#read_csv(path=path)
Group_By(path=path2)
