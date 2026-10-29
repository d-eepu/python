import pandas as pd;

data=pd.read_csv("data.csv",index_col="Name");
legendary=data[data["Legendary"]==True]
print(legendary)




# data cleaning

#1. removing legendary column
df=data.drop(columns=["Legendary","Weight"])
#2. handling missing values
# df=df.dropna(subset="Type2")
df=df.fillna({"Type2": "None"})
# 3.fix inconsistance values
df["Type1"]=df["Type1"].replace({"Grass":"GRASS"})
# 4.standardizing text
df["Type1"]=df["Type1"].str.lower()
# 5.remving duplicates
df=df.drop_duplicates()
print(df.to_string())