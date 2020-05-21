import time
import os
import threading

#REFERENCE https://www.youtube.com/watch?v=CzH3UPhKVgQ

#The code below should be implemented into the run.py


def check_ddos():
	file_name = 'ip_log.txt'
	banned = []
	unban_count = 0
	while True:
		unban_count += 1
		time.sleep(15)
		try:
			# print(banned)
			if unban_count == 4:
				if len(banned) != 0:
					for x in banned:
						os.system("iptables -D INPUT -s {} -j DROP".format(x))
						print("{} has been unbanned!".format(x))
						banned.remove(x)
					unban_count = 0
			# print(banned)

			e_list = []
			es_list = []
			os.system('netstat -an | grep :80 | sort > {}'.format(file_name))
			log_file = open(file_name, "r").read().split("\n")
			count = 0
			while count < len(log_file):
				log_file[count] = log_file[count][44:]
				count += 1
			count = 0
			while count < len(log_file):
				log_file[count] = log_file[count][:12]
				count += 1


			for x in log_file:
				count = 0
				if x not in es_list:
					es_list.append(x)
					e_list.append([x, 0])
				else:
					while count < len(e_list):
						if e_list[count][0] == x:
							e_list[count][1] += 1
						count += 1
						

			for x in e_list:
				if x[1] > 12:
					print("detected ddos attack from *{}*".format(x[0]))
					os.system("iptables -I INPUT -s {} -j DROP".format(x[0]))
					if x[0] not in banned:
						banned.append(x[0])
		except:
			print("some kind of error ")





#implment underneath main

t = threading.Thread(target = check_ddos)
t.start()


