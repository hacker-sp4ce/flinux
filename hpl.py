#importing modules:
import os
import getpass
import time
import os.path

#checking for root access
checkroot = (getpass.getuser())
if checkroot == 'root':

	#banner:
	print('\033[31m' + '''
╭╮╱╭┳━━━┳╮
┃┃╱┃┃╭━╮┃┃
┃╰━╯┃╰━╯┃┃
┃╭━╮┃╭━━┫┃╱╭╮
┃┃╱┃┃┃╱╱┃╰━╯┃
╰╯╱╰┻╯╱╱╰━━━╯ (Hacking Passwords in Linux) By OverBafer1
	''' + '\033[33m')

	#text printing effect:
	txt = 'Hello friend!'
	for i in txt:  
	    time.sleep(0.1)
	    print(i, end='', flush=True)

	#contacts:
	print('\033[31m' + '\n.......................')

	#User and file Search:
	fileshadow = input('\033[32m' + 'Specify the location of the file with password hashes: ' + '\033[33m')

	if os.path.isfile(fileshadow):

		user = input('\033[32m' + 'Enter username to reset your password: ' + '\033[33m')
		
		#creating a backup:
		print('Creating a backup... (FileName: BackupFileByHPL)')
		os.system('sudo cp -r ' + fileshadow + ' BackupFileByHPL')

		#printhashes:
		print('\nHashes: '+ '\033[32m')
		os.system('sudo grep -w -n ' + user + ' ' + fileshadow)
		numberhash = input('\033[32m' + '\nPlease select a hash number: ' + '\033[33m')
		
		#deletepassword:
		print('The password will be deleted and a new one will be added. Make sure you have entered the correct data.')
		input('\033[32m' + '[ENTER]' + '\033[33m')
		print('\nPassword deletion...')
		os.system('sudo sed -i "' + numberhash + 'd" ' + fileshadow)
		
		#newpassword:
		print('\033[31m' + '\n---------------------------' + '\033[33m')
		print('Hash of the new password:' + '\033[32m')
		os.system('sudo sed "s/userbyhackpasswordinlinux/' + user + '/" ./pass')
		os.system('sudo sed -i "1r pass" '+ fileshadow)
		os.system('sudo sed -i "s/userbyhackpasswordinlinux/' + user + '/" ' + fileshadow)
		print('\033[33m' + 'your new password: ' + '\033[32m' + 'qwerty' + '\033[31m')
		print('-----------------------------')
		print('\033[33m' + '\nBackup file: BackupFileByHPL' + '\033[0m')

	#if the file is not found:
	else:
    		print ("File not found")

#if there are no superuser rights:
else:
	print('\033[31m' + 'ERROR: permission denied | Proper launch: sudo python3 hpl.py')


