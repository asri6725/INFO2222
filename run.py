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
from bottle import route, get, post, request, redirect, static_file, error, template, response
import html
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
    if request.get_cookie("username",secret='m14AGroup6'):
        username = request.get_cookie("username", secret='m14AGroup6')
        return model.homepage(username)
    else:
        print("going to login")
        return model.login()

#-----------------------------------------------------------------------------

@app.post('/')
def do_login():

    username = html.escape(request.forms.get('username'))
    if len(username) > 10:
        return model.error()
    password = html.escape(request.forms.get('password'))
    if len(password) > 20:
        return model.error()
    #response.set_cookie("username",username, secret='m14AGroup6')

        
    return model.login_check(username, password)


#-----------------------------------------------------------------------------
  
@app.post('/homepage')
def unit_add():
    if request.get_cookie("username"):
        username = request.get_cookie("username",secret='m14AGroup6')
        unit_add = html.escape(request.forms.get('unit'))
        if len(unit_add) != 8:
            return model.error()
        return model.addUnit(unit_add, username)
    else:
        return model.login()

#-----------------------------------------------------------------------------

@app.get('/forgot-password')
def forgot():
    return model.forgot_password()
#-----------------------------------------------------------------------------

@app.get('/reset-password')
def forgot():
    return model.reset_password()

#-----------------------------------------------------------------------------

@app.post('/forgot-pwd')
def reset_pass():
    email = html.escape(request.forms.get("email"))
    if len(email)>50:
        return model.error()
    return model.reset_pass(email)

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
    username = html.escape(request.forms.get('username'))
    if len(username) > 10:
        return model.error()
    password = html.escape(request.forms.get('password'))
    if len(password) > 20:
        return model.error()
    email = html.escape(request.forms.get('email'))
    if len(email)>50:
        return model.error()
    #Need to remove 
    if email is None:
        email = "test123@gmail.com"
    return model.signup_check(username, password, email)

#-----------------------------------------------------------------------------

@app.get('/homepage/<subject>')            
def list_of_topics(subject):
    if request.get_cookie("username",secret='m14AGroup6'):
        username = request.get_cookie("username",secret='m14AGroup6')
        return model.listTopics(subject, username)
    else:
        return model.login()

#-----------------------------------------------------------------------------

@app.post('/homepage/send/<subject>')
@app.post('/homepage/send/homepage/<subject>')
def get_post(subject):
    if request.get_cookie("username",secret='m14AGroup6'):
        title = html.escape(request.forms.get('title'))
        if len(title) > 100:
            return model.error()
        content = html.escape(request.forms.get('content'))
        print(content)
        if len(content) > 250:
            return model.error()
        username = request.get_cookie("username",secret='m14AGroup6')
        return model.new_post(subject, title, content, username)
    else:
        return model.login()

#-----------------------------------------------------------------------------

@app.post('/homepage/<subject>/<value>')            
def topic(subject, value):
    if request.get_cookie("username",secret='m14AGroup6'):
        title = html.escape(request.forms.get('title'))
        if len(title) > 100:
            return model.error()
        username = request.get_cookie("username",secret='m14AGroup6')
        return model.content(subject, title, username)
    else:
        return model.login()

#-----------------------------------------------------------------------------

@app.post('/homepage/comment/<subject>/<value>')
def add_comment(subject, value):
    if request.get_cookie("username",secret='m14AGroup6'):
        comment = html.escape(request.forms.get("comment"))
        username = request.get_cookie("username",secret='m14AGroup6')
        title = html.escape(request.forms.get("title"))
        unit = html.escape(request.forms.get("unit"))
        if len(title) > 100 or len(username)>10 or len(comment)>250:
            return model.error()
        if unit!=subject:
            return model.error()
        return model.new_comment(subject, title, comment,username)
    else:
        return model.login()


#-----------------------------------------------------------------------------

@app.get('/messages')
def list_users():
    print("list of users")
    if request.get_cookie("username",secret='m14AGroup6'):
        username = request.get_cookie("username",secret='m14AGroup6')
        return model.overview_messages(username)
    else:
        return model.login()

#-----------------------------------------------------------------------------

@app.post('/messages/<user>')
def view_chat(user):
    print("view chat")
    if request.get_cookie("username",secret='m14AGroup6'):
        username = request.get_cookie("username",secret='m14AGroup6')
        user_to_chat = html.escape(request.forms.get("message_user"))
        if len(user_to_chat) > 10:
            return model.error()
        return model.get_messages(username, user_to_chat)
    else:
        return model.login()

#-----------------------------------------------------------------------------

@app.post('/messages/send')
def new_message():
    print("Enter controller for messages post")
    if request.get_cookie("username",secret='m14AGroup6'):
        username = request.get_cookie("username",secret='m14AGroup6')
        user_to_chat = html.escape(request.forms.get("message_user"))
        message = html.escape(request.forms.get("message"))
        if len(message) > 100 or len(user_to_chat)>10:
            return model.error()
        print("Going to model")
        return model.new_message(username, user_to_chat, message)
    else:
        return model.login()

#-----------------------------------------------------------------------------
@app.get('/signout')
def signout():
    response.delete_cookie("username",secret='m14AGroup6')
    username = request.get_cookie("username")
    print(username)
    return model.login()

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
@app.error(500)
@app.error(502)
@app.error(400)
@app.error(401)
@app.error(403)
@app.error(503)

def error404(error):
    print(error)
    return model.error()


#-----------------------------------------------------------------------------
# It might be a good idea to move the following settings to a config file and then load them
# Change this to your IP address or 0.0.0.0 when actually hosting
host =  conf.ip_conf() #'localhost'10.86.163.196

# Test port, change to the appropriate port to host
port = 8080

# Turn this off for production
debug = False
#-----------------------------------------------------------------------------

#Run the server
if __name__ == "__main__":
    app.run(host=host, port=port, debug=debug)
