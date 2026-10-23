# q8:Count how many times each character appears in a string.
string="hello world"
count={}
for w in string:
    if w in count:
        count[w]+=1
    else:
        count[w]=1


print(count)