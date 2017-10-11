credentials = {}

def login():
	print('Username:')
	username = input()

	print('Password:')
	password = input()

	if (username in credentials) == False:
		print('Unknown user!')
	elif password == credentials[username]:
		print('Success!')
	else:
		print('You are a fraudster!')

def newUser():
	print('Username:')
	username = input()

	print('Password:')
	password = input()

	credentials[username] = password

	print('Welcome!')

def deleteUser():
	print('Username:')
	username = input()

	print('Password:')
	password = input()

	if (username in credentials) == False:
		print('Unknown user!')
	elif password == credentials[username]:
		print('Deleting user!')
		del credentials[username]
	else:
		print('You are a fraudster!')
	
while True:
	command = input()
	if command == 'login':
		login()
	elif command == 'new':
		newUser()
	elif command == 'delete':
		deleteUser()
	elif command == 'exit':
		exit()
	else:
		print('Unknown command')