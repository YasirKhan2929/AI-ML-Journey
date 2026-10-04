# total = 0
# for i in range(1,11):
#     total = i+total
# print(total)

# for i in range(1, 21):
#     if i%2==0:
#         print(i)
# errors = [2, 8, 15, 4, 25, 7, 30]
# for error in errors:
#     if error<=10:
#         print("Good")
#     else: print("Need improvement")

# count = 5
# while count>0:
#     print(count)
#     count = count-1

errors = [3, 12, 7, 25, 5, 18, 2, 30, 50, 60, 2]
G_P = 0
N_I = 0
for error in errors:
    if error<=10:
        print(f"Error: {error} -> 'Good Pridiction'")
        G_P = G_P +1
    else: 
        print(f"Error: {error} -> 'Needs improvement'")
        N_I = N_I +1
print(f"Good pridiction: {G_P}")
print(f"Needs Improvement: {N_I}")