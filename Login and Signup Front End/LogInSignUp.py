from bottle import run, route, request, static_file, template

d = dict()

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./images')

@route('/login')
def login():
    return template('Login.tpl')

@route('/login', method='POST')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Website Home Page.</p>"
    else:
        return template('LoginError.tpl')

@route('/forgot-password')
def forgot():
    return template('ForgotPwd.tpl')

@route('/reset-password')
def forgot():
    return template('ResetPwd.tpl')

@route('/sign-up')
def sign_up():
    return template('Signup.tpl')

@route('/sign-uperror')
def sign_up():
    return template('SignupError.tpl')

@route('/sign-up', method='POST')
def do_sign_up():
    username = request.forms.get('email')
    password = request.forms.get('password')

    if check_sign_up(email, password):
        d[email] = password
        return template('Login.tpl')
    else:
        return template('SignupError.tpl')

def check_sign_up(username, password):
    global d
    if username in d:
        return False
    else:
        return True

def check_login(username, password):
    global d
    if username in d:
        if password == d[username]:
            return True

    return False
# http://localhost:2000/login
run(host='localhost', port=2000)
