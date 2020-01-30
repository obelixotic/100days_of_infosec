import zipfile
from threading import Thread
import optparse

def extractFile(zFile,passTry):
    try:
        zFile.extractall(pwd=passTry)
        print "[+] Password found: " +passTry
        # return passTry
    except:
        pass

def main():
    parser = optparse.OptionParser("usage %prog -f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()

    if (options.zname == None or options.dname == None):
        print parser.usage
        exit(0)
    
    zFile = zipfile.ZipFile(options.zname)
    passFile = open(options.dname)

    print "Implementing dictionary attack to unzip evil.zip"
    print "Trying passwords from dictionary.txt"

    for line in passFile.readlines():
        passTry = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile,passTry))
        t.start()


if __name__ == '__main__':
    main()