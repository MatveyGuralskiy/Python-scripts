#-------------------Binary Search------------------
def BINARYSEARCH(SORTEDMYLIST,SEARCHNUM,START,STOP):
    """Binary search in array of numbers"""
    if START > STOP:
        return False
    else:
        MIDDLE=(START+STOP)//2
        if SEARCHNUM==SORTEDMYLIST[MIDDLE]:
            return MIDDLE
        elif SEARCHNUM<SORTEDMYLIST[MIDDLE]:
            return BINARYSEARCH(SORTEDMYLIST,SEARCHNUM,START,MIDDLE-1)
        else:
            return BINARYSEARCH(SORTEDMYLIST,SEARCHNUM,MIDDLE+1,STOP)
        

MYLIST=[0,3,104,5,6,7,8,45,16,18,19,23,56,34,67,78,98,100]
SORTEDMYLIST=sorted(MYLIST)
print(SORTEDMYLIST)

SEARCHNUM=int(input("Write your number to binary search in array: "))
START=0
STOP=len(MYLIST)

X=BINARYSEARCH(SORTEDMYLIST,SEARCHNUM,START,STOP)
if X==False:
    print(f"The number {SEARCHNUM} not found")
else:
    print(f"The number {SEARCHNUM} is in your array\nIndex number in array: {X}")
