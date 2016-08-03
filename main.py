#!/bin/python

VERSION = '0.0'

import sys, os
sys.path.append ('/data/git/Battleship/lib')
import menu

Doing = 'start'

while Doing != 'exit':
	
	os.system ('clear')
	print (menu.Header)
	print ('-------------------------------')
	for i in range (len (menu.MainMenu)):
		print ("%d. %s" % (menu.MainMenu [i][0], menu.MainMenu [i][1]))

	Doing = input ('Что делать? ')
