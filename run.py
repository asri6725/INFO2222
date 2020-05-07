import bottle
import conf
#-----------------------------------------------------------------------------
# Get our components
# You may eventually wish to put these in their own directories and then load
# Each file separately
# For the template, we will keep them together
import model
#-----------------------------------------------------------------------------

'''
    This file is the one to run to start your webserver
    Keep it clean and keep it simple, you're going to have
    Up to 5 people running around breaking this constantly
    If it's all in one file, then things are going to be hard to fix

    If in doubt, `import this`
'''
#-----------------------------------------------------------------------------
#Testing if this way runs the wsgi server
from bottle import route, get, post, request, redirect, static_file, error, template

import model

#-----------------------------------------------------------------------------
'''
    This file will handle our typical Bottle requests and responses
    You should not have anything beyond basic page loads, handling forms and
    maybe some simple program logic
'''
app = application = bottle.Bottle()
@app.route('/', method='GET')
def login():
    return model.login()

#-----------------------------------------------------------------------------

@app.post('/')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return model.login_check(username, password)


#-----------------------------------------------------------------------------
  
@app.post('/homepage')
def unit_add():
    username = request.forms.get('username')
    unit_add = request.forms.get('unit')
    return model.addUnit(unit_add, username)

#-----------------------------------------------------------------------------

@app.get('/forgot-password')
def forgot():
    return model.forgot_password()

#-----------------------------------------------------------------------------

@app.get('/reset-password')
def forgot():
    return model.reset_password()

#-----------------------------------------------------------------------------

@app.get('/sign-up')
def sign_up():
    return model.signup()

#-----------------------------------------------------------------------------

@app.get('/sign-uperror')
def sign_up():
    return model.signup_error()

#-----------------------------------------------------------------------------

@app.get('/sign-up', method='POST')
def do_sign_up():
    username = request.forms.get('username')
    password = request.forms.get('password')
    email = request.forms.get('email')

    #Need to remove 
    if email is None:
        email = "test123@gmail.com"
    return model.signup_check(username, password, email)

#-----------------------------------------------------------------------------

@app.get('/homepage/<subject>')            
def list_of_topics(subject):
    return model.listTopics(subject)

#-----------------------------------------------------------------------------

@app.post('/homepage/send/<subject>')
@app.post('/homepage/send/homepage/<subject>')
def get_post(subject):
    title = request.forms.get('title')
    content = request.forms.get('content')
    return model.new_post(subject, title, content)

#-----------------------------------------------------------------------------

@app.post('/homepage/<subject>/<value>')            
def topic(subject, value):
    title = request.forms.get('title')
    return model.content(subject, title)


#-----------------------------------------------------------------------------
# Static file paths
#-----------------------------------------------------------------------------

# Allow image loading
@app.route('/img/<picture:path>')
def serve_pictures(picture):
    return static_file(picture, root='img/')

#-----------------------------------------------------------------------------

#Allow everything just incase
@app.route('/<filename:path>')
def server_static(filename):
    return static_file(filename, root='/')


#-----------------------------------------------------------------------------

# Allow javascript
@app.route('/js/<js:path>')
def serve_js(js):
    return static_file(js, root='js/')

#-----------------------------------------------------------------------------
# Allow CSS
@app.route('/css/<css:path>')
def serve_css(css):
    return static_file(css, root='css/')

#-----------------------------------------------------------------------------

@app.error(404)
def error404(error):
    return model.error()


#-----------------------------------------------------------------------------
# It might be a good idea to move the following settings to a config file and then load them
# Change this to your IP address or 0.0.0.0 when actually hosting
host =  conf.ip_conf() #'localhost'10.86.163.196

# Test port, change to the appropriate port to host
port = 8080

# Turn this off for production
debug = True
#-----------------------------------------------------------------------------

#Run the server
if __name__ == "__main__":
    app.run(host=host, port=port, debug=debug)
