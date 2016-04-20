#!/usr/bin/env python

import pyaes
import os
import sys

if len(sys.argv) <=2:
 print "Exemple Usage : ./class_cbc_encrypt_feeder.py <Original_file.txt> <Encrypted_file.txt>"
 print "Exemple Usage : ./class_cbc_encrypt_feeder.py </home/original_file.txt> </home/encrypt_file.txt>"            
 exit()

class pyaes_encrypt_feeder():
 def __init__(self, val1, val2):
  self.val1 = val1
  self.val2 = val2
 def file_size(self, filesize):
  self.filesize = filesize
 def key_file(self, keyfile):
  self.keyfile = keyfile
 def file_open(self, file_object):
  self.file_object = file_object
 def cont_file(self, contents):
  self.contents = contents
 def encrypt_file(self, object_encrypt):
  self.object_encrypt = object_encrypt
 def file2_open(self, file2_object):
  self.file2_object = file2_object
 
xxx_object = pyaes_encrypt_feeder("val1" , "val2")
xxx_object.file_size = os.path.getsize(sys.argv[1])
xxx_object.key_file = "\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x01\x01"
xxx_object.file_open = open(sys.argv[1])
xxx_object.cont_file = xxx_object.file_open.read(xxx_object.file_size)
xxx_object.encrypt_file = pyaes.Encrypter(pyaes.AESModeOfOperationCBC(xxx_object.key_file, "this is an IV456"))
xxx_object.file2_open = open(sys.argv[2], "a+")
xxx_object.file2_open = open(sys.argv[2], "wb")
xxx_object.file2_open.write(xxx_object.encrypt_file.feed(xxx_object.cont_file))
xxx_object.file2_open = open(sys.argv[2], "rb")
xxx_object.file2_open.read()



  


