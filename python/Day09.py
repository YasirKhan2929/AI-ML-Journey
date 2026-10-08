# import numpy as np
# print(np.__version__)

# import numpy as np

# numbers = np.array([10, 20, 30, 40, 50])

# print(numbers)

#difference between numpy and python list
# numbers = [10, 20, 30]
# print("arrey multiplication from python")
# print(numbers * 2)
# now try for numpy
import numpy as np
# number= np.array([10, 20, 30])
# print("Array operations numpy")
# print(number * 2)
# print(number + 2)
# print(number - 2)
# print(number / 2)
# mydata = np.array([10, 20, 30, 40, 50])

# print(mydata)
# print(mydata.ndim)
# print(mydata.shape)
# print(mydata.size)
# print(mydata.dtype)

# errors = np.array([5, 12, 3, 18, 7])
# print(errors +5)
# print(errors * 2)
# print(errors - 2)
# avg = np.mean(errors)
# print(avg)

# scores = np.array([85, 90, 72, 95, 88, 76])
# first_score = scores[0]
# lastScore = scores[-1]
# thirdScore = scores[2]
# FirstThreeScore = scores[0:3]
# lastthreescore = scores[-3:]
# indexonetofour = scores[1:5]
# print(first_score)
# print(lastScore)
# print(thirdScore)
# print(FirstThreeScore)
# print(lastthreescore)
# print(indexonetofour)

# errors = np.array([5, 12, 3, 18, 7, 25, 2, 15])
# good_error= errors[errors<10]
# high_error = errors[errors>10]
# print(good_error)
# print(high_error)
errors = np.array([5, 12, 3, 18, 7, 25, 2, 15])
avg = np.mean(errors)
print(avg)
minimum = np.min(errors)
print(minimum)
maximum = np.max(errors)
print(maximum)
total = np.sum(errors)
print(total)
std = np.std(errors)
print(std)