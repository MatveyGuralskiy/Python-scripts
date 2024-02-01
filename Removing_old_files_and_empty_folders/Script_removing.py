#!/bin/python3
#-------------------------------SCRIPT REMOVING----------------------
#------------SCRIPT REMOVING OLD FILES AND EMPTY DIRECTORIES---------
import os,time
 
DAYS=0                                                      #Max age of file to stay, older will be deleted
FOLDERS= [                                                  #Directories you want to remove
        "C:\\YOUR PATH\\Removing_old_files_and_empty_folders\\TRASH\\Trash1",
        "C:\\YOUR PATH\\Removing_old_files_and_empty_folders\\TRASH\\Trash2",
        "C:\\YOUR PATH\\Removing_old_files_and_empty_folders\\TRASH\\Trash3"
         ]

TOTAL_DELETED_SIZE=0                                        #Deleted size stats(size in Bytes)
TOTAL_DELETED_FILES=0                                       #Deleted files
TOTAL_DELETED_DIRS=0                                        #Deleted directories

NOWTIME=time.time()                                         #Get current time in seconds
AGETIME=NOWTIME-60*60*24*DAYS                               #Minus DAYS in seconds


def DELETE_OLD_FILES(folder):
    """Delete all old files older than X DAYS"""
    global TOTAL_DELETED_FILES                              #To initialize total deleted files
    global TOTAL_DELETED_SIZE                               #To initialize total deleted size
    for path,dirs,files in os.walk(folder):                 #Shows all path,name directory and files
        for FILE in files:
            FILENAME=os.path.join(path,FILE)                #To get full path to the file
            FILETIME=os.path.getmtime(FILENAME)             #When files was created(time in seconds)
            if FILETIME<AGETIME:
                SIZEFILE=os.path.getsize(FILENAME)
                TOTAL_DELETED_SIZE+=SIZEFILE                #Count sum of all free space
                TOTAL_DELETED_FILES+=1                      #Count number of deleted files
                print("Deleting files: "+str(FILENAME))
                os.remove(FILENAME)


def DELETE_EMPTY_DIR(folder):
    """Delete empty directory"""
    global TOTAL_DELETED_DIRS                               #To initialize total deleted directories
    EMPTY_FOLDERS=0
    for path,dirs,files in os.walk(folder):
        if (not dirs) and (not files):
            TOTAL_DELETED_DIRS+=1                           #Count numbers of deleted directories
            EMPTY_FOLDERS+=1                                #Count empty folders 
            print("Deleting empty directory: "+str(path))
            os.rmdir(path) 
    if EMPTY_FOLDERS>0:
        DELETE_EMPTY_DIR(folder)                           #Recursion of the function if you have parent folders

#---------------------------------MAIN------------------------------
STARTTIME=time.asctime()

for folder in FOLDERS:
    DELETE_OLD_FILES(folder)                               #Delete old files functions
    DELETE_EMPTY_DIR(folder)                               #Delete empty directories function

FINISHTIME=time.asctime()

print("="*50)
print("Start time: "+str(STARTTIME))
print("Total deleted size: "+str(int(TOTAL_DELETED_SIZE/1024/1024))+"MB")
print("Total deleted files: "+str(TOTAL_DELETED_FILES))
print("Total deleted empty directories: "+str(TOTAL_DELETED_DIRS))
print("Finish time: "+str(FINISHTIME))
print("="*50)
