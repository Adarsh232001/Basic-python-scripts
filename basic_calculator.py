print('*******************CALCULATOR********************')
print('Select the below operations to perform')
print('1.Addition')
print('2.Subtraction')
print('3.Multyplication')
print('4.Division')
n = int(input('Enter a valid option'))
if (n <= 4):
    print('Enter the first operand')
    a = int(input())
    print('Enter the second operend')
    b = int(input())
    if (n == 1):
        print('Performing addition')
        result = int(a + b)
    elif (n == 2):
        print('Performing subtraction')
        result = int(a - b)
    elif (n == 3):
        print('Performing multyplication')
        result = int(a * b)
    elif (n == 4):
        print('Performing Division')
        result = int(a / b)
else:
    print('Enter a valid choice')

print('The result is ')
print(result)