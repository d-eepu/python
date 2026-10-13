# Write a program to calculate grades using a student's score.

score=int(input("Enter your score: "))
if score>=90:
    print("Grade: A")
elif score>=80: 
    print("Grade: B")
elif score>=70:
    print("Grade: C")
elif score>=60:
    print("Grade: D")
elif score>=50:
    print("Grade: E")
else:
    print("Grade: F")