import random
from bottle import template, TEMPLATE_PATH

'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''

# Initialise our views, all arguments are defaults

users = {'admin':'password', 'abhi':'123'}
print(users.keys())
print(users.values())
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
            print("Username check exist, password should be", users[username])
            if users[username] == password:
                login = True
        else:
            print("username: ", username, ", not equal to user: ", user)
        


    if login==True:
        subject = {'name':'INFO2222', 'code': 'COMP3333'}
        return template("homepage.tpl", name="username", subject=subject)
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
