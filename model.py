import random
from bottle import template, error

'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''

# Initialise our views, all arguments are defaults

users = {'admin':'password', 'abhi':'123'}
subject = ['comp2022', 'info2222', 'comp3333', 'info1111', 'comp2123', 'info3315', 'comp3308', 'data3404']

#-----------------------------------------------------------------------------
# Login

def login():
    return template('Login.html')

#-----------------------------------------------------------------------------
# Check the login credentials
def login_check(username, password):
    # By default assume bad creds
    # doesn't work for now just to deploy
    login = False
    global users
    for user in users.keys():
        if username == user: # right username
            #print("Username check exist, password should be", users[username])
            if users[username] == password:
                login = True
        # else:
        #     print("username: ", username, ", not equal to user: ", user)
        


    if login==True:
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
    global users
    exist = False
    for user in users.keys():
        if username == user:
            exist = True
    if (exist == False):
        users[username] = password
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