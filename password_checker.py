import re


def password_is_valid(password):
	for pass_word in password:

		if len(pass_word) < 8:
			print("FAILURE Password must be atleast 8 characters in_length")
			continue
		if len(pass_word) == 0
			print("FAILURE Enter Password")
			continue
		elif not re.search("[A-Z]", pass_word):
			print("Failure Password should contain atleast 1 uppercase character")
		elif not re.search("[a-z]", pass_word):
			print("Failure Password should contain atleast 1 lowecase character")
		elif not re.search("[0-9]", pass_word):
			print("Failure Password should contain atleast 1 number")

		else:
			print("Good Password")




	