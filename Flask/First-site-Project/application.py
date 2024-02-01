#--------------FIRST SITE PROJECT---------------------
from flask import Flask
application=Flask(__name__)

#-----------------PAGES SETTINGS----------------------
@application.route("/")
def INDEX():
    """The main page of project"""
    INDEXFILE="C:\\YOUR PATH\\Flask\\First-site-Project\\INDEX.html"       #Enter your path
    INDEXOPEN=open(INDEXFILE,mode='r')
    INDEXPAGE=INDEXOPEN.read()
    INDEXOPEN.close()
    return INDEXPAGE


@application.route("/help")
def HELP_PAGE():
    """Help page for users"""
    HELPFILE="C:\\YOUR PATH\\Flask\\First-site-Project\\HELPPAGE.html"     #Enter your path
    HELPOPEN=open(HELPFILE,mode='r')
    HELPPAGE=HELPOPEN.read()
    HELPOPEN.close()
    return HELPPAGE


@application.route("/user")
def USER_PAGE():
    """Page of users"""
    return "User's main page"


@application.route("/user/<USERNAME>")
def SHOW_USER_PAGE(USERNAME):
    """User's name"""
    return "Hi!"+USERNAME.upper()


@application.route("/path")
def PATH_PAGE():
    """Path page"""
    return "Please enter the subpath for this page:"


@application.route("/path/<path:subpath>")
def SUBPATH_PAGE(subpath):
    """Print to the page Subpath"""
    return "Subpath of user is: "+subpath


@application.route("/squared")
def SQUARED_MAIN_PAGE():
    """Squared page"""
    return "Please enter to the subpath number you want to calculate"


@application.route("/squared/<int:X>")
def SQUARED_PAGE(X):
    """Calculate squared of user number"""
    return "Squared number from: "+str(X)+" = "+str(X*X)
    
    
#---------------------MAIN----------------------------
if __name__=="__main__":
    application.debug=True
    application.env="FIRST SITE PROJECT"
    application.run()

