#creating tuple
# models = ("Python", "Machine Learning","Deep Learning","Generative AI")
# print(models[0])
# print(models[-1])
# print(len(models))

# models = ("Linear Regression", "Logistic Regression", "Decision Tree", "Random Forest")
# print(models[1])
# print(models[3])
# print(models[1])
# print(models[-1])

# models = ("Linear Regression", "Logistic Regression", "Decision Tree")

# models[1] = "Random Forest"

# print(models)

# models = {"Python", "Python", "Machine Learning", "Deep Learning", "Machine Learning"}

# print(models)

# skills = ["Python", "SQL", "Python", "Excel", "SQL", "Python", "Power BI"]
# unique_skills = set(skills)
# for un in unique_skills:
#     print(un)
# print(len(unique_skills))

# skills = {"Python", "SQL", "Excel", "Power BI"}
# print("Python" in skills)
# print("Java" in skills)

# python_skills = {"Python", "Pandas", "NumPy"}
# ml_skills = {"Scikit-learn", "PyTorch", "Python"}
# print(len(python_skills | ml_skills))


# python_skills = {"Python", "Pandas", "NumPy"}
# ml_skills = {"Scikit-learn", "PyTorch", "Python"}
# print(python_skills & ml_skills)
#Skills in python_skills but not in ml_skills.
# python_skills = {"Python", "Pandas", "NumPy"}
# ml_skills = {"Scikit-learn", "PyTorch", "Python"}
# print(python_skills - ml_skills)

# project_1 = {"Python", "Pandas", "NumPy", "SQL", "Matplotlib"}
# project_2 = {"Python", "Pandas", "Scikit-learn", "SQL", "FastAPI"}
# # Skills used in both projects
# print(project_1 & project_2)
# # Skills used only in Project 1
# print(project_1 - project_2)
# # Skills used only in Project 2
# print(project_2 - project_1)
# # All unique skills across both projects
# print(project_1 | project_2)
# a = len(project_1 | project_2)
# print(a)

# student = {
#     "name": "Yasir khan", "degree":"computer engineering", "field":"AI/ML", "experience":1.5
# }
# student["city"] = "islamabad"
# student["field"] = "AI/ML Engineer"

# print(student["name"])
# print(student['degree'])
# print(student["field"])
# print(student["experience"])
# print(student["city"])

# student = {
#     "name": "Yasir Khan",
#     "degree": "Computer Engineering",
#     "field": "AI/ML Engineer",
#     "experience": 1.5,
#     "city": "Islamabad"
# }
# print("Salary" in student)
model = {
    "name": "Random Forest",
    "type": "Classification",
    "accuracy": 0.92,
    "status": "Trained"
}
print(model["name"])
print(model["accuracy"])

for key,value in model.items():
    print(key,value)
print("accuracy" in model)

print("loss" in model)
if "loss" in model:
    print("loss exists")
else: print("loss does not exists")
