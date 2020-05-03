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
	
	subjects = get_user_subject(username);
	
	for subject in subjects:
		if subject == unit:
			return subjects

	cursor.execute("INSERT INTO user_subject VALUES(?, ?)", (username, unit));
	connection.commit()

	return get_user_subject(username)

def get_post_contents(subject, title):

	cursor.execute("""
		SELECT P.title, P.subject_id, P.context
		FROM post P
		WHERE P.title = :title AND P.subject_id = :subject_id
		""", {"title": title, "subject_id": subject})
	data = cursor.fetchall()
	return data[0]
	# print(data[0])

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

def add_new_post(username, subject, title, content):
	cursor.execute("INSERT INTO post VALUES(?, ?, ?, ?)", (title, content, username, subject))
	connection.commit()
	return 0

def add_user(username, password):
	cursor.execute("INSERT INTO user_detail VALUES(?, ?, ?)", (username, password, 1))
	connection.commit()
	return 0

