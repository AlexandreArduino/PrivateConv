import os
import sys
import socket
from lib import GetPublicIp, CheckInternetConnection
class PrivateConvServer(object):
	def __init__(self):
		if os.name == "posix": os.system('clear')
		elif os.name == "nt": os.system('cls')
		else: pass
		self.messages = []
		print("Checking Internet connection...")
		if not CheckInternetConnection():
			input("Unable to access to the Internet\nMake sure you are connected to it!\nPress enter to exit...")
			exit()
		else: pass
		print("Detecting auto-configuration...")
		if len(sys.argv) == 5:
			print("Launching auto-configuration...")
			print("Detecting Host Ip...")
			self.ip = str(sys.argv[1])
			print(self.ip + " will be used as Host Ip!")
			print("Detecting Host Port...")
			try:
				self.port = int(sys.argv[2])
				print(str(self.port) + " will be used as Host Port!")
			except:
				input(str(sys.argv[2]) + " is not a number!\nPress enter to restart the program and change the port...")
				exit()
			print("Detecting Number of Members maximum...")
			try:
				self.NumMembers = int(sys.argv[3])
				print(str(self.NumMembers) + " will be used as number of members maximum!")
			except:
				input(str(sys.argv[3]) + " is not a number!\nPress enter to restart the program and change this server...")
				exit()
			print("Detecting password...")
			self.password = str(sys.argv[4])
			if len(self.password) < 2:
				input("You password is too weak!Press enter to change it, then restart this program...")
				exit()
			else: print(self.password + " will be used as password for this value!")
		else:
			print("auto-configuration not permitted!")
			print("Setting up server...")
			print("Getting public IP...")
			self.ip = GetPublicIp()
			print("Ip : " + self.ip)
			print("Setting port...")
			self.port = 4567
			print("Port used : " + str(self.port))
			print("Setting number of members...")
			self.NumMembers = input("Number of members maximum >>> ")
			try: self.NumMembers = int(self.NumMembers)
			except:
				print("The value must be a number!")
				input("Press enter to exit then, restart this program...")
				exit()
			self.password = input("Please enter a password for this server >>> ")
			if len(self.password) < 2:
				input("Your password is too weak!\nPlease restart the program to enter a new password!\nPress enter to exit...")
				exit()
			else: pass
		print("Configuring the whole service...")
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.bind((self.ip, self.port))
		self.ShowServerInfos()
		print("Starting InfinityLoop...")
		self.InfinityLoop()
	def ShowServerInfos(self):
		print("Your server is ready!\nYou can talk with your friends without tracking, advertisements for free!")
		print("Here is the actually configuration you need to share to the members :\nIp adress : " + self.ip + "\nPort : " + str(self.port) + "\nPassword : " + self.password)
		print("Message from the developper : you can do what you want with this program except making it non-free. Please mention my name in it : BAALBAKY Alexandre :) Thanks! :p")
	def InfinityLoop(self):
		print("Press ctrl+c to stop the server.")
		while True:
			self.socket.listen(self.NumMembers)
			self.member, self.adrs = self.socket.accept()
			#print("A new member arrived !")
			self.response = self.member.recv(999999).decode()
			#print("Message from the member : " + str(self.response))
			self.ActionWithMessage()
			self.member.close()
	def ActionWithMessage(self):
		msg = list(self.response)
		del msg[0]
		del msg[len(msg)-1]
		msg = "".join(msg).split(",")
		if msg[1] == self.password:
			if msg[2] != '':
				self.messages.append(msg[0] + " >>> " + msg[2] + "\n")
				if len(self.messages) > 20: del self.message[0]
				else: pass
				self.member.send("".join(self.messages).encode())
			else: self.member.send("".join(self.messages).encode())
		else:
			self.member.send("Incorrect Password!".encode())
PrivateConvServer()
