#----------------CALCULATE OPERATIONS--------------
class OPERATIONS:
    """Class of operations"""
    def __init__(self):
        """First method"""
        pass


    def Division(self,num1,num2):
        """Division of 2 numbers"""
        print(f"Division 2 numbers {num1},{num2}")
        if num2 != 0:
            result=num1 // num2
        else:
            return 0
        return result


    def GreaterOne(self,num1,num2):
        """Find the greater number"""
        print("Calculate the greater one")
        if num1==num2:
            print("The numbers are equal")
            return num1
        elif num1>num2:
            print("The first number is the greater")
            return num1
        else:
            print("The second number is greater")
            return num2


    def Count_Digit(self,digit,num):
        """Back number of digits in the num"""
        if num<0:
            print("Error the number should be greater than 0")
            exit(1)
        COUNT=0
        STR_NUM=str(num)
        for CHAR in STR_NUM:
            if CHAR==str(digit):
                COUNT+=1
        return COUNT


    def Stars(self,num):
        """Back count of number in stars"""
        stars='*'*num
        return stars
    

    def Stars_Square(self,size):
            """Back count of number in stars as shape square"""
            square=''
            for unit in range(size):
                square+='*'*size+'\n'
            return square


if __name__=="__main__":
    """Record to the main"""
    SELF_OPERATIONS=OPERATIONS()
    num=15              #Enter your number
    STARS_STRING=SELF_OPERATIONS.Stars(num)
    print("\n"+STARS_STRING)
    NUM_STARS=len(STARS_STRING)
    print("Number of stars at Stars method:"+str(NUM_STARS)+"\n")
    size=45
    STARS_SQUARE_STRING=SELF_OPERATIONS.Stars_Square(size)
    print(STARS_SQUARE_STRING)
    NUM_SQUARE=(len(STARS_SQUARE_STRING)//size)-1
    print(f"The size of the side is {NUM_SQUARE}")


#-------------------MAIN------------------------
SELF_OPERATIONS=OPERATIONS()
print(SELF_OPERATIONS.Division(12,3))
print(SELF_OPERATIONS.GreaterOne(85,88))
print(SELF_OPERATIONS.Count_Digit(2,780214324124))
