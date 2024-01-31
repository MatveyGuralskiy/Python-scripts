#!/bin/python3
#------------------Log-files cleaning---------------
import sys
import os
import shutil

#Example to run Log-file cleaning
#Number of arguments:                  0             1       2 3
                    #python3 Log_files_cleaning.py FILE.txt 10 3
#Or enter python3 instead python

if(len(sys.argv)<4):
    """Check if number of arguments is correct"""
    print("Missing arguments\nPlease correct your arguments and try again")
    exit(1)
FILE=sys.argv[1]
LIMITSIZE=int(sys.argv[2])
LOG_NUMBER=int(sys.argv[3])
if(os.path.isfile(FILE)==True):
    """Check if main exist"""
    LOG_SIZE=os.stat(FILE).st_size
    #To convert to Kilobytes
    LOG_SIZE=LOG_SIZE/1024
    if(LOG_SIZE>=LIMITSIZE):
        """Check if you should clean the log-file"""
        if(LOG_NUMBER>0):
            """Just clear the main file if it's limit size"""
            for CURRENT_FILE_NUM in range(LOG_NUMBER,1,-1):
                """Loop from Max number to the main file"""
                SOURCE=FILE+"_"+str(CURRENT_FILE_NUM-1) #Previous file
                DESTINATION=FILE+"_"+str(CURRENT_FILE_NUM) #Current file
                if(os.path.isfile(SOURCE)==True):
                    """If the previous is exist copy him to the current"""
                    shutil.copyfile(SOURCE,DESTINATION)
                    print(f"Copied: {SOURCE} to {DESTINATION}")

            shutil.copyfile(FILE,FILE+"_1")
            """For the first file"""
            print(f"Copied: {FILE} to {FILE}_1")
        OPEN_FILE=open(FILE,mode="w")
        OPEN_FILE.close()
