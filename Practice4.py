#Functions

def PRINTSCRIPT():
    """PRINT SYMBOL '-'"""
    print()
    print("-"*30)


def NAMES(NAME):
    """NAMES OF COMPANY"""
    print("The DevOps enginer/s:\t"+NAME.title())
#-------------------------
PRINTSCRIPT()
NAMES(input("Write a name of worker:\t"))
PRINTSCRIPT()

def SUMMARY(x,y):
    """SUM OF 2 NUMBERS(X+Y)"""
    return x+y
#-------------------------
print("Sum of 2 numbers x and y is:\t"+str(SUMMARY(15,25)))
PRINTSCRIPT()

def FACTORIAL(x):
    """CALCULATE FACTORIAL OF NUMBER"""
    ANSWER=1
    for NUM in range(1,x+1):
        ANSWER=ANSWER*NUM
    return ANSWER
#-------------------------
for b in range(1,10):
    print(str(b)+"! = \t"+str(FACTORIAL(b)))
PRINTSCRIPT()


def DICTIONARY_RECORD(D_NAME,D_TELEPHONE,D_ADRESS):
    """DICTIONARY OF NAMES,PHONES,ADRESSES"""
    RECORD={
        'NAME':D_NAME,
        'PHONES':D_TELEPHONE,
        'ADRESS':D_ADRESS,
    }
    return RECORD
#-------------------------
print(DICTIONARY_RECORD('Petr','+495935494','NY'))
PRINTSCRIPT()


def OBJECTS(PLACE,*PEOPLE):
    """LIST OF MANY PEOPLE OF COMPANY AND PLACES OF WORK"""
    for p in PEOPLE:
        print("Persons in company:\t"+p.title()+"\t\tPlaces of companies:\t"+PLACE)
#-------------------------
OBJECTS('Chicago','arnorld','johnny','lionel')
