#!/usr/bin/env python

import hashlib
import sys

if len(sys.argv) <= 1:
 print "Usage : ./hash_class.py <file>"
 exit()

class md5():
 def __init__(self, file_object, hash_object):
  self.file_object = file_object
  self.hash_object = hash_object
 def file_open(self, file_object):
  self.file_object = file_object
 def hash_file(self, hash_object):
  self.hash_object = hash_object
  return xxx_object.hash_file
 def block_file(self, blocksize):
  self.blocksize = blocksize
 def cont_file(self, contents):
  self.contents = contents

class sha1():
 def __init__(self, file_object1, hash_object1):
  self.file_object1 = file_object1
  self.hash_object1 = hash_object1
 def file_open1(self, file_object1):
  self.file_object1 = file_object1
 def hash_file1(self, hash_object1):
  self.hash_object1 = hash_object1
  return xxx_object1.hash_file1
 def block_file1(self, blocksize1):
  self.blocksize1 = blocksize1
 def cont_file1(self, contents1):
  self.contents1 = contents1

class sha224():
 def __init__(self, file_object2, hash_object2):
  self.file_object2 = file_object2
  self.hash_object2 = hash_object2
 def file_open2(self, file_object2):
  self.file_object2 = file_object2
 def hash_file2(self, hash_object2):
  self.hash_object2 = hash_object2
  return xxx_object2.hash_file2
 def block_file2(self, blocksize2):
  self.blocksize2 = blocksize2
 def cont_file2(self, contents2):
  self.contents2 = contents2

class sha256():
 def __init__(self, file_object3, hash_object3):
  self.file_object3 = file_object3
  self.hash_object3 = hash_object3
 def file_open3(self, file_object3):
  self.file_object3 = file_object3
 def hash_file3(self, hash_object3):
  self.hash_object3 = hash_object3
 def block_file3(self, blocksize3):
  self.blocksize3 = blocksize3
 def cont_file3(self, contents3):
  self.contents3 = contents3

class sha384():
 def __init__(self, file_object4, hash_object4):
  self.file_object4 = file_object4
  self.hash_object4 = hash_object4
 def file_open4(self, file_object4):
  self.file_object4 = file_object4
 def hash_file4(self, hash_object4):
  self.hash_object4 = hash_object4
  return xxx_object4.hash_file4
 def block_file4(self, blocksize4):
  self.blocksize4 = blocksize4
 def cont_file4(self, contents4):
  self.contents4 = contents4 

class sha512():
 def __init__(self, file_object5, hash_object5):
  self.file_object5 = file_object5
  self.hash_object5 = hash_object5
 def file_open5(self, file_object5):
  self.file_object5 = file_object5
 def hash_file5(self, hash_object5):
  self.hash_object5 = hash_object5
  return xxx_object5.hash_file5
 def block_file5(self, blocksize5):
  self.blocksize5 = blocksize5
 def cont_file5(self, contents5):
  self.contents5 = contents5

xxx_object = md5("file_object", "hash_object")
xxx_object.block_file = 65535
xxx_object.file_open = open(sys.argv[1], "rb")
xxx_object.cont_file = xxx_object.file_open.read(xxx_object.block_file)
xxx_object.hash_file = hashlib.md5()
for i in xxx_object.cont_file:
 xxx_object.hash_file.update(i)
 i = xxx_object.file_open.read(xxx_object.block_file)

xxx_object1 = sha1("file_object1", "hash_object1")
xxx_object1.block_file1 = 65535
xxx_object1.file_open1 = open(sys.argv[1], "rb")
xxx_object1.cont_file1 = xxx_object1.file_open1.read(xxx_object1.block_file1)
xxx_object1.hash_file1 = hashlib.sha1()
for j in xxx_object1.cont_file1:
 xxx_object1.hash_file1.update(j)
 j = xxx_object1.file_open1.read(xxx_object1.block_file1)

xxx_object2 = sha224("file_object2", "hash_object2") 
xxx_object2.block_file2 = 65535
xxx_object2.file_open2 = open(sys.argv[1], "rb")
xxx_object2.cont_file2 = xxx_object2.file_open2.read(xxx_object2.block_file2)
xxx_object2.hash_file2 = hashlib.sha224()
for k in xxx_object2.cont_file2:
 xxx_object2.hash_file2.update(k)
 k = xxx_object2.file_open2.read(xxx_object2.block_file2)

xxx_object3 = sha256("file_object3", "hash_object3")
xxx_object3.block_file3 = 65535
xxx_object3.file_open3 = open(sys.argv[1], "rb")
xxx_object3.cont_file3 = xxx_object3.file_open3.read(xxx_object3.block_file3)
xxx_object3.hash_file3 = hashlib.sha256()
for l in xxx_object3.cont_file3:
 xxx_object3.hash_file3.update(l)
 l = xxx_object3.file_open3.read(xxx_object3.block_file3)

xxx_object4 = sha384("file_object4", "hash_object4")
xxx_object4.block_file4 = 65535
xxx_object4.file_open4 = open(sys.argv[1], "rb")
xxx_object4.cont_file4 = xxx_object4.file_open4.read(xxx_object4.block_file4)
xxx_object4.hash_file4 = hashlib.sha384()
for p in xxx_object4.cont_file4:
 xxx_object4.hash_file4.update(p)
 p = xxx_object4.file_open4.read(xxx_object4.block_file4)

xxx_object5 = sha512("file_object5", "hash_object5")
xxx_object5.block_file5 = 65535
xxx_object5.file_open5 = open(sys.argv[1], "rb")
xxx_object5.cont_file5 = xxx_object5.file_open5.read(xxx_object5.block_file5)
xxx_object5.hash_file5 = hashlib.sha512()
for e in xxx_object5.cont_file5:
 xxx_object5.hash_file5.update(e)
 e = xxx_object5.file_open5.read(xxx_object5.block_file5)

print "The md5 sum is : " , xxx_object.hash_file.hexdigest()
print "The sha1 sum is : ", xxx_object1.hash_file1.hexdigest()
print "The sha224 sum is : ", xxx_object2.hash_file2.hexdigest()
print "The sha256 sum is : ", xxx_object3.hash_file3.hexdigest()
print "The sha384 sum is : ", xxx_object4.hash_file4.hexdigest()
print "The sha512 sum is : ", xxx_object5.hash_file5.hexdigest()



