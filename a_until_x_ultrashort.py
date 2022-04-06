a, x = map(int, input("Please provide A and X separated by 'space', they MUST be >0: ").split())
print(f'A until X {list(range(a, x+1, a))},\nA+1 until 2X {list(range(a+1, (2*x)+1, a+1))},\nA+2 until 3X {list(range(a+2, (3*x)+1, a+2))}')

# in first line of this code we take input from user using just one line, so the inputs must be separated by 'space',
# then inputs are being converted into INT type
# in the second line of the code we print results which are lists, and the results are being calculated using
# range built-in function

# this code has been made to be as minimalistic as possible, so there were no checks introduced,
# I assume that user must follow instructions and provide int type as an input
# checks can be introduced in the form of .isdecimal or using try / except to try to convert input to required type
