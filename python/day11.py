import numpy as np

students = np.array([
    [78, 85, 92, 88],
    [65, 72, 68, 75],
    [90, 95, 93, 97],
    [55, 60, 58, 62],
    [82, 79, 85, 80]
])

# print("Marks greater than 90: ",students [students>90])
# print("Marks less than 70: ", students[students<70])
# marks_greater_than80 = students[students>80]
# print(len(marks_greater_than80))
# student_avg = np.mean(students, axis=1)
# print("students average: ",student_avg)
# student_avg_greaterthan80 = student_avg[student_avg>80]
# print(len(student_avg_greaterthan80))
# print(np.where(student_avg>80))
student_avg = np.mean(students,axis=1)
student_number = np.where(student_avg>80)[0]+1
print(student_avg)
print(student_number)
for sn in student_number:
    print(f"student{sn}: {student_avg[sn-1]}")