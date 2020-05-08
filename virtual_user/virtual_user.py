from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome("./chromedriver")

def post_comp2022():
	browser.get("http://localhost:8080/homepage/COMP2022")
	time.sleep(1)
	browser.find_element_by_class_name("CreatePostBtn").click()
	title = browser.find_element_by_class_name("ttl")
	content = browser.find_element_by_class_name("txt")
	title.send_keys("This is virtual user's new post")
	time.sleep(3)
	content.send_keys("Hello COMP2022")
	time.sleep(3)
	browser.find_element_by_class_name("CreatePostBtn")
	post_btn = browser.find_elements_by_class_name("CreatePostBtn")
	count = 0
	for x in post_btn:
		if count == 1:
			x.click()
		count = 1
	time.sleep(3)

def add_comment_in_post(comment):
	post = browser.find_element_by_class_name("discuss_card").click()
	time.sleep(2)
	cmt = browser.find_element_by_class_name("comment")
	cmt.send_keys(comment)
	time.sleep(2)
	#submit
	browser.find_element_by_class_name("submit_btn").click()

	time.sleep(2)

def send_message(receiver, msg):
	browser.get("http://localhost:8080/messages")
	recipient = browser.find_element_by_class_name('bottomchat')
	message = browser.find_element_by_class_name('bottomchat')
	recipient.find_element_by_name("message_user").send_keys(receiver)
	time.sleep(2)
	message.find_element_by_name("message").send_keys(msg)
	time.sleep(2)
	browser.find_element_by_class_name("submit_btn").click()
	time.sleep(2)

def sign_up(usern, pwd, mail):
	browser.get("http://localhost:8080/sign-up")
	time.sleep(1)
	username = browser.find_element_by_class_name('mail')
	username.send_keys(usern)
	time.sleep(1)
	email = browser.find_element_by_class_name('pword')
	email.send_keys(mail)
	time.sleep(1)
	password = browser.find_element_by_class_name('e')
	password.send_keys(pwd)
	time.sleep(1)

	check_box_status = browser.find_element_by_id("myCheck").is_selected()
	time.sleep(1)
	# print(check_box_status)
	browser.find_element_by_id("myCheck").click()
	browser.find_element_by_id("button").click()
	time.sleep(1)

def log_in(usr, pwd):
	email = browser.find_element_by_class_name('email')
	password = browser.find_element_by_class_name('pword')
	email.send_keys(usr)
	time.sleep(1)
	password.send_keys(pwd)
	time.sleep(1)
	email.send_keys(Keys.ENTER)
	time.sleep(1)

def view_message():
	browser.get("http://localhost:8080/messages")
	browser.find_element_by_class_name("usrmsg").click()
	time.sleep(1)
	reply = browser.find_element_by_name("message")
	reply.send_keys("From virtual user")
	time.sleep(2)
	browser.find_element_by_class_name("submit_btn").click()
	pass

def full_traverse(usr, email, pwds):
	browser.get("http://localhost:8080/")
	time.sleep(1)
	#Sign up to existing account
	sign_up("admin", "admin@gmail.com", "admin123")
	browser.get("http://localhost:8080/sign-up")
	#Signup with proper account
	sign_up(usr, email, pwds)
	#Login with wrong username
	log_in("blah", pwds)
	browser.get("http://localhost:8080/signout")

	log_in(usr, pwds)
	nav = browser.find_element_by_class_name("topnav")
	nav.find_element_by_link_text("Unit").click()
	nav.find_element_by_link_text("Academic Dishonesty").click()
	select_here = browser.find_element_by_class_name("dropdown")
	time.sleep(1)
	drop_down = select_here.find_element_by_class_name("dropdown-content")
	time.sleep(1)
	nav.find_element_by_link_text("Signout").click()
	time.sleep(1)
	log_in("admin", "password")
	post_comp2022()
	add_comment_in_post("Commented by the virtual user")
	view_message()
	# Message needs to be fixed!
	# send_message("jackey", "hello")
	time.sleep(1)
	browser.get("http://localhost:8080/signout")
	time.sleep(2)
	browser.get("http://localhost:8080/forgot-password")




full_traverse("new_vr", "nvr@gmail.com", "nvrpassword")


	
