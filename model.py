import random
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


#-----------------------------------------------------------------------------
# Login
#-----------------------------------------------------------------------------

def main_page():
    return page_view("login")

#-----------------------------------------------------------------------------

# Check the login credentials
def login_check(username, password):
    # By default assume bad creds
    login = True
    
    if username != "admin": # Wrong Username
        err_str = "Incorrect Username"
        login = False
    
    if password != "password": # Wrong password
        err_str = "Incorrect Password"
        login = False
        
    if login: 
        return page_view("homepage", name=username)
    else:
        return page_view("invalid", reason=err_str)
    


#-----------------------------------------------------------------------------

#go to units
def units(username):

    return page_view("units", name=username)


#-----------------------------------------------------------------------------

#go to topic
def topic(username):
    return page_view("topic", name=username)

