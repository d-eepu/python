# Find common elements between two lists using sets.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common=set(list1) & set(list2)
print(common)

# Find elements that exist in the first set but not in the second.
diff=set(list1) - set(list2)
print(diff)

removedup =set(list1) | set(list2)
print(removedup)