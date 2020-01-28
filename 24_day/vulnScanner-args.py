import sys
import os
import socket

def retBanner(ip, port):
	try:
		socket.setdefaulttimeout(1)
		s = socket.socket()
		s.connect((ip, port))
		banner = s.recv(1024)
		return banner
	except Exception, e:
		return str(e)

def checkVulns(banner, filename):
	f = open(filename, 'r')
	for line in f.readlines():
		if line.strip('\n') in banner:
			print "[+] Server is vulnerable: " + banner.strip('\n')

def main():

	if len(sys.argv) < 4:
		print "You have not provided enough arguments. Please provide the following arguments :"
		print "1) mode - 1 for scanning a single IP or 2 for a range"
		print "2) IP - for mode 1, mention an IP address; for mode 2 mention the first 24 bits/3 groups of an IP address"
		print "3) filename - a vuln banner file name to compare the scanned the IP/port banners against"
		exit(0)

	elif len(sys.argv) == 4:
		portList = [21,22,25,80,110,443]
		filename = sys.argv[3]
		if not os.path.isfile(filename):
			print "[-] " + filename + " does not exist."
			exit(0)
		if not os.access(filename, os.R_OK):
			print "[-] " + filename + ": access denied."
			exit(0)
		print "[+] Reading vulnerabilities from: " + filename

		if sys.argv[1] == '2':
			for x in range(1,256):
				ip = sys.argv[2]+'.'+str(x)
				for port in portList:
					banner = retBanner(ip, port)
					print '[+] ' + ip + ':' + str(port) + ': ' + banner
					if 'timed out' not in banner and 'Err' not in banner:	
						checkVulns(banner, filename)

		elif sys.argv[1] == '1':
			ip = sys.argv[2]
			for port in portList:
				banner = retBanner(ip, port)
				print '[+] ' + ip + ':' + str(port) + ': ' + banner
				if 'timed out' not in banner and 'Err' not in banner:	
					checkVulns(banner, filename)
	
	elif len(sys.argv) > 4:
		print "You have provided too many arguments. Please provide the following arguments :"
		print "1) mode - 1 for scanning a single IP or 2 for a range"
		print "2) IP - for mode 1, mention an IP address; for mode 2 mention the first 24 bits/3 groups of an IP address"
		print "3) filename - a vuln banner file name to compare the scanned the IP/port banners against"
		exit(0)



if __name__ == '__main__':
	main()