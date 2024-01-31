#-----------------Bubble sort----------------

def BUBBLE_SORT(MYLIST):
    """Bubble sort of array"""
    LAST_ITEM=len(MYLIST)-1
    for ELEM in range(0,LAST_ITEM):
        #Total elements inside the array
        for SORTING in range(0,LAST_ITEM-ELEM):
            #Sorting elements
            print(f"Processing... {MYLIST}")
            if MYLIST[SORTING]>MYLIST[SORTING+1]:
                MYLIST[SORTING],MYLIST[SORTING+1]=MYLIST[SORTING+1],MYLIST[SORTING]
    return MYLIST


ARRAY=[10,34,65,32,67,89,1,31,88,72,95,100,55,76]
print(f"Your array: {ARRAY}")
NEW_ARRAY=BUBBLE_SORT(ARRAY).copy()
print(f"Bubble sorted array:  {NEW_ARRAY}")
