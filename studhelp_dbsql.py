
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
				return 0
			else:
				print("Wrong Password")
				return 1
	else:
		print("Wrong username")
		return 2

#Return 0 for success
#Return 1 for existing username
def check_signup(username, password):
	cursor.execute("SELECT * FROM user_detail")
	data = cursor.fetchall()
	for record in data:
		if (username == record[0]):
			return 1
	else:
		return 0

def get_user_subject(username):

	subjects = []
	count = 0

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
	
	return subjects

#Return -1 when user is already enrolled in the unit
def unit_add(username, unit):
	
	subjects = get_user_subject(username)
	
	for subject in subjects:
		if subject == unit:
			return subjects

	cursor.execute("INSERT INTO user_subject VALUES(?, ?)", (username, unit))
	connection.commit()

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

	return 0

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
	return data

def get_post_contents(subject, title):

	cursor.execute("""
		SELECT P.title, P.subject_id, P.context
		FROM post P
		WHERE P.title = :title AND P.subject_id = :subject_id
		""", {"title": title, "subject_id": subject})
	data = cursor.fetchall()
	if len(data) == 0:
		return [("This post does not exist")]
	return data[0]

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
		return ["Response does not exist"]
	return data

def add_post_reponses(postID, message):
	cursor.execute("""
		SELECT R.response, R.username
		FROM post_repose PR INNER JOIN Response R
		WHERE PR.post_id = :post_id
		""", {"post_id": postID})
	data = cursor.fetchall()
	if len(data) == 0:
		return ["Response does not exist"]
	return data


def add_new_post(username, subject, title, content):
	cursor.execute("SELECT MAX(post_id) FROM post")
	data = cursor.fetchall()
	p_id = data[0][0]+1
	cursor.execute("INSERT INTO post VALUES(?, ?, ?, ?, ?)", (p_id, title, content, username, subject))
	connection.commit()
	return 0

def add_user(username, password, email):
	cursor.execute("INSERT INTO user_detail VALUES(?, ?, ?, ?)", (username, password, 1, email))
	connection.commit()
	return 0

def send_password(username):

	mail = None
	password = None

	cursor.execute("""
		SELECT U.email, U.password
		FROM user_detail U
		WHERE U.username = :username
		""", {"username": username})

	data = cursor.fetchall()
	mail = data[0][0]
	password = data[0][1]

	if (mail == None or password == None):
		return -1

	mf = "studhelp_info@gmail.com"
	rt = mail
	subject = "Password Recover from StudHelp"
	f = "studhelp <studhelp_info@gmail.com"
	t = username + " <" + mail + ">"
	context = "Hello, - - Your password is : " + password + ". -"
	context_list = context.split("-")

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
	return 0

