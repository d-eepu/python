import pandas as pd;

# data={1:"absf",2:"bcd",3:"cde",4:"def"};

# series=pd.Series(data);
# series.loc[2]="updatd"
# print(series.loc[2])


data={
    "name":["abc","bcd","cde","def"],
    "age":[20,30,40,50],
}
df=pd.DataFrame(data);
# //new column
df["job"]=["cashier","n/a","engineer","manager"]
# new row
newrow=pd.DataFrame({"name":["xyz"],"age":[60],"job":["n/a"]})
df=pd.concat([df,newrow],ignore_index=True)
print(df)