import prediction_tools
actual = 100
prediction = 92

error = prediction_tools.calculate_error(actual, prediction)
result = prediction_tools.classify_error(error)

print(f"Actual: {actual}")
print(f"Prediction: {prediction}")
print(f"Error: {error}")
print(f"Result: {result}")