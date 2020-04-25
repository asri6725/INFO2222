import random
from bottle import template, error
import studhelp_dbsql

'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''

# Initialise our views, all arguments are defaults

#we dont need this anymore
users = {'admin':'password', 'abhi':'123'}
subject = ['comp2022', 'info2222', 'comp3333', 'info1111', 'comp2123', 'info3315', 'comp3308', 'data3404', 'tester1231']

#-----------------------------------------------------------------------------
# Login

def login():
    return template('Login.html')

#-----------------------------------------------------------------------------
# Check the login credentials

def login_check(username, password): 
    result = studhelp_dbsql.check_login(username, password)
        


    if result == 0:
        global subject
        return template("homepage.tpl", name=username, subject=subject)
    else:
        return template("LoginError.html", reason="check credentials")



#-----------------------------------------------------------------------------
# Forgot password
def forgot_password():
    return template("ForgotPwd.html")
#-----------------------------------------------------------------------------
# Reset password
def reset_password():
    return template("ResetPwd.html")
#-----------------------------------------------------------------------------
# Signup
def signup():
    return template("Signup.html")
#-----------------------------------------------------------------------------
# Signup Check
def signup_check(username, password):

    result = studhelp_dbsql.check_signup(username, password)

    if (result == 0):
        studhelp_dbsql.add_user(username, password)
        return template("Login.html")
    else:
        return template("SignupError.html")

#-----------------------------------------------------------------------------
# Signup Error
def signup_error():
    return template("SignupError.html")

#-----------------------------------------------------------------------------

def homepage():
    global users
    global subject
    return template("homepage.tpl", name = 'username', subject='subject')

#-----------------------------------------------------------------------------

def error():
    return template("ErrorPage.html")