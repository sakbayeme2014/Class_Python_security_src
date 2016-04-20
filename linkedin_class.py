#!/usr/bin/env python

class linkedin1():
 def __init__(self, val1, val2):
  self.val1 = val1
  self.val2 = val2
 def basic_account(self):
  print "my basic account is %s"  % self.val1
 def premium_account(self):
  print "My Premium account is %s" % self.val2 

class linkedin2():
 def __init__(self, val3, val4):
  self.val3 = val3
  self.val4 = val4
 def business_account(self):
  print "My business account is %s" % self.val3

compte = linkedin1("ID = 0001, Username = geoffroy, Password = _89", "ID = 0002, Username = Rene, Password = _*9")
comptes = linkedin2("ID = 0003, Username = Rene, Password = _**+", " ")
compte.basic_account()
compte.premium_account()
comptes.business_account()
