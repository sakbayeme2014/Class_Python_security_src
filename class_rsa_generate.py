#!/usr/bin/env python

from Crypto.PublicKey import RSA
from Crypto import Random


class RSA_Randomize():
 def __init__(self, val1, val2):
  self.val1 = val1
  self.val2 = val2
 def random_file(self, random_object):
  self.random_object = random_object
 def rsa_file(self, rsa_object):
  self.rsa_object = rsa_object
 def file_open(self, file_object):
  self.file_object = file_object
 def file2_open(self, file2_object):
  self.file2_object = file2_object

xxx_object = RSA_Randomize("val1" , "val2")
xxx_object.random_file = Random.new().read
xxx_object.rsa_file = RSA.generate(4096, xxx_object.random_file)
xxx_object.file_open = open("/root/publickey.txt", "a+")
xxx_object.file_open = open("/root/publickey.txt", "wb")
xxx_object.file_open.write(xxx_object.rsa_file.publickey().exportKey())
xxx_object.file2_open = open("/root/privatekey.txt", "a+")
xxx_object.file2_open = open("/root/privatekey.txt", "wb")
xxx_object.file2_open.write(xxx_object.rsa_file.exportKey())
xxx_object.file_open = open("/root/publickey.txt", "rb")
xxx_object.file_open.read()
xxx_object.file2_open = open("/root/privatekey.txt", "rb")
xxx_object.file2_open.read()



