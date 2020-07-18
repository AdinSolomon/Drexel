# Adin Solomon - July 2020
# abs358@drexel.edu

import bcrypt
import time
import string

chars = string.ascii_lowercase

def findpw(digest):
	count = 1
	timing = time.time()
	for i in chars:
		for j in chars:
			if bcrypt.checkpw((i+j).encode(), digest):
				return [(i+j), count, (time.time() - timing) / 60]
			count += 1
	return ["", "", ""]

if __name__ == "__main__":
	print("Student ID, Password, Count, Timing")
	with open("student_pwd.txt", "r") as fileboi:
		for line in fileboi:
			student = line.strip().split(",")
			info = findpw(student[1].encode())
			print(student[0] + ", " + info[0] + ", " + str(info[1]) + ", " + str(info[2]))
