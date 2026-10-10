import matplotlib.pyplot as plt

students = ["Ali", "Sara", "Ahmed", "Ayesha"]
marks = [78, 90, 65, 82, 83]
# Histogram: Distribution of student marks

plt.figure()
plt.hist(marks, bins=5, edgecolor="black")

plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()
# bars = plt.bar(students,marks)
# plt.bar_label(bars, padding=2)

# plt.title("Student Marks")
# plt.xlabel("Students")
# plt.ylabel("Marks")

# plt.show()

# months = ["Jan", "Feb", "Mar", "Apr"]
# sales = [120, 150, 135, 180]

# plt.figure()

# plt.plot(months, sales, marker="o")

# plt.title("Monthly Sales")
# plt.xlabel("Month")
# plt.ylabel("Sales")

# plt.show()
# months = ["Jan", "Feb", "Mar", "Apr"]
# sales = [120, 150, 135, 180]

# plt.figure()
# plt.plot(months, sales, marker="o")

# # Display value above each marker
# for month, sale in zip(months, sales):
#     plt.annotate(
#         str(sale),
#         (month, sale),
#         textcoords="offset points",
#         xytext=(0, 8),
#         ha="center"
#     )

# plt.title("Monthly Sales")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.show()