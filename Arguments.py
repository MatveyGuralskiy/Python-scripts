#-------------------Intercepting errors-----------------------
import sys,time,os


def CORRECTINPUT():
    """Check if your input is correct"""
    while True:
        ANSWER="exit"
        USERINPUT=input("Please write a secret command: ")
        if USERINPUT==ANSWER:
            return "You're successfully entered to the script..."
        else:
            print("Please try again")


RESULT=CORRECTINPUT()
print(RESULT)
FILE="Argume.txt"
while True:     
    try:
        print("Inside try")
        print("Try to open the file...")
        OPENFILE=open(FILE,mode="r",encoding="utf_8")
        pass
        time.sleep(2)
        #if
    except Exception:
        print("Inside except")
        print("Errors are found")
        print(sys.exc_info()[1])
        FILE=input("Enter the correct file: ")
    else:
        print("Inside else")
        print(OPENFILE.read())
        sys.exit()
    finally:
        print("Inside finally\nIf you don't have any errors,\tyou can continue your script")
        break
        
#-------------------------Arguments-----------------------------
APPENDFILE=open(FILE,mode='a',encoding='latin_1')
HELPREQUEST="Welcome to Help request\nman version 1.0.0 01.2024\nUsage of python.exe"
x=len(sys.argv)
if x>1:
    print("Arguments: "+str((sys.argv[1:])))
    if sys.argv[1]=="/?":
        print(HELPREQUEST)
        APPENDFILE.write("\nHELP REQUEST:\n")
        APPENDFILE.write("\n"+HELPREQUEST+"\tComplete...\n")
    else:
        print("Arguments are not provide")
        for line in FILE:
            APPENDFILE.write(str(line))
        APPENDFILE.write("\nAll list of Arguments:\n")
        for arg in sys.argv[1:]:
            APPENDFILE.write(arg+"\n")
    APPENDFILE.close()


#-----------------------Library OS------------------------------
        #To see what's file include inside
os.system("type Arguments.txt")
os.system("dir Arguments.txt")