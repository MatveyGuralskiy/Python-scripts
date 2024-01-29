#-------Working with the Internet(GET,POST,Donwload files from sites)-------

#-------------------------GET----------------------------
import sys
from urllib import request
import time

    #URL I choose it's a test http site
URL="http://www.testingmcafeesites.com/index.html"
ANSWER=request.urlopen(URL)
URLTEXT=ANSWER.readlines()

try:
    """Open your site and print the text"""
    print("Open the site:\nProcessing...")
    time.sleep(2)
    for LINES in URLTEXT:
        print(LINES)
except Exception:
    """Error to connect to the site and print information"""
    print("Error occuried during web request...")
    print(sys.exc_info()[1])
finally:
    """End of checking web request"""
    time.sleep(1)
    print("Have a nice day!")


#-------------------------POST----------------------------
from urllib import request,parse
import sys
import time

    #Google search "Apple"
URL="https://www.google.com/search?"
VALUE={'q':'Apple'}

#PRESS F12 in Your Browser-->Network-->Choose some action-->Headers-->Request Headers-->User-agent
HEADERS={}
HEADERS['User-Agent']= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'

try:
    """Encode the search of the user"""
    DATA=parse.urlencode(VALUE)
    print("Your search request: "+DATA+"Processing")
    time.sleep(2)
    URL+=DATA
    REQ=request.Request(URL,headers=HEADERS)
    ANSWER=request.urlopen(REQ)
    ANSWER=ANSWER.readlines()
    for LINES in ANSWER:
        print(LINES)
except Exception:
    """Error of searching web request"""
    print("Error occuried during web request...")
    print(sys.exc_info()[1])
finally:
    """End of searching user's request"""
    time.sleep(1)
    print("Have a nice day!")

#-------------------------Download files for sites----------------------------
from urllib import request
import sys
import time

        #Download image test
URL="https://sample-videos.com/images/amcodr.jpg"
#Your file path, don't forget double slash
FILE="C:\\Users\\Your user name\\Desktop\\FILE.jpg"

try:
    """Checks the file's link site"""
    print("Your picture search in progress...")
    time.sleep(1)
    print("Download the picture...")
    time.sleep(2)
    request.urlretrieve(URL,FILE)
except Exception:
    """Error with searching your file"""
    print("Error occuried during web request or non-existent file")
    print(sys.exc_info()[1])
    exit
finally:
    """End of searching and downloading your file"""
    time.sleep(1)
    print("Have a nice day!")
print("File downloaded and saved "+FILE)
