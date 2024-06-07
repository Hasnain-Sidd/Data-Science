import numpy as np
import pandas as pd
class Practice:
    def properties_of_numpy(Arr):
        print("Dimensions of Array:",Arr.ndim)
        print("Shape of an array:",Arr.shape)
        print("Type of Data stored in an array:",Arr.dtype)
        print("Size of an array:",Arr.size)
    def Calculation_of_array(Arr):
        print("Maximun value of an array:",np.max(Arr))
        print("Minimum value of an array:",np.min(Arr))
        print("Mean of an array:",np.mean(Arr))
        print("Standard Deviation of an array:",np.std(Arr))
        print("Total sum of a column:",Arr.sum(axis=0))
        print("Total sum of a row:",Arr.sum(axis=1))
    def Read_file(Path):
        file=np.genfromtxt(Path,skip_header=1)
        file_arr=np.array(file)
        df=pd.DataFrame(file_arr)
        #print("All rows with column 1\n:",df)
        NaN=np.isnan(file_arr[:,3]==False)
        Arr1=np.array(NaN)
        
        #print(NaN)



Arr=np.array([[4,5,2],[87,32,12],[90,56,71],[54,55,57]])
#Practice.properties_of_numpy(Arr=Arr)
#Practice.Calculation_of_array(Arr=Arr)
path="C:\\Users\\PMLS\\Documents\\Virat_Kohli.txt"
Practice.Read_file(Path=path)
