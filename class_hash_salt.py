#!/usr/bin/env python

import hashlib
import uuid
import sys

if len(sys.argv) <= 1:
 print "Usage : ./class_hash_salt.py <password>"
 exit()

class md5():
 def __init__(self, password, hashing):
  self.password = password
  self.hashing = hashing
 def pass_file(self, password):
  self.password = password
 def hash_file(self, hashing):
  self.hashing = hashing
  return pass_object.hash_file
 def salt_file(self, salt):
  self.salt = salt

class sha1():
 def __init__(self, password1, hashing1):
  self.password1 = password1
  self.hashing1 = hashing1
 def pass_file1(self, password1):
  self.password1 = password1
 def hash_file1(self, hashing1):
  self.hashing1 = hashing1
 def salt_file1(self, salt1):
  self.salt1 = salt1

class sha224():
 def __init__(self, password2, hashing2):
  self.password2 = password2
  self.hashing2 = hashing2
 def pass_file2(self, password2):
  self.password2 = password2
 def hash_file2(self, hashing2):
  self.hashing2 = hashing2
 def salt_file2(self, salt2):
  self.salt2 = salt2
 
class sha256():
 def __init__(self, password3, hashing3):
  self.password3 = password3
  self.hashing3 = hashing3
 def pass_file3(self, password3):
  self.password3 = password3
 def hash_file3(self, hashing3):
  self.hashing3 = hashing3
  return pass_object3.hash_file3
 def salt_file3(self, salt3):
  self.salt3 = salt3

class sha384():
 def __init__(self, password4, hashing4):
  self.password4 = password4
  self.hashing4 = hashing4
 def pass_file4(self, password4):
  self.password4 = password4
 def hash_file4(self, hashing4):
  self.hashing4 = hashing4
 def salt_file4(self, salt4):
  self.salt4 = salt4

class sha512():
 def __init__(self, password5, hashing5):
  self.password5 = password5
  self.hashing5 = hashing5
 def pass_file5(self, password5):
  self.password5 = password5
 def hash_file5(self, hashing5):
  self.hashing5 = hashing5
 def salt_file5(self, salt5):
  self.salt5 = salt5

pass_object = md5("password", "hashing")
pass_object1 = sha1("password1", "hashing1")
pass_object2 = sha224("password2", "hashing2")
pass_object3 = sha256("password3", "hashing3")
pass_object4 = sha384("password4", "hashing4")
pass_object5 = sha512("password5", "hashing5")
pass_object.salt_file = uuid.uuid4().hex
pass_object1.salt_file1 = uuid.uuid4().hex
pass_object2.salt_file2 = uuid.uuid4().hex
pass_object3.salt_file3 = uuid.uuid4().hex
pass_object4.salt_file4 = uuid.uuid4().hex
pass_object5.salt_file5 = uuid.uuid4().hex
pass_object.pass_file = sys.argv[1] 
pass_object.hash_file = hashlib.md5(pass_object.salt_file.encode() + pass_object.pass_file.encode()).hexdigest()
pass_object1.hash_file1 = hashlib.sha1(pass_object1.salt_file1.encode() + pass_object.pass_file.encode()).hexdigest()
pass_object2.hash_file2 = hashlib.sha224(pass_object2.salt_file2.encode() + pass_object.pass_file.encode()).hexdigest()
pass_object3.hash_file3 = hashlib.sha256(pass_object3.salt_file3.encode() + pass_object.pass_file.encode()).hexdigest()
pass_object4.hash_file4 = hashlib.sha384(pass_object4.salt_file4.encode() + pass_object.pass_file.encode()).hexdigest()
pass_object5.hash_file5 = hashlib.sha512(pass_object5.salt_file5.encode() + pass_object.pass_file.encode()).hexdigest()
print "The pass md5 is :" , pass_object.hash_file
print "The pass sha1 is :" , pass_object1.hash_file1
print "The pass sha224 is :" , pass_object2.hash_file2
print "The pass sha256 is :" , pass_object3.hash_file3
print "The pass sha384 is :" , pass_object4.hash_file4
print "The pass sha512 is :" , pass_object5.hash_file5

