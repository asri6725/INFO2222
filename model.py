import random
from bottle import template, TEMPLATE_PATH
import os


'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''
import view

# Initialise our views, all arguments are defaults
global TEMPLATE_PATH

TEMPLATE_PATH.insert(0, './templates/')
print(TEMPLATE_PATH)

print(os.getcwd())
page_view = view.View()

users = {"admin":"password"}

#-----------------------------------------------------------------------------
# Login

def login():
    return template('Login.html')

#-----------------------------------------------------------------------------
# Check the login credentials
def login_check(username, password):
    # By default assume bad creds
    # doesn't work for now just to deploy
    login = True
    global users
    if username in users: # right username
        if users[username] == password:
            login = True


    if login:
        return template("homepage.html", name=username)
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
    global users
    if (username not in users):
        users[username] = password
        return template("Login.html")
    else:
        return template("SignupError.html")

#-----------------------------------------------------------------------------
# Signup Error
def signup_error():
    return template("SignupError.html")
