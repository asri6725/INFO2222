import sqlite3

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

def add_user(username, password):
	cursor.execute("INSERT INTO user_detail VALUES(?, ?, ?)", (username, password, 1))
	connection.commit()

#cursor.execute("INSERT INTO user_detail VALUES('jackey', 'password', 1)")
#connection.commit()

#cursor.execute("INSERT INTO user_detail VALUES('aa', 'bb')")