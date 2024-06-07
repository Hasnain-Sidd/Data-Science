import pandas as ps
import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")
#Cricketers={"Name":['Babar Azam','Virat Kohli','Joe Root','Heinrick Klaasen'],"Matches":[112,287,164,82]
  #          ,"Runs":[5432,11452,7654,4291],"ODI_AVG":[57.8,54.98,49.87,45.32]}
#df1=ps.DataFrame(Cricketers)
#Cricketers2={"Name":['Travis Head','Rohit Sharma','Steve Smith','Mohammad Rizwan'],"Matches":[112,287,164,82]
 #           ,"Runs":[5432,11452,7654,4291],"ODI_AVG":[57.8,54.98,49.87,45.32],"Strike_Rate":[121.3,102.4,89.76,93.81]}
#df2=ps.DataFrame(Cricketers2)
#print(df1)
#**************SLICING*********************
#two_rows=df1[:-2]
#last_rows=df1[-2:]
#print("Starting Two Rows after  slicing operations:")
#print(two_rows)
#print(df1.head(2))
#print("Last two Rows after Slicing operations:")
#print(last_rows)   both ways do the same thing
#print(df1.tail(2))
#*******************MERGING*******************
#print(df2)
#merge=ps.merge(df1,df2,on='ODI_AVG')
#print(merge)
#************************joining******************
#joined=df1.join(df2,lsuffix='_df1', rsuffix='_df2')
#print(joined)
#*************Changing the Index*******************
#df=ps.DataFrame({"Obtained Numbers":[92,78,91,89,73],"Percentage":[0.92,0.78,0.91,0.89,0.73]})
#df.set_index("Obtained Numbers",inplace=True)
#df1=df.rename(columns={"Percentage":"Total Percentage"})
#print("Data Frame before renaming")
#print(df)
#print("Data Frame after renaming")
#print(df1)
#df.plot()
#plt.show()
#********Concatenation************
#Cricketers={"Name":['Babar Azam','Virat Kohli','Joe Root','Heinrick Klaasen'],"Matches":[112,287,164,82]
 #           ,"Runs":[5432,11452,7654,4291],"ODI_AVG":[57.8,54.98,49.87,45.32],}
#df1=ps.DataFrame(Cricketers)
#Cricketers2={"Name":['Travis Head','Rohit Sharma','Steve Smith','Mohammad Rizwan'],"Matches":[112,287,164,82]
 #          ,"Runs":[5432,11452,7654,4291],"ODI_AVG":[57.8,54.98,49.87,45.32],"Strike_Rate":[121.3,102.4,89.76,93.81]}
#df2=ps.DataFrame(Cricketers2)
#Concate=ps.concat([df1,df2])
#print(Concate)
#*******Data Munging*********
df=ps.read_csv("C:\\Users\\PMLS\\Downloads\\cleaned.csv",index_col=0)
#df.to_html("Clean.html")

#df.to_excel("Clean.xlsx")
print(df.head(5))
df=df.set_index(["Product_Description"])
sd=df.reindex(columns=['Price','Screen_Size'])
db=sd.diff(axis=1)
db.plot(kind='bar')
plt.show()


