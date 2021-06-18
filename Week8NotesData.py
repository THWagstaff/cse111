# to read a csv pandas.read_csv("File Path")
import pandas as pd

df = pd.read_csv("filename.csv")

filtered_data = df[df["col_name"] > "Condition/Threshold"]
    #This returns the whole data set, filtered out
filteredcolumn = filtered_data["column"]
    #This returns just the column of the filtered dataset

print(df.dtypes)
    #This print function gives the data type of each column
#df = dataframe
#df = datatype

print(df.describe())
    #This function returns statistical measures from the data
