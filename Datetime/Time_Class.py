from datetime import time

curTime = time(15,5,12)
print(f"Your choosen time is {curTime}")

#Or the second way to print
curTime = time.fromisoformat("15:05:12")
print(f"Your choosen time is {curTime} with (fromisoformat)")