#Show First and Last elements in list
USER_INPUT = input("Enter a list of numbers, separated by spaces: ")
INDEX = [int(i) for i in USER_INPUT.split()]
print(f"Your first number in list: {INDEX[0]} and the last number in list: {INDEX[-1]}")