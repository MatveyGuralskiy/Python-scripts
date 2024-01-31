#-----------------Bubble sort with JSON----------------
import json
import time
def BUBBLE_SORT(MYLIST):
    """Bubble sort of array"""
    LAST_ITEM=len(MYLIST)-1
    for ELEM in range(0,LAST_ITEM):
        #Total elements inside the array
        for SORTING in range(0,LAST_ITEM-ELEM):
            #Sorting elements
            print(f"Processing... {MYLIST}")
            time.sleep(0.5)
            if MYLIST[SORTING]>MYLIST[SORTING+1]:
                MYLIST[SORTING],MYLIST[SORTING+1]=MYLIST[SORTING+1],MYLIST[SORTING]
    return MYLIST

INPUT_FILE="C:\\Users\\Matvey\\Desktop\\Python\\ARRAY.txt"
OUTPUT_FILE="C:\\Users\\Matvey\\Desktop\\Python\\Bubble_Sorted_Array.txt"

INPUT_OPEN=open(INPUT_FILE,mode="r",encoding="utf-16")
INPUT_JSON=INPUT_OPEN.read()
ARRAY=json.loads(INPUT_JSON)
INPUT_OPEN.close()

OUTPUT_ARRAY=BUBBLE_SORT(ARRAY.copy())
OUTPUT_OPEN=open(OUTPUT_FILE,mode="a",encoding="utf-16")
OUTPUT_OPEN.write("\t\t\tBubble sorted array\n")
OUTPUT_OPEN.write(json.dumps(OUTPUT_ARRAY))
OUTPUT_OPEN.close()
