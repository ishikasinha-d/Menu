import os
import getpass

os.system("tput setaf 3")
print("\t\t\twelcome to docker menu.")
os.system("tput setaf 7")
print("\t\t............................................")

passwd = getpass.getpass("Enter your password: ")

if passwd != "arth":
	print("Incorrect password!!!")
	exit()

while True:

	os.system("clear")

	print('''1. to start docker service
2. info of docker
3. see all images of os 
4. to check running os
5. to launch an os
0. to exit''')
	query = int(input("Choose one option: "))

	if query == 1:
		os.system("systemctl start docker")
		os.system("systemctl enable docker")

	elif query == 2:
		os.system("docker info")

	elif query == 3:
		os.system("docker images")

	elif query == 4:
		os.system("docker ps")

	elif query == 5:
		image = input("enter image and its version: ")
		os.system("docker run -it {}".format(image))

	elif query == 0:
		os.system("clear")
		exit()

	else:
		print("invalid choice")
	
	input("press Enter to continue.")
  
  
