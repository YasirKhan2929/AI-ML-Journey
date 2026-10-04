#Exercise 01
# age = int(input("Enter your age: "))
# if age>=18:
#     print("You are eligible")
# else: print("You are not eligible")
 
#Exercise 02
#  80 or above → Grade A
# 70–79 → Grade B
# 60–69 → Grade C
# 50–59 → Grade D
# Below 50 → Fail
# marks = int(input("Enter your mark to check grade: "))
# if marks>=80:
#     print("Grade A")
# elif (marks>=70 and marks<=79):
#     print("Grade B")
# elif (marks>=60 and marks<=69):
#     print("Grade C")
# elif (marks>=50 and marks<=59):
#     print("Grade D")
# else: print("fail")

# confidence >= 0.90 → "Very High Confidence"
# confidence >= 0.75 → "High Confidence"
# confidence >= 0.50 → "Medium Confidence"
# Below 0.50 → "Low Confidence"
# confidence = float(input("enter model confidence number: "))
# if confidence>=0.90:
#     print("Very High Confidence")
# elif confidence>=0.75:
#     print("High Confidence")
# elif confidence>=0.5:
#     print("Medium Confidence")
# else:
#     print("Low confidence")
# ============================================================
print("DAY 2 - MINI PROJECT: AI PREDICTION DECISION SYSTEM")
# ============================================================
#
# Create a Python program that:
#
# 1. Asks the user for their name.
name = input("Enter your name: ")
# 2. Asks for the actual value.
actual_value = int(input("Enter your actual value: "))
# 3. Asks for the predicted value.
predicted_value = int(input("Enter predicted value: "))

# 4. Calculates the absolute error:
#       error = abs(actual - predicted)
error = abs(actual_value - predicted_value)
# 5. Uses if / elif / else to evaluate the prediction:
#
print(f"Your name: {name}")
#       Actual Value
print(f"actual value: {actual_value}")
#       Predicted Value
print(f"predicted value: {predicted_value}")
#       Absolute Error
print(f"Absolute error: {error}")

print("Result: ")
#       Error <= 5   → "Excellent Prediction"
if error<=5:
    print("Exellent Predication")
#       Error <= 10  → "Good Prediction"
elif error<=10:
    print("Good Pridication")
#       Error <= 20  → "Acceptable Prediction"
elif error<=20:
    print("Acceptable Prediction")
#       Error > 20   → "Poor Prediction"
else: print("Poor Prediction")
#
# 6. Finally, display:
#       Name

#       Result

# Example:
#
# Enter your name: Yasir
# Enter actual value: 100
# Enter predicted value: 92
#
# Absolute Error: 8
# Result: Good Prediction
#
# ============================================================