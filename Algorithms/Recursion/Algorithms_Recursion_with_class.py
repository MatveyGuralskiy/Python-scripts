#---------------------Recursions------------------
#!/usr/bin/env python3

class Recursions():
    """Class of Recursions"""
    def __init__(self):
        pass


    def Factorial(self,X):
        if X==0:
            return 1
        else:
            return int(X)*self.Factorial(int(X-1))
    
    
    def Fibonacci(self,Y):
        if Y==0:
            return 1
        elif Y==1:
            return 1
        else:
            return self.Fibonacci(int(Y-1))+self.Fibonacci(int(Y-2))
 

#----------------------MAIN-----------------------
RESULT=Recursions() 

    #Input of user

while True:
    try:
        USERNUM=input("Enter your number you want to calculate: ")
        USER_RECURSION=int(USERNUM)
        USER_TYPE=input("Choose the type of recursion 'Factorial' or 'Fibonacci' ")

        if USER_TYPE=="Factorial":
            print(RESULT.Factorial(USER_RECURSION))
        elif USER_TYPE=="Fibonacci":
            print(RESULT.Fibonacci(USER_RECURSION))
        else:
            print("Try again please\nChoose between recursions:\n")
            continue

        
        CHOOSE=input("Do you want to exit from the script? ").lower()
        if CHOOSE=='yes' or CHOOSE=='yeah':
            print("Have a nice day!")
            break
        elif CHOOSE=='no' or CHOOSE=='not':
            pass
        else:
            print("Invalid input, You will be return to the start of script")
            continue

    except ValueError:
        print("Invalid input, please enter the integer number")

    finally:
        print("Recursion script by Matvey Guralskiy")