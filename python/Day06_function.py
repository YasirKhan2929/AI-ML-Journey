# def intro():
#     print("My name is Yasir khan\n i am learning python \n my goal to become AI/ML engineer")

# intro()
# name = input("Enter your name: ")
# def greeting(name):
#     print(f"Hello {name}")

# greeting(name)

# def calculate_square(n):
#     return(n*n)
# result = calculate_square(5)
# print(result)

# def calculate_error(actual, prediction):
#     return(abs(actual-prediction))
# error = calculate_error(100,85)
# print(error)
# errors = [5, 10, 15, 20, 10]
# def analyze_errors(errors):
#     total = 0
#     for error in errors:
#         total = error + total
#     avg = total/len(errors)
#     return total,avg
# total,avg = analyze_errors(errors)
# print(total,avg)

# error <= 5       → "Excellent"
# error <= 10      → "Good"
# error <= 20      → "Acceptable"
# otherwise        → "Poor"
# def classify_error(error):
#     if error<=5:
#         return "Excellent"
#     elif error<=10:
#         return "Good"
#     elif error<=20:
#         return "Acceptable"
#     else: return "Poor"
# print(classify_error(3))
# print(classify_error(8))
# print(classify_error(15))
# print(classify_error(30))

# predictions = [95, 82, 70, 98, 60]
# actual = [100, 80, 75, 100, 50]

# def calculate_errors(predictions, actual):
#     errors = []
#     for i in range(len(predictions)):
#         error = abs(actual[i] - predictions[i])
#         errors.append(error)
#     return errors
# errors = calculate_errors(predictions, actual)
# print(errors)


# def calculate_accuracy(correct, total):
#     return correct/total
# print(calculate_accuracy(90, 100))
# print(calculate_accuracy(45, 50))

# errors = [5, 12, 3, 18, 7, 25]
 
# def get_good_errors(errors):
#     good_error = []
#     for error in errors:
#         if error <=10:
#             good_error.append(error)
#     return good_error
# print(get_good_errors(errors))

# actual_values = [100, 80, 75, 100]
# predictions = [95, 82, 70, 98]

# def calculate_error(actual, prediction):
#     return abs(actual - prediction)

# def all_errors(actual, prediction):
#     errors = []

#     for i in range(len(predictions)):
#         error = calculate_error(actual_values[i], predictions[i])
#         errors.append(error)
#     return errors

# result = all_errors(actual_values,predictions)
# print(result)

# def check_prediction(a):
#     if a<=10:
#         return "Good"

# print(check_prediction(14))
# print(check_prediction(9))

actual_value = [100, 80, 75, 100, 50]
predictions = [95, 82, 70, 98, 60]

def calculate_error(actual, prediction):
    return abs(actual - prediction)

def analyze_prediction(actual, prediction):
    errors = []
    for i in range(len(predictions)):
        error = calculate_error(actual[i],prediction[i])
        errors.append(error)
    total = 0
    for error in errors:
        total = total + error
        avg = total/len(errors)
    return errors,avg


result,avg = analyze_prediction(actual_value,predictions)
print("Errors: ", result)
print("average: ", avg)