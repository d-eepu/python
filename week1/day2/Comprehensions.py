# Use list comprehension to create squares of numbers from 1 to 10.
squares = [x**2 for x in range(1, 11)]
print(squares)
# Use list comprehension to extract numbers greater than 10.
greaterthan10=[x for x in squares if x > 10]
print(greaterthan10)
# Use dictionary comprehension to map numbers from 1 to 5 to their squares.
squaredict={x:x**2 for x in range(1,6)}
print(squaredict)
# Use set comprehension to extract unique vowels from a string.
uniquevowels={x for x in "hello world" if x in "aeiou"}
print(uniquevowels)