# Given the names and grades for each student in a class of  students,
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade,
# order their names alphabetically and print each name on a new line.

import math

student_marks = {'Krishna': [67.0, 68.0, 69.0], 'Arjun': [70.0, 98.0, 63.0], 'Malika': [52.0, 56.0, 60.0]}

print("student",student_marks)

def getavg(student_marks,key):
    get_marks = student_marks.get(key)
    total_marks=0
    for marks in range(len(get_marks)):
        total_marks += get_marks[marks]
        avg_mark = total_marks/len(get_marks)
    return format(avg_mark,".2f")

print(getavg(student_marks,"Krishna"))