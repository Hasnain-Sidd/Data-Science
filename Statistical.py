import numpy as np
import pandas as pd
class DataSet:
    def read_dataset(path):
            dtype=np.dtype([("Opponents",np.unicode_, 16)
                            ,("Span",np.unicode_, 16),
                            ("Matches",np.float64),
                            ("Inns",np.int32),
                            ("NO",np.int32),
                            ("Runs",np.int32),
                            ("HS",np.int32),
                            ("Avg",np.float64),
                            ("BF",np.float64),
                            ("SR",np.float64),
                            ("100s",np.int32),
                            ("50s",np.int32),
                            ("0s",np.int32),
                            ("4s",np.int32),
                            ("6s",np.int32)])
            file=np.genfromtxt(path,delimiter=",",dtype=dtype,skip_header=1)
            arr2=np.array(file,ndmin=2)
            #arr2.reshape(14,14)
            df=pd.DataFrame(file)
            NAN=pd.isna(df)
            df[pd.isna(df)]=0
            df.replace(-1,0,inplace=True)
            Opp=arr2[:,:]
            #print(Opp)
            print(arr2.shape)
            #print(arr2)
            #print(df)
            #print(arr2.size)
            max=np.max(df["Avg"])
            print(df["Opponents"]," ",df["Avg"])
            
            

path="C:\\Users\\PMLS\\Desktop\\Virat_Kohli.csv"
DataSet.read_dataset(path=path)