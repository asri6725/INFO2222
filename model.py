import random
from bottle import template, error, redirect
import studhelp_dbsql
import conf
'''
    Our Model class
    This should control the actual "logic" of your website
    And nicely abstracts away the program logic from your page loading
    It should exist as a separate layer to any database or data structure that you might be using
    Nothing here should be stateful, if it's stateful let the database handle it
'''

# Initialise our views, all arguments are defaults

#we dont need this anymore
#Jackey this is the design for users
#Anyone feel free to add your name and subjects here and it will show them in the login


#-----------------------------------------------------------------------------
# Login

def login():
    return template('Login.tpl', server = conf.complete_server_conf()) 

#-----------------------------------------------------------------------------
# Check the login credentials

def login_check(username, password): 
    if len(username) == 0:
        return error("No username written")
    if len(password) == 0:
        return error("No password written")
    result = studhelp_dbsql.check_login(username, password)

    if result == 0:
        #checking the units that the user chose and only showing them in the homepage
        subject = studhelp_dbsql.get_user_subject(username)
        if subject == -3:
            return error()
        return template("homepage.tpl", name=username, subject=subject, server = conf.complete_server_conf())
    else:
        return template("LoginError.tpl", reason="check credentials", server = conf.complete_server_conf())

#-----------------------------------------------------------------------------

def homepage(username):
    if len(username)==0:
        return error()
    subject = studhelp_dbsql.get_user_subject(username)
    if subject == -3:
        return error()
    return template("homepage.tpl", name=username, subject=subject, server = conf.complete_server_conf())
#-----------------------------------------------------------------------------

def addUnit(unit, username):
    #ADD unit to DB with the username and return homepage
    subject = studhelp_dbsql.unit_add(username, unit)
    if subject == -3:
        return error()
    return template("homepage.tpl", name=username, subject=subject, server = conf.complete_server_conf())

#-----------------------------------------------------------------------------
# Forgot password
def forgot_password():
    return template("ForgotPwd.tpl", server = conf.complete_server_conf())
#-----------------------------------------------------------------------------
# Reset password
def reset_password():
    return template("ResetPwd.tpl", server = conf.complete_server_conf())
#-----------------------------------------------------------------------------
# Send the email for reset
def reset_pass(email):
    if len(email) == 0:
        return error("No email mentioned")
    ret = studhelp_dbsql.send_password(email)
    url = conf.complete_server_conf()+"/"
    if ret == -3 or ret == -1:
        return error()
    return redirect(url)

#-----------------------------------------------------------------------------
# Signup
def signup():
    return template("Signup.tpl", server = conf.complete_server_conf())
#-----------------------------------------------------------------------------
# Signup Check
def signup_check(username, password, email):
    u_l = len(username)
    p_l = len(password)
    e_l = len(email)
    if u_l == 0 or p_l == 0 or e_l == 0:
        return error("One of the fields in the previous form was blank")
    result = studhelp_dbsql.check_signup(username, password)

    if (result == 0):
        studhelp_dbsql.add_user(username, password, email)
        return template("Login.tpl", server = conf.complete_server_conf())
    else:
        return template("SignupError.tpl", server = conf.complete_server_conf())

#-----------------------------------------------------------------------------
# Signup Error
def signup_error():
    return template("SignupError.tpl", server = conf.complete_server_conf())

#-----------------------------------------------------------------------------

def error(error):
    return template("ErrorPage.tpl", error = error)

#-----------------------------------------------------------------------------
# Unit Discussion

def listTopics(unit, username):
    title = studhelp_dbsql.get_all_post_title(unit)
    if title == -1:
        return error()
    url = 'homepage/'+ unit
    return template("UnitDiscussion.tpl", title = title, url=url, unit=unit, server = conf.complete_server_conf(), username=username)  

#-----------------------------------------------------------------------------
# Viewing each post, including title, content and responses

def content(subject, title, username):
    res = studhelp_dbsql.get_post_contents(subject, title)
    content = res
    if content == -3:
        return error()
    responses = studhelp_dbsql.get_post_responses(subject, title)
    if responses == -3:
        return error
    val = None
    for i in title:
        mod_i = ''.join(e for e in i if e.isalnum())
        for char in mod_i.lower():
            val = ord(char) - 96

    return template("topic.tpl", title = title, unit=subject, content=content, responses = responses, server = conf.complete_server_conf(), username = username, value = val)

#-----------------------------------------------------------------------------

def new_post(subject, title, content, username):
    if len(title) == 0 or len(content) == 0:
        return error("One title or content not written")        
    ret = studhelp_dbsql.add_new_post(username, subject, title, content)
    if ret == -3:
        return error()
    url = conf.complete_server_conf()+'/homepage/'+subject
    redirect(url)   
#-----------------------------------------------------------------------------

def new_comment(subject, title, comment, username):
    if len(comment) == 0:
        return error("Comment not written")
    ret = studhelp_dbsql.add_post_response(subject, title, comment, username)
    if ret == -3:
        return error()
    return content(subject, title, username)

#-----------------------------------------------------------------------------

def get_users(ret, username):
    users = []
    for row in ret:
        if row [1] != username:
            if row[1] not in users:
                users.append(row[1])
        if row[2] != username:
            if row[2] not in users:
                users.append(row[2])    
    return users

def overview_messages(username):
    ret = studhelp_dbsql.view_messages(username)
    if ret == -3:
        return error()
    users = []
    users = get_users(ret, username)
    return template("view_all_messages.tpl", username = username, users = users, server = conf.complete_server_conf())

#-----------------------------------------------------------------------------

def get_messages(username, chat_with):
    ret = studhelp_dbsql.view_chat_history(username, chat_with)
    if ret == -3:
        return error()
    return template("chat.tpl", chat = ret, reciever=chat_with, server= conf.complete_server_conf())

#-----------------------------------------------------------------------------

def new_message(sender, reciever, message):
    if len(message) == 0:
        return error("message not written")
    ret = studhelp_dbsql.add_message(sender, reciever, message)
    if ret == -3:
        return error()
    return get_messages(sender, reciever)
