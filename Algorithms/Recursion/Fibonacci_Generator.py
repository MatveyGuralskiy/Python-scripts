#-----------Fibonacci generator-------------
import time

def MAIN_FUNCTION():
    print("Welcome to Fibonacci generator!\nThink about some number...")
    time.sleep(2)
    USER_GENERATOR = int(input("Enter the number for the Fibonacci generator to search: "))

    def FIBONACCI_GENERATOR(USER_INPUT):
        """Fibonacci generator function"""
        if USER_INPUT < 0:
            print("The number must be greater than 0")
            exit(1)
        elif USER_INPUT == 0:
            return 0
        elif USER_INPUT == 1:
            return 1
        FIBONACCILIST = [0, 1]
        for NUMBER in range(2, USER_INPUT + 1):
            FIBONACCILIST.append(FIBONACCILIST[NUMBER-1] + FIBONACCILIST[NUMBER-2])
        return FIBONACCILIST[-1]

    def FIBONACCI_SEQUENCE(NUMBER):
        FIBONACCILIST = [0, 1]
        while FIBONACCILIST[-1] < NUMBER:
            FIBONACCILIST.append(FIBONACCILIST[-1] + FIBONACCILIST[-2])
        if FIBONACCILIST[-1] > NUMBER:
            FIBONACCILIST.pop()
        return FIBONACCILIST

    print(f"Fibonacci number place {USER_GENERATOR} equal to number: ", FIBONACCI_GENERATOR(USER_GENERATOR))
    SEQUENCE = FIBONACCI_SEQUENCE(USER_GENERATOR)
    print(f"Fibonacci sequence of User {USER_GENERATOR} = {SEQUENCE} ")

#-------------------MAIN---------------------------
MAIN_FUNCTION()