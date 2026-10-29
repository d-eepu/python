# Write a function that accepts two numbers and returns their sum.
def sumFunction(num1, num2):
    sum = num1 + num2
    print("The sum of", num1, "and", num2, "is:", sum)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# sumFunction(num1, num2)

# 2.Write a function that checks whether a number is even or odd.
def checkEvenOdd(num):
    if num%2==0:
        print(num,"is even number")
    else:
        print(num,"is odd number")
num=int(input("enter a number:"))
checkEvenOdd(num)