#---------Convertion of numbers----------
import time
print("Welcome to convert numbers")
MESSAGE=input("Please choose your options to convert,enter the number of option you want to choose: \n1.Binary-->Decimal\n2.Decimal-->Binary\n3.Octal-->Decimal\n4.Decimal-->Octal\n")
print("="*30)

#---------------Main Conviguration----------------
NUMBER=input("Now enter your number to convert: ")
print("Convert...")
time.sleep(2)
if MESSAGE=="1." or MESSAGE=="1":
    """Binary to Decimal"""
    ANSWER_BIN=int(NUMBER, 2)
    print(f"Your binary number {NUMBER} convert to {ANSWER_BIN}\nHave a nice day!")
elif MESSAGE=="2." or MESSAGE=="2":
    """Decimal to Binary"""
    NUMBER_BIN=int(NUMBER)
    print(f"Your number {NUMBER} convert to binary: "+bin(NUMBER_BIN)+"\nHave a nice day!")
elif MESSAGE=="3." or MESSAGE=="3":
    """Octal to Decimal"""
    ANSWER_OCT=int(NUMBER, 8)
    print(f"Your octal number {NUMBER} convert to {ANSWER_OCT}\nHave a nice day!")
elif MESSAGE=="4." or MESSAGE=="4":
    """Decimal to Octal"""
    NUMBER_OCT=int(NUMBER)
    print(f"Your number {NUMBER} convert to octal: "+oct(NUMBER_OCT)+"\nHave a nice day!")
else:
    print("Please try another one")
    exit()
