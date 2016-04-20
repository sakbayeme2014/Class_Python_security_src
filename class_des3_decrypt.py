#!/usr/bin/env python

from Crypto.Cipher import DES3
import os
import sys

if len(sys.argv) <=2:
 print "Usage : ./class_des3_decrypt <encrypt_file.txt> < decrypt_file.txt>"
 exit()

class des3_decrypt():
 def __init__(self, val1, val2):
  self.val1 = val2
  self.val2 = val2
 def file_size(self, filesize):
  self.filesize = filesize
 def file_open(self, file_object):
  self.file_object = file_object
 def key_file(self, key_object):
  self.key_object = key_object
 def cont_file(self, contents):
  self.contents = contents
 def encrypt_file(self, encrypt_object):
  self.encrypt_object = encrypt_object
 def file1_open(self, file1_object):
  self.file1_object = file1_object

xxx_object = des3_decrypt("val1", "val2")
xxx_object.filesize = os.path.getsize("/root/python/creolink2.txt")
xxx_object.file_open = open("/root/python/creolink2.txt", "rb")
xxx_object.cont_file = xxx_object.file_open.read(xxx_object.filesize)
xxx_object.key_file = "\x00\x11\x22\x23\x25\x26\x01\x02\x03\x05\x00\x11\x11\x14\x15\x00"
xxx_object.encrypt_file = DES3.new(xxx_object.key_file, DES3.MODE_CFB)
xxx_object.file1_open = open("/root/python/creolink3.txt", "a+")
xxx_object.file1_open = open("/root/python/creolink3.txt", "wb")
xxx_object.file1_open.write(xxx_object.encrypt_file.decrypt(xxx_object.cont_file))
xxx_object.file1_open = open("/root/python/creolink3.txt", "rb")
xxx_object.file1_open.read()


