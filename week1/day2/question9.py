# Create a dictionary of student names and marks. Find the student with the highest marks.

students={
    "deepa":90,
    "jyothi":80,
    "sowmya":95,    
    "prashu":9,
    "abcd":34
}


print(max(students,key=students.get))