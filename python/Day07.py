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