#---------Recursion------------
"""
def FUNCTION():
    "Call the function endlessly"
    print('Hello')
    print(FUNCTION())
FUNCTION()
"""


def FUNCTION2(x):
    """Call the function x times"""
    if x==0:
        return
    else:
        print('Hello')
        FUNCTION2(x-1)
FUNCTION2(5)


def SUM(x):
    """Sum of numbers in numerical order"""
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return x+SUM(x-1)
print(SUM(5))


def FACTORIAL(x):
    """Calculate factorial number"""
    if x==0:
        return 1
    else:
        return x*FACTORIAL(x-1)
USERNUMBER=input("Enter your number to calculate factorial: ")
USERFACTORIAL=int(USERNUMBER)
FACTORIAL_RESULT=FACTORIAL(USERFACTORIAL)
print(f"Your Factorial number of your number: {FACTORIAL_RESULT}")


def FIBONACCI(x):
    """Calculate Fibonacci number"""
    if x==0:
        return 0
    elif x==1:
        return 1
    else:
        return FIBONACCI(x-1)+FIBONACCI(x-2)
USERNUM=input("Enter your number to calculate to Fibonacci number: ")
USERFIBONACCI=int(USERNUM)
FIBONACCI_RESULT=FIBONACCI(USERFIBONACCI)
print(f"Your Fibonacci number is: {FIBONACCI_RESULT}")