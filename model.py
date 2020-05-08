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
    result = studhelp_dbsql.check_login(username, password)

    if result == 0:
        #checking the units that the user chose and only showing them in the homepage
        subject = ['initial_value_subject']
        subject = studhelp_dbsql.get_user_subject(username)

        return template("homepage.tpl", name=username, subject=subject, server = conf.complete_server_conf())
    else:
        return template("LoginError.html", reason="check credentials")

#-----------------------------------------------------------------------------

def homepage(username):
    subject = ['initial_value_subject']
    subject = studhelp_dbsql.get_user_subject(username)
    print("Enter here")
    return template("homepage.tpl", name=username, subject=subject, server = conf.complete_server_conf())

'''#-----------------------------------------------------------------------------
#Creating new msg

#usernames: array of users who participate in this char
#message_name: is the naming of the chat.
def create_new_chat(usernames, message_name):
    #This creates new chat in the database, and return message_id
    message_id = studhelp_dbsql.create_new_message(usernames, message_name)

    #return something here?

#-----------------------------------------------------------------------------
#Retrieve Message
#Message_data: Array of tuples, ("Message content", "User who wrote the message")
#   E.g. [('hey jackey', 'admin'), ('hi admin', 'jackey'), ('how you doing admin?', 'jackey')]
def retrieve_message(message_id):

    messsage_data = studhelp_dbsql.get_message_contents(message_id)

    #return something

#-----------------------------------------------------------------------------
#Probaly after this function, retrieve_message should be called to update the contents
def add_message(username, message_id, content):
    studhelp_dbsql.add_new_msg(message_id, usernamem content)

    #return something


'''#-----------------------------------------------------------------------------

def addUnit(unit, username):
    #ADD unit to DB with the username and return homepage
    subject = studhelp_dbsql.unit_add(username, unit)
    return template("homepage.tpl", name=username, subject=subject, server = conf.complete_server_conf())

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
def signup_check(username, password, email):

    result = studhelp_dbsql.check_signup(username, password)

    if (result == 0):
        studhelp_dbsql.add_user(username, password, email)
        return template("Login.tpl", server = conf.complete_server_conf())
    else:
        return template("SignupError.html")

#-----------------------------------------------------------------------------
# Signup Error
def signup_error():
    return template("SignupError.html")

#-----------------------------------------------------------------------------

def error():
    return template("ErrorPage.html")

#-----------------------------------------------------------------------------
# Unit Discussion

def listTopics(unit, username):
    title = []
    title = studhelp_dbsql.get_all_post_title(unit)

    url = 'homepage/'+ unit
    return template("UnitDiscussion.tpl", title = title, url=url, unit=unit, server = conf.complete_server_conf(), username=username)  

#-----------------------------------------------------------------------------
# Viewing each post, including title, content and responses

def content(subject, title, username):
    res = studhelp_dbsql.get_post_contents(subject, title)
    content = res
    print(content)
    responses = studhelp_dbsql.get_post_responses(subject, title)
    val = None
    for i in title:
        mod_i = ''.join(e for e in i if e.isalnum())
        for char in mod_i.lower():
            val = ord(char) - 96

    return template("topic.tpl", title = title, unit=subject, content=content, responses = responses, server = conf.complete_server_conf(), username = username, value = val)

#-----------------------------------------------------------------------------

def new_post(subject, title, content, username):
    ret = studhelp_dbsql.add_new_post(username, subject, title, content)
    url = conf.complete_server_conf()+'/homepage/'+subject
    redirect(url)   
#-----------------------------------------------------------------------------

def new_comment(subject, title, comment, username):
    ret = studhelp_dbsql.add_post_response(subject, title, comment, username)
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
    users = []
    users = get_users(ret, username)
    return template("view_all_messages.tpl", username = username, users = users, server = conf.complete_server_conf())

#-----------------------------------------------------------------------------

def get_messages(username, chat_with):
    ret = studhelp_dbsql.view_chat_history(username, chat_with)
    return template("chat.tpl", chat = ret, reciever=chat_with, server= conf.complete_server_conf())

#-----------------------------------------------------------------------------

def new_message(sender, reciever, message):
    ret = studhelp_dbsql.add_message(sender, reciever, message)
    return get_messages(sender, reciever)