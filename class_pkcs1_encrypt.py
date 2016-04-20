#!/usr/bin/env python

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA

class PKCS1_v5_encrypt():
 def __init__(self, val1, val2):
  self.val1 = val1
  self.val2 = val2
 def file_open(self, file_object):
  self.file_object = file_object
 def cont_file(self, contents):
  self.contents = contents
 def key_file(self, key_object):
  self.key_object = key_object
 def hash_file(self, hash_object):
  self.hash_object = hash_object
 def encrypt_file(self, encrypt_object):
  self.encrypt_object = encrypt_object
 def file2_open(self, file2_object):
  self.file2_object = file2_object

xxx_object = PKCS1_v5_encrypt("val1" , "val2")
xxx_object.file_open = open("/root/crypt.txt", "rb")
xxx_object.cont_file = xxx_object.file_open.read()
xxx_object.key_file = RSA.importKey(open("/root/publickey.txt").read())
xxx_object.file2_open = open("/root/encrypt.txt", "a+")
xxx_object.file2_open = open("/root/encrypt.txt", "wb")
xxx_object.hash_file = SHA.new()
xxx_object.encrypt_file = PKCS1_v1_5.new(xxx_object.key_file)
xxx_object.file2_open.write(xxx_object.encrypt_file.encrypt(xxx_object.cont_file + xxx_object.hash_file.digest()))
xxx_object.file2_open = open("/root/encrypt.txt", "rb")
xxx_object.file2_open.read()


