# Asking user to input A
a = input("Pleas type a number (A): ")

# Doing some basic checks, trying to convert input to float type, and if unsuccessful asking for input again
while True:
    try:
        a = float(a)
        break
    except ValueError:
        print("Can not be word or zero or negative:")
        a = input("Pleas type a number (A): ")

if a <= 0:
    print('(A) can not be zero or negative,  please try again.')
    exit()
# Asking user to input X
x = input("Pleas type a number (X): ")

# Doing some basic checks, trying to convert input to float type, and if unsuccessful asking for input again
while True:
    try:
        x = float(x)
        break
    except ValueError:
        print("Can not be word or zero or negative:")
        x = input("Pleas type a number (X): ")

if x <= 0:
    print('(X) can not be zero or negative,  please try again.')
    exit()

# creating variables i, i2 , i3 used later in while loops to calculate results
# also creating empty lists for results, where the calculated results will be appended to these lists accordingly
i = 1
i2 = 1
i3 = 1
results = []
results2 = []
results3 = []

# Calculating first results using while loop and the print the list that has all the results
while a*i <= x:
    results.append(round((a * i), 3))
    i += 1

print('\n')
print("For A = " + str(a), "and X = " + str(x), "there were", len(results), "result(s):")
print(results)

# Calculating second results using while loop and the print the list that has all the results
while (a+1)*i2 <= 2*x:
    results2.append(round(((a+1)*i2), 3))
    i2 += 1
# print("\n")
print("For A+1 =", round((a+1), 3), "and 2X = " + str(2*x), "there were", len(results2), "result(s):")
print(results2)

# Calculating third results using while loop and the print the list that has all the results
while (a+2)*i3 <= 3*x:
    results3.append(round(((a+2)*i3), 3))
    i3 += 1
print("For A+2 =", round((a+2), 3), "and 3X = " + str(3*x), "there were", len(results3), "result(s):")
print(results3)
