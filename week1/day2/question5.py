# Create a new list containing only even numbers from an existing list.
list1=[1,2,3,4,5,23,12,1,12,3,45,6,7,8,5,43,24]

# creating a new list odd

newList=list(filter(lambda x:x%2!=0,list1))
print(newList)
# even list
evenlist=list(filter(lambda x:x%2==0,list1))
print(evenlist)