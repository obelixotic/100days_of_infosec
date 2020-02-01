#!/usr/bin/python

import sys
from word2number import w2n

try:
    from pwn import *
except ImportError:
    print "In order to complete this challenge, please install pwntools"
    print "https://pwntools.readthedocs.io/en/stable/install.html"
    sys.exit(1)

def word2number(data):
  data_ = []
  for i in range(len(data)):
    data_.append(str(w2n.word_to_num(data[i])))

  s = ""
  num = s.join(data_)
  return int(num)


def processResponse(math_prob):
    char = math_prob.split(' ')
    # print(char)
    
    try:
      try:
        a = int(char[0])
      except:
        a = char[0].split('-')
        a = word2number(a)
    except:
      a = int(char[0],0)

    try:
      try:
        b = int(char[2])
      except:
        b = char[2].split('-')
        b = word2number(b)
    except:
      b = int(char[2],0)

    # print a,b
    if(char[1] == '*'):
      print a*b
      return a*b
    if(char[1] == '+'):
      print a+b
      return a+b
    if(char[1] == '-'):
      print a-b
      return a-b
    else:
      print a/b
      return a/b

def pwn(address, port):
    connection = remote(address, port)
    print connection.recvuntil(":")
    connection.sendline("tg1799")
    print connection.recvuntil("??\n")
    for i in range(1000):
      try:
        math_prob = connection.recvuntil("= ?\n")
        print math_prob
        connection.sendline(str(processResponse(math_prob)))
        print connection.recvuntil("!\n")
      except:
        print connection.recv()
        exit(0)

def main():
    #try:
        #address = sys.argv[1]
        #port = sys.argv[2]
    #except IndexError:
        #print "Usage: ./client.py [IP] [Port]"
        #sys.exit(1)
    # pwn('recruit.osiris.cyber.nyu.edu', 1279)
    pwn('offsec-chalbroker.osiris.cyber.nyu.edu', 1236)

if __name__ == "__main__":
    main()

