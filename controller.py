from bottle import route, get, post, request, redirect, static_file

import model

#-----------------------------------------------------------------------------
'''
    This file will handle our typical Bottle requests and responses
    You should not have anything beyond basic page loads, handling forms and
    maybe some simple program logic
'''

@get('/')
def login():
    return model.login()

@post('/')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return model.login_check(username, password)

@get('/forgot-password')
def forgot():
    return model.forgot_password()

@get('/reset-password')
def forgot():
    return model.reset_password()

@get('/sign-up')
def sign_up():
    return model.signup()

@get('/sign-uperror')
def sign_up():
    return model.signup_error()

@get('/sign-up', method='POST')
def do_sign_up():
    username = request.forms.get('username')
    password = request.forms.get('password')

    return model.signup_check(username, password)


#-----------------------------------------------------------------------------
# Static file paths
#-----------------------------------------------------------------------------

# Allow image loading
@route('/img/<picture:path>')
def serve_pictures(picture):
    return static_file(picture, root='img/')

#-----------------------------------------------------------------------------

#Allow everything just incase
@route('/<filename:path>')
def server_static(filename):
    return static_file(filename, root='/')


#-----------------------------------------------------------------------------

# Allow javascript
@route('/js/<js:path>')
def serve_js(js):
    return static_file(js, root='js/')

#-----------------------------------------------------------------------------
# Allow CSS
@route('/css/<css:path>')
def serve_css(css):
    return static_file(css, root='css/')

#-----------------------------------------------------------------------------
