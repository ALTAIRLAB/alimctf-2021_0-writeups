class Xeon:
	def __init__(self):
		self.name = "XEON"
		self.password = "alimCTF{}"

	def set_name(self, name):
		self.name = name

	def get_name(self):
		return self.name

	def check_password(self, psswd):
		return psswd == "n30_d03s_n0t_kn0w_pyth0n"

if __name__ == "__main__":
	password = input("Enter Xeon password:")
	xeon = Xeon()
	if (xeon.check_password(password[8:len(password)-1])):
		print("Access granted!")
	else:
		print("Acces denied!")
