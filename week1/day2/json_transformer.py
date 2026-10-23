import json

with open(r"C:\Users\jyoth\Downloads\deepa\python\week1\day2\users.json") as f:
    users = json.load(f)
print(users)
# Remove extra spaces from each user's name.