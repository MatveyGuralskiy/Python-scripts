#---------------------Duplicate Numbers at Lists--------------------------

FIRST_LIST=input("Enter a first list of numbers, separated by spaces: ")
SECOND_LIST=input("Enter a second of numbers, separated by spaces: ")

USER_FIRST_LIST=(FIRST_LIST).split()   
USER_SECOND_LIST=(SECOND_LIST).split()

FIRST_LIST_NUM= set([int(i) for i in USER_FIRST_LIST])
SECOND_LIST_NUM= set([int(i) for i in USER_SECOND_LIST])

DUPLICATE_FIRST_LIST = [int(i) for i in USER_FIRST_LIST if USER_FIRST_LIST.count(i) > 1]
DUPLICATE_SECOND_LIST = [int(i) for i in USER_SECOND_LIST if USER_SECOND_LIST.count(i) > 1]

UNIQUE_DUPLICATES= list(FIRST_LIST_NUM.intersection(SECOND_LIST_NUM))
UNIQUE_DUPLICATES.sort()

#------------------------------MAIN------------------------------------------
print(f"Your duplicate numbers at first list: {DUPLICATE_FIRST_LIST}")
print(f"Your duplicate numbers at second list: {DUPLICATE_SECOND_LIST}")
print(f"Your unique duplicate numbers at lists: {UNIQUE_DUPLICATES}")