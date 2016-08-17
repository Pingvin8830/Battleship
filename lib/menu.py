#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

class Menu():
	'''Стандартный класс меню'''
	def __init__(self):
		'''Инициализация: присвоение заголовка и списка пунктов'''
		self.Header   = 'Морской бой!'
		self.Menu = ['Выход',
					 'Начать игру',
					 'Справка',
					 'История',
					 'Планы']
	def render(self):
		'''Отображение меню на экране'''
		print (self.Header)
		print ('-------------------------------')
		for i in list (range (1, len (self.Menu))) + [0]:
			print ("%d. %s" % (i, self.Menu [i]))
		return self.user_input()
	def user_input(self):
		'''Получение номера выбранного пункта'''
		try:
			index = int (input ('Что делать? '))
		except:
			return None
		if index in tuple (range (len (self.Menu))):
			return self.Menu[index]

def _yes_no (Question):
	'''Получение ответа Да / Нет'''
	#--- Возвращает True или False
	return input(Question).lower() in 'yд'
