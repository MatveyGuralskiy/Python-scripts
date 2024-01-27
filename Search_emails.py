        #Regular expressions
#Find emails from the file
import sys,re,os
INPUTFILE="EMAILS.txt"
OUTPUTFILE="SEARCHED_EMAILS"

INPUTOPEN=open(INPUTFILE,mode="r",encoding="latin_1")
OUTPUTOPEN=open(OUTPUTFILE,mode="a",encoding="latin_1")

INPUTMAILS=INPUTOPEN.read()
print(INPUTMAILS.rsplit())
LOOK=r"[\w._-]+@[\w._-]+\.[\w.]+"
RESULTS=re.findall(LOOK,INPUTMAILS)
OUTPUTOPEN.write("\t\t\t---LIST OF EMAILS:---\n")
for item in RESULTS:
    print("List of emails: "+item)
    OUTPUTOPEN.write(item+"\n")
LENMAILS=len(RESULTS)
OUTPUTOPEN.write("\nThe number of emails in file: "+str(LENMAILS)+"\n")
print("="*50+"\n")
os.system('type .\SEARCHED_EMAILS')
INPUTOPEN.close()
OUTPUTOPEN.close()