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
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print "[-] " + filename + " does not exist."
			exit(0)
		if not os.access(filename, os.R_OK):
			print "[-] " + filename + ": access denied."
			exit(0)
		print "[+] Reading vulnerabilities from: " + filename
	
	portList = [21,22,25,80,110,443]
	for x in range(1,256):
		ip='xx.xx.xx.'+str(x)
		for port in portList:
			banner = retBanner(ip, port)
			print '[+] ' + ip + ':' + str(port) + ': ' + banner
			if 'timed out' not in banner and 'Err' not in banner:	
				checkVulns(banner, filename)
			

if __name__ == '__main__':
	main()