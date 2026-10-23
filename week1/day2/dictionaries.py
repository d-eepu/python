# reate a dictionary containing a student's name, age, and marks. Print each value.

dict1={"name":"deepa","age":20,"company":"manocore"}
for key in dict1:
    print(key,dict1[key])

dict2=dict1.copy()
dict2["city"]="bangalore"
print(dict2)
