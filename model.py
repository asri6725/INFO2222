import random
from bottle import template

'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''
import view

# Initialise our views, all arguments are defaults
page_view = view.View()

users = {"admin":"password"}

#-----------------------------------------------------------------------------
# Login

def login():
    return template('templates/Login.html')

#-----------------------------------------------------------------------------
# Check the login credentials
def login_check(username, password):
    # By default assume bad creds
    login = True

    if username == "admin@gmail.com" and password=="password": # Wrong Username
        login = True



    if login:
        return template("templates/homepage.html", name=username)
    else:
        return template("templates/LoginError.html", reason="check credentials")

#-----------------------------------------------------------------------------
# Forgot password
def forgot_password():
    return template("templates/ForgotPwd.html")
#-----------------------------------------------------------------------------
# Reset password
def reset_password():
    return template("templates/ResetPwd.html")
#-----------------------------------------------------------------------------
# Signup
def signup():
    return template("templates/Signup.html")
#-----------------------------------------------------------------------------
# Signup Check
def signup_check(username, password):
    global users
    if (username not in users):
        users[username] = password
        return template("templates/Login.html")
    else:
        return template("templates/SignupError.html")

#-----------------------------------------------------------------------------
# Signup Error
def signup_error():
    return template("templates/SignupError.html")
