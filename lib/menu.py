Header   = 'Морской бой!'
MainMenu = [(1, 'Начать игру'),
						(2, 'Справка'),
						(3, 'История'),
						(4, 'Планы'),
						(0, 'Выход')]

def _yes_no (Question):
	'''Получение ответа Да / Нет'''
	print (Question)
	Ret = input ()
	if Ret == 'y' or Ret == 'Y' or Ret == 'Д' or Ret == 'д':
		return 1
	else:
		return 0

print (Header)
print ('-------------------------------')
for i in range (len (MainMenu)):
	print ("%d. %s" % (MainMenu [i][0], MainMenu [i][1]))
