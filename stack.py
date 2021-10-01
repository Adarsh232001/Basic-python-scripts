#In python list acts as stack
'''Basically stack performs the operation of FIFO (First In First Out)'''
stack = []
stack.append(0)
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
#Expected output is [0, 1, 2, 3]
stack.pop()
print(stack)
#Expected output is [0, 1, 2]
stack.pop()
print(stack)
#Expected output is [0, 1]