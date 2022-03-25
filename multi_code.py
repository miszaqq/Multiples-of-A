from math import *

# asking for input from user
ask_for_A = "Please type first number (A): "
first_number = input(ask_for_A)

while first_number.isdecimal() != True or int(first_number) == 0:
    print("Number A can not be 0 or negative and must be typed as digit.")
    first_number = input(ask_for_A)

ask_for_X = "Please type second number (X): "
second_number = input(ask_for_X)

while second_number.isnumeric() != True or int(second_number) == 0:
    print("Number X can not be 0 or negative and must be typed as digit.")
    second_number = input(ask_for_X)

# convert inputs from str to int, and create variables for A+1, A+2, 2X and 3X, create separator line
a = int(first_number)
a_plus1 = a + 1
a_plus2 = a + 2
x = int(second_number)
x_times2 = 2 * x
x_times3 = 3 * x

separator_line = "\n--------------------\n"

# Text line before first set of number(s) being printed
print("\nMultiples of A (" + str(a) + ") until X (" + str(x) + "):")

# variable y used for range in the for loop
y = (x / a)

if (x % a) < 1:
    y = (ceil(y) + 1)
else:
    y = (ceil(y))

# for loop to print multiples of A until X
for i in range(1, y):
    print(i * a)

print("\nThere were " + str(y-1) + " result(s)!")

# print empty lines and separator between first and second part
print(separator_line + "Multiples of A+1 (" + str(a_plus1) + ") until 2X (" + str(x_times2) + "):")

# variable y2 used for range in the second for loop
y2 = (x_times2 / a_plus1)

if (x_times2 % a_plus1) == 0:
    y2 = (ceil(y2) + 1)
else:
    y2 = (ceil(y2))

# for loop to print multiples of A+1 until 2X
for i in range(1, y2):
    print(i * a_plus1)

print("\nThere were " + str(y2-1) + " result(s)!")


# print empty lines and separator between second and third part
print(separator_line + "Multiples of A+2 (" + str(a_plus2) + ") until 3X (" + str(x_times3) + "):")

# variable y3 used for range in the second for loop
y3 = (x_times3 / a_plus2)

if (x_times3 % a_plus2) == 0:
    y3 = (ceil(y3) + 1)
else:
    y3 = (ceil(y3))

# for loop to print multiples of A+2 until 3X
for i in range(1, y3):
    print(i * a_plus2)

print("\nThere were " + str(y3-1) + " result(s)!")
