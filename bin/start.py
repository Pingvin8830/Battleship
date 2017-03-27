#!/bin/python3

'''
Создание окна
Пока пользователь не выбрал выход
  Отображение меню
  Опрос событий
    Если выбрано "Начало игры"
      Создание игровых полей
      Расстановка кораблей
      Игровой цикл
      Объявление победителя
Выход
'''

from sys import path
path.append ('/data/git/Battleship/lib')

import pygame
from color_vars  import BLACK, WHITE
from main_vars   import VERSION
from screen_vars import SCREEN_SIZE

pygame.init ()

screen = pygame.display.set_mode ([SCREEN_SIZE ['x'], SCREEN_SIZE ['y']])
pygame.display.set_caption ('Морской бой. Версия %s' % VERSION)

clock = pygame.time.Clock ()

current_status = 'menu'

while current_status != 'quit':

  for event in pygame.event.get ():
    if event.type == pygame.QUIT: current_status = 'quit'
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE: current_status = 'quit'

  screen.fill (WHITE)

  pygame.display.flip ()

  clock.tick (60)

pygame.quit ()
