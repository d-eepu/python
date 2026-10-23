# 6. Convert two lists into a dictionary.
keys = ["name", "age", "city"]
values = ["deepa", 20, "bangalore"]
my_dict = dict(zip(keys, values))
print(my_dict)
# or
my_dict1={
    keys[0]:values[0],
    keys[1]:values[1],  
    keys[2]:values[2]
}
print(my_dict1)