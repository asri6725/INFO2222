import sqlite3
import base64
from socket import *
import sys


connection = sqlite3.connect("stud_help.db")
cursor = connection.cursor()

#Return 0 for correct login credentials
#Return 1 for incorrect password
#Return 2 for incorrect username
def check_login(username, password):
	cursor.execute("SELECT * FROM user_detail")
	data = cursor.fetchall()
	for record in data:
		if (username == record[0]):
			if (password == record[1]):
				print("Correct password, now login")
				connection.close()
				return 0
			else:
				print("Wrong Password")
				connection.close()
				return 1
	else:
		print("Wrong username")
		connection.close()
		return 2

#Return 0 for success
#Return 1 for existing username
def check_signup(username, password):
	cursor.execute("SELECT * FROM user_detail")
	data = cursor.fetchall()
	for record in data:
		if (username == record[0]):
			connection.close()
			return 1
	else:
		connection.close()
		return 0

#This function get all the subject that user has selected
def get_user_subject(username):

	subjects = []
	count = 0

	#Search for all id user has selected
	cursor.execute("""
		SELECT S.subject_id
		FROM user_detail UD INNER JOIN user_subject US USING(username) INNER JOIN subject S USING(subject_id)
		WHERE UD.username = :username
		ORDER BY S.subject_id
		""", {"username": username})
	data = cursor.fetchall()
	if (len(data) == 0):
		subjects = ["Not Initalised"]
	else:
		for record in data:
			subjects.append(record[0])
			count += 1
	connection.close()
	return subjects

#Adds selected unit to the user
#Return -1 when user is already enrolled in the unit
def unit_add(username, unit):
	
	subjects = get_user_subject(username)
	
	for subject in subjects:
		if subject == unit:
			return subjects

	cursor.execute("INSERT INTO user_subject VALUES(?, ?)", (username, unit))
	connection.commit()
	connection.close()

	return get_user_subject(username)

#users: Array of username that are part of the chat
#message_name: Name of the chat
def create_new_message(users, message_name):

	cursor.execute("INSERT INTO message (message_name) VALUES(?)", (message_name,))
	connection.commit()
	for user in users:
		cursor.execute("SELECT MAX(message_id) FROM message")
		data = cursor.fetchall()
		m_id = data[0][0]
		cursor.execute("INSERT INTO message_user VALUES (?, ?)", (m_id, user))
		connection.commit()
	connection.close()

	return m_id

#m_id: message_id
#return example: [('hey jackey', 'admin'), ('hi admin', 'jackey'), ('how you doing admin?', 'jackey')]
def get_message_contents(m_id):

	message_his = []
	count = 0

	command = """
		SELECT M.content, M.username
		FROM message_content M
		WHERE M.message_id = {}
		ORDER BY M.content_id""".format(m_id)
	cursor.execute(command)
	data = cursor.fetchall()
	connection.close()
	return data

#Adds new messsage from the user
def add_new_msg(m_id, username, content):

	cursor.execute("INSERT INTO message_content (message_id, content, username) VALUES (?, ?, ?)", (m_id, content, username))
	connection.commit()
	connection.close()

#Returns -1 there is no post in this subject
#Otherwise return array of tuples containing information
#	E.g. [(1, 'how to make websites?', 'admin')]
def get_pid_title_username(subject):

	cursor.execute("""
		SELECT post_id, title, username
		FROM post
		WHERE subject_id = :subject_id
		""", {"subject_id": subject})
	data = cursor.fetchall()
	if len(data) == 0:
		connection.close()
		return -1
	connection.close()
	return data

def get_post_contents(subject, title):

	cursor.execute("""
		SELECT P.title, P.subject_id, P.context
		FROM post P
		WHERE P.title = :title AND P.subject_id = :subject_id
		""", {"title": title, "subject_id": subject})
	data = cursor.fetchall()
	if len(data) == 0:
		connection.close()
		return [("This post does not exist")]
	connection.close()
	return data[0]

#New version
# def get_post_contents(post_id):
# 	cursor.execute("""
# 		SELECT P.title, P.subject_id, P.context
# 		FROM post P
# 		WHERE P.post_id = :post_id""", {"post_id": post_id})
# 	data = cursor.fetchall()
# 	if len(data) == 0:
# 		return [("This post does not exist")]
# 	return data[0]

#Gets an array of all the post_title in the unit
def get_all_post_title(unit):
	cursor.execute("""
		SELECT P.title
		FROM post P
		WHERE subject_id = :subject_id
		ORDER BY P.post_id""", {"subject_id": unit})
	data = cursor.fetchall()

	title = []
	for record in data:
		title.append(record[0])
	connection.close()
	return title

def get_post_responses(subject, title):
	cursor.execute("""
		SELECT R.response, R.username
		FROM post P INNER JOIN post_response PR USING (post_id) INNER JOIN response R USING (response_id)
		WHERE P.title = :title AND P.subject_id = :subject_id
		ORDER BY PR.response_id
		""", {"title": title, "subject_id":subject})
	data = cursor.fetchall()
	if len(data) == 0:
		connection.close()
		return ["Response does not exist"]
	connection.close()
	return data

#new version
# def get_post_response(post_id):
# 	cursor.execute("""
# 		SELECT R.response, R.username
# 		FROM post P INNER JOIN post_response PR USING (post_id) INNER JOIN response R USING (response_id)
# 		WHERE PR.post_id = :post_id
# 		ORDER BY PR.response_id""", {"post_id": post_id})
# 	data = cursor.fetchall()
# 	if len(data) == 0:
# 		return ["Response does not exist"]
# 	return data



def add_post_response(unit, title, content, username):
	cursor.execute("""
		SELECT P.post_id
		FROM post P
		WHERE P.subject_id = :subject_id AND P.title = :title
		""", {"subject_id": unit, "title": title})
	data = cursor.fetchall()
	post_id = int(data[0][0])

	cursor.execute("INSERT INTO response (response, username) VALUES(?, ?)", (content, username))
	connection.commit()
	cursor.execute("""
		SELECT MAX(response_id)
		FROM response""")
	data = cursor.fetchall()
	response_id = int(data[0][0])
	cursor.execute("INSERT INTO post_response VALUES(?, ?)", (post_id, response_id))
	connection.commit()
	connection.close()


def add_new_post(username, subject, title, content):
	cursor.execute("INSERT INTO post (title, context, username, subject_id) VALUES(?, ?, ?, ?)", (title, content, username, subject))
	connection.commit()
	connection.close()
	return 0


def add_user(username, password, email):
	cursor.execute("INSERT INTO user_detail VALUES(?, ?, ?, ?)", (username, password, 1, email))
	connection.commit()
	connection.close()
	return 0

#Sends an email to the users with their password
def send_password(mail):

	#looks up username and password, related to this email
	cursor.execute("""
		SELECT U.password, U.username
		FROM user_detail U
		WHERE U.email = :email
		""", {"email": mail})

	data = cursor.fetchall()
	password = data[0][0]
	username = data[0][1]


	if (mail == None or password == None):
		return -1

	mf = "studhelp_info@gmail.com"
	rt = mail
	subject = "Password Recover from StudHelp"
	f = "studhelp <studhelp_info@gmail.com"
	t = username + " <" + mail + ">"
	context = "Hello, - - Your password is : " + password + ". -"
	context_list = context.split("-")

	#Connects to uni mail server to send a msg

	cc = socket(AF_INET, SOCK_STREAM)
	cc.connect(("mail.usyd.edu.au", 25))
	print(cc.recv(1024).decode())

	cc.send(("MAIL FROM: <" + mf + ">" + "\r\n").encode())
	print(cc.recv(1024).decode())
	cc.send(("RCPT TO: <" + rt + ">" + "\r\n").encode())
	print(cc.recv(1024).decode())
	cc.send(("DATA" + "\r\n").encode())
	print(cc.recv(1024).decode())

	cc.send(("Subject: " + subject + "\r\n").encode())
	cc.send(("From: " + f + "\r\n").encode())
	cc.send(("To: " + t + "\r\n").encode())
	count = 0
	while count < len(context_list): 
	    cc.send((context_list[count] + "\r\n").encode())
	    count += 1
	cc.send("\r\n.\r\n".encode())
	print(cc.recv(1024).decode())

	connection.close()
	return 0

def add_message(usr_from, user_to, message):
	cursor.execute("SELECT max(message_id) from messages_final;")
	data = cursor.fetchall()
	m_id = data[0][0]+1
	cursor.execute("INSERT INTO messages_final VALUES(?, ?, ?, ?)", (m_id, usr_from, user_to, message))
	connection.commit()
	connection.close()
	return 0

def view_messages(username):
	cursor.execute("SELECT * FROM messages_final WHERE sender= :username OR reciever= :username ORDER BY message_id;", {"username": username})
	data = cursor.fetchall()
	connection.close()
	return data

def view_chat_history(username1, username2):
	cursor.execute("SELECT * FROM messages_final WHERE (sender = :user1 AND reciever = :user2) OR (sender = :user2 AND reciever = :user1) ORDER BY message_id;", {'user1':username1, "user2": username2})
	data = cursor.fetchall()
	connection.close()
	return data


