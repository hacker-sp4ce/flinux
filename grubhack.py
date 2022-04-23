#import modules:
import os
import getpass

#checking for root access
checkroot = (getpass.getuser())
if checkroot == 'root':

	#banner:
	print('\033[31m' + '''
	┏━━━┳━━━┳┓╋┏┳━━┓╋┏┓╋┏┳━━━┳━━━┳┓┏━┓
	┃┏━┓┃┏━┓┃┃╋┃┃┏┓┃╋┃┃╋┃┃┏━┓┃┏━┓┃┃┃┏┛
	┃┃╋┗┫┗━┛┃┃╋┃┃┗┛┗┓┃┗━┛┃┃╋┃┃┃╋┗┫┗┛┛
	┃┃┏━┫┏┓┏┫┃╋┃┃┏━┓┃┃┏━┓┃┗━┛┃┃╋┏┫┏┓┃
	┃┗┻━┃┃┃┗┫┗━┛┃┗━┛┃┃┃╋┃┃┏━┓┃┗━┛┃┃┃┗┓
	┗━━━┻┛┗━┻━━━┻━━━┛┗┛╋┗┻┛╋┗┻━━━┻┛┗━┛ By OverBafer1
	''') 

	#search file:
	filegrub = input('\033[35m' + 'Where is the "grub.cfg" file located? Аull path to the file: ' + '\033[31m')
	if os.path.isfile(filegrub):
		print('\033[31m' + 'The file is detected. Creating a backup')
		os.system('sudo cp ' + filegrub + ' backupfile')
		print('\033[35m' + '\nDelete password?')
		confirmation = input('\033[31m' + '[ENTER]')
		os.system('sudo sed -i "s/set superusers/#set superusers/" ' + filegrub)
		os.system('sudo sed -i "s/password_pbkdf2/#password_pbkdf2/" ' + filegrub)
		print('\nDone!')
		
	else:
		print('\033[31m' + 'File Not Found!')
else:
	print('\033[31m' + 'ERROR: permission denied | Proper launch: sudo python3 grubhack.py')

