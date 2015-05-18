#coding:utf-8
__author__ = 'maxbon'

from sys import argv

script, qualifier, user_name = argv
prompt = '>'

print "Hi %s %s, I'm the %s script." % (qualifier, user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s %s?" % (qualifier, user_name)
likes = raw_input(prompt)

print "Where do you live %s %s?" % (qualifier, user_name)
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %s about liking me.
You live in %s. Not sure where that is.
And you have a %s computer. Nice.
""" % (likes, lives, computer)