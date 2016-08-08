#!/usr/bin/python
# -*- coding: utf-8 -*-

class Menu():
	def __init__(self):
		self.Header   = 'Морской бой!'
		self.Menu = ('Выход',
					 'Начать игру',
					 'Справка',
					 'История',
					 'Планы')
	def render(self):
		print (self.Header)
		print ('-------------------------------')
		for i in range (1, len (self.Menu)) + [0]:
			print ("%d. %s" % (i, self.Menu [i]))
		index = input ('Что делать? ')
		if index in range(len(self.Menu)):
			return self.Menu[index]

def _yes_no (Question):
	'''Получение ответа Да / Нет'''
	#--- Возвращает True или False
	return input(Question).lower() in 'yд'
