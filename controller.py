from bottle import route, get, post, request, redirect, static_file

import model

#-----------------------------------------------------------------------------
'''
    This file will handle our typical Bottle requests and responses 
    You should not have anything beyond basic page loads, handling forms and 
    maybe some simple program logic
'''
# Redirect to login
@get('/')
def get_index():
    return model.main_page()

#-----------------------------------------------------------------------------

# Attempt the login
@post('/')
def post_login():
    # Handle the form processing
    username = request.forms.get('username')
    password = request.forms.get('password')
    
    # Call the appropriate method
    return model.login_check(username, password)


#-----------------------------------------------------------------------------

@get('/homepage/subject')
def units():
 	return model.units()

#-----------------------------------------------------------------------------