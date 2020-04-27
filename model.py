import random
from bottle import template, error
import studhelp_dbsql

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
users = {1:{'user':'admin',
             'password': 'password',
             'subject':['math2068','info2222']            
            },
        2:{
            'user':'abhi',
            'password': '123',
            'subject': ['data3404','info2222']
        } }

#Discussion table

discussion = {
    'info2222':{
        1:{
            'title':'how to make websites?',
            'content': 'I want to learn how to make websites',
            'responses':{
                'abhi':'Just learn html, css and javascript',
                'admin': 'it is easy! definitely have a go with html',
            }
        },
        2:{
            'title':'I have a doubt with loading JavaScript',
            'content': 'How to use the window object?',
            'responses':{
                'admin':'Call the variables with "window.<something>"',
            },
        },
    },
    'math2068':{
        1:{
            'title':'How can we crack SHA encryption',
            'content': 'Why is it computationally not possible to do so?',
            'responses':{
                'abhi':'I dunno',
                'admin': 'it is easy! ',
            }
        },
        2:{
            'title':'What is diffie helman method of encryption?',
            'content': 'How to use the window object?',
            'responses':{
                'admin':'It can be used to generate secret keys between 2 users',
            },
        },
    },
    'comp2022':{
        1:{
            'title':'What are NP hard problems',
            'content': 'I do not know what NP means',
            'responses':{
                'abhi':'Non Polynomial time complexity',
                'admin': 'What he said^',
            }
        },
        2:{
            'title':'What is dynamic programming?',
            'content': 'I dont really understand it',
            'responses':{
                'admin':'It is a style that basically saves some computation to reduce time',
            },
        },
    },
}


#-----------------------------------------------------------------------------
# Login

def login():
    return template('Login.html')

#-----------------------------------------------------------------------------
# Check the login credentials

def login_check(username, password): 
    result = studhelp_dbsql.check_login(username, password)

    if result == 0:
        #checking the units that the user chose and only showing them in the homepage
        subject = ['initial_value_subject']
        global users
        for i in users:
            if users[i]['user']== username:
                subject = users[i]['subject']

        return template("homepage.tpl", name=username, subject=subject)
    else:
        return template("LoginError.html", reason="check credentials")

#-----------------------------------------------------------------------------

def addUnit(unit_add, username):
    #ADD unit to DB with the username and return homepage
    global users
    subject = ['not initialised']
    print(username, unit_add)
    for i in users:
        if users[i]['user']== username:
            print(username, unit_add)
            users[i]['subject'].append(unit_add)
            subject = users[i]['subject']
            print(subject)
    
    return template("homepage.tpl", name=username, subject=subject)

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

    result = studhelp_dbsql.check_signup(username, password)

    if (result == 0):
        studhelp_dbsql.add_user(username, password)
        return template("Login.html")
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

def listTopics(unit):
    title = []
    global discussion
    for i in discussion[unit]:
        title.append(discussion[unit][i]['title'])
    
    print(title)
    return template("UnitDiscussion.tpl", title = title, unit=unit)

#-----------------------------------------------------------------------------
# Viewing each post, including title, content and responses

def content(subject, title):
    
    global discussion
    content = None
    responses = {}
    for i in discussion[subject]:  #itreate the subjects (from signature) content looking for title (from signature), returning that, it's content and responses
        title_check = ''.join(e for e in discussion[subject][i]['title'] if e.isalnum()) 
        if title == title_check:
            content = discussion[subject][i]['content']
            responses = discussion[subject][i]['responses']
            title_normal = discussion[subject][i]['title']
       
    return template("topic.tpl", title = title_normal, unit=subject, content=content, responses = responses)

#-----------------------------------------------------------------------------
