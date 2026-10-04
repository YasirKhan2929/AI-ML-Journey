def calculate_error(actual, prediction):
    return abs(actual - prediction)


def classify_error(error):
    if error <= 5:
        return "Excellent"
    elif error <= 10:
        return "Good"
    elif error <= 20:
        return "Acceptable"
    else:
        return "Poor"