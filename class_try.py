#!/usr/bin/env python

class Human():
 def __init__(self, name, gender):
  self.name = name
  self.gender = gender
 def speak_name(self):
  print "My name is %s" % self.name
 def speak_gender(self):
  print "My name is %s" % self.gender
 def speak(self, text):
  print text 
 def addition(self, addition, *args):
  print "%s task is %f" % (self.name, addition(*args))
 def subtraction(self, subtraction, *args):
  print "%s task is %f" % (self.gender, subtraction(*args))
def add1(a,b):
 return a + b
def sub1(c,d):
 return c - d
 

  
  
person = Human("andre", "lea")
print person.name
print person.gender
person.speak_name()
person.speak_gender()
person.speak("My name is python")
person.addition(add1, 100, 65)
person.subtraction(sub1, 200.75, 180.30)

