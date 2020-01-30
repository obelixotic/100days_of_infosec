import zipfile

def extractFile(zFile,passTry):
    try:
        zFile.extractall(pwd=passTry)
        return passTry
    except:
        return

def main():
    print "Implementing dictionary attack to unzip evil.zip"
    print "Trying passwords from dictionary.txt"
    zFile = zipfile.ZipFile("evil.zip")
    passFile = open("dictionary.txt",'r')
    for line in passFile:
        passTry = line.strip('\n')
        guess = extractFile(zFile, passTry)
        if guess:
            print "[+] Password found: " +passTry
            print "file unzipped!"
            exit(0)
        else: 
            print "..."


if __name__ == '__main__':
    main()