import numpy as np

# students = np.array([
#     [80, 75, 90],
#     [65, 70, 60],
#     [90, 85, 95],
#     [55, 60, 70]
# ])

# print("Students marks:")
# print(students)

# print("Shape:", students.shape)

# print("First student:", students[0])

# print("Math marks:", students[:, 0])

# print("Average of all marks:", np.mean(students))

# print("Average of each student:", np.mean(students, axis=1))

# print("Average of each subject:", np.mean(students, axis=0))

# print("Third student marks: ", students[2])
# print("Second subject marks: ", students[:,1])
# print("Highest marks in array: ", np.max(students))
# print("Lowest marks in array: ", np.min(students))
# print("Standard deviation of array: ", np.std(students))

import numpy as np

students = np.array([
    [78, 85, 92, 88],
    [65, 72, 68, 75],
    [90, 95, 93, 97],
    [55, 60, 58, 62],
    [82, 79, 85, 80]
])
print(students)
student_average = np.mean(students, axis=1)
print("Each student average: ",student_average)
sub_avg = np.mean(students, axis=0)
print(sub_avg)
best_avg_student = np.max(student_average)
print("Best student", best_avg_student)
max_student = np.argmax(students)
print("argmax: ",max_student)
print(students.size)
print(students.shape)
st_avg= np.mean(students, axis=1)
print("best student average",np.max(st_avg))
print("Best subjet average: ", np.max(sub_avg))
print("Highest mark: ", np.max(students))
print("Lowest marks: ", np.min(students))
print("overall average: ", np.mean(students))
print("Overall deviation of students: ", np.std(students))