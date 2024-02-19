#-----------------DATETIME-------------------
import datetime
import time

CUR_YEAR= datetime.datetime.now().year
print("Welcome to datetime")
print(f"It's {CUR_YEAR} now")
print("="*20+"\n")
time.sleep(2)

USERNAME = input("Enter your name: ")
AGE = int(input("Enter your age: "))
BORN_AGE=CUR_YEAR-AGE
FUTURE_AGE=2100-BORN_AGE
print("Calculating...")
print("="*20+"\n")
time.sleep(2)
print(f"So {USERNAME}, you're {AGE} years old and you born in {BORN_AGE}, in 2100 you will be {FUTURE_AGE} years old")

