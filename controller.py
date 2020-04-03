from bottle import route, get, post, request, redirect, static_file

import model

#-----------------------------------------------------------------------------
'''
    This file will handle our typical Bottle requests and responses 
    You should not have anything beyond basic page loads, handling forms and 
    maybe some simple program logic
'''
# Static file paths
#-----------------------------------------------------------------------------

# Allow image loading
@route('/img/<picture:path>')
def serve_pictures(picture):
    return static_file(picture, root='img/')


#-----------------------------------------------------------------------------
# Allow CSS
@route('/css/<css:path>')
def serve_css(css):
    return static_file(css, root='css/')

#-----------------------------------------------------------------------------

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
    username = "admin"
    return model.units(username)

#-----------------------------------------------------------------------------

@get('/homepage/subject/topic')
def topic():
    username = "admin"
    return model.topic(username)

#-----------------------------------------------------------------------------