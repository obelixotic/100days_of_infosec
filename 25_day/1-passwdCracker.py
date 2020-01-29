import crypt
import sys

def main():
	if len(sys.argv) == 3:
		passFile = open(sys.argv[1],'r')
		for line in passFile.readlines():
			if ":" in line:
				user = line.split(":")[0]
				cryptPass = line.split(":")[1].strip(' ')
				print "[*] Attempting to crack password for " + user
				testPass(cryptPass)
	else:
		print "please provide the following arguments:"
		print "1) name of file containing contents of /etc/shadow"
		print "2) name of file containing wordlist"

def testPass(cryptPass):
	salt = cryptPass[0:2]
	dictFile = open(sys.argv[2],'r')
	for line in dictFile.readlines():
		word = line.strip('\n')
		cryptWord = crypt.crypt(word, salt)
		if (cryptWord == cryptPass):
			print "[+] Found password: "+ word +"\n"
			return

	print "[-] Password not found\n"		


if __name__ == '__main__':
	main()