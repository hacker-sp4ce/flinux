# flinux
Hack Password in Linux and hack hack password from grub.



DISCLAIMER:
The author is not responsible for your actions and does not develop to offenses.
All information is provided for informational purposes only.



This is a universal set of tools for exploiting Linux and Grub vulnerabilities.



HPL Using:
1. Running from a live distribution. You can use most distributions for this as long as you have root. I will use kali linux.
2. Open the disk partition with the system from which you want to crack the password.
3. Copying the Path.
4. Launch a terminal as root and download the repository:
git clone https://github.com/hacker-sp4ce/hpl/
cd hpl
python3 hpl.py
5. The program will ask you for the path to the hash file. On Linux, the hash file is located on the path "/etc/shadow", so in the program you need to go to the /etc/shadow system partition.
6. The program will ask you to enter the full name of the user you want to reset the password from.
7. If the file is found and the username is entered correctly, it will display the credentials.
8. Enter the displayed credential number.
9. Confirm hash replacement by pressing Enter.
10. Ready! Now you can restart your computer and log in with a new password!

Password: qwerty



Grub Hack Using:
1. Running from a live distribution. You can use most distributions for this as long as you have root. I will use kali linux.
2. Open the disk partition with the system from which you want to crack the password.
3. Copying the Path.
4. Launch a terminal as root and download the repository:
git clone https://github.com/hacker-sp4ce/hpl/
cd hpl
python3 hpl.py
5. The program will ask you for the path to the hash file. On Linux, the hash file is located on the path "/boot/grub/grub.cfg", so in the program you need to go to the /etc/shadow system partition.
6. If the file is found, it will display the credentials.
7. Confirm the deletion of the hash by pressing Enter.
9. Done! Now you can restart your computer and log in without a password!
