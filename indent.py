# import time, sys
# indent = 0 # How many spaces to indent.
# indentIncreasing = True # Whether the indentation is increasing or not.
#
#
# try:
#     while True: # The main program loop.
#         print(' ' * indent, end='')
#         print('********')
#         time.sleep(0.1) # Pause for 1/10 of a second.
#
#         if indentIncreasing:
#             # Increase the number of spaces:
#             indent = indent + 1
#             if indent == 20:
#                 # Change direction:
#                 indentIncreasing = False
#
#         else:
#             # Decrease the number of spaces:
#             indent = indent - 1
#             if indent == 0:
#                 # Change direction:
#                 indentIncreasing = True
# except KeyboardInterrupt:
#     sys.exit()


#function that prints if number is even the number //2 value
def collatz(num):
    try:
        num=int(num)
        if num%2 == 0:
            # print(num//2)
            return num//2

        else:
            # print(3*num+1)
            return 3*num+1


    except  TypeError:
        print('Invalid Input, Type Error.')

def repCollatz(num):
    while collatz(num) != 1:
        num = collatz(num)
        print(num)
print('Enter your number:', end=' ')
inNum = input()

repCollatz(inNum)
