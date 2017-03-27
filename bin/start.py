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
path.append ('/data/git/Battleship/images')

import pygame
from color_vars   import BLACK, WHITE
from main_vars    import VERSION
from screen_vars  import SCREEN_SIZE
from draw_classes import Menu

pygame.init ()

screen = pygame.display.set_mode ([SCREEN_SIZE ['x'], SCREEN_SIZE ['y']])
pygame.display.set_caption ('Морской бой. Версия %s' % VERSION)

clock = pygame.time.Clock ()
pygame.mouse.set_visible (0)

current_status = 'menu'
menu = Menu ()

while current_status != 'quit':

  for event in pygame.event.get ():
    if event.type == pygame.QUIT: current_status = 'quit'
    elif event.type == pygame.KEYDOWN:
      if   event.key     == pygame.K_ESCAPE: current_status = 'quit'
      elif event.unicode == 'q':             current_status = 'quit'
      if current_status == 'menu':
        if   event.key == pygame.K_DOWN: menu.moving ('next')
        elif event.key == pygame.K_UP:   menu.moving ('prev')
        elif event.key == 13:            current_status = menu.get_status ()

  screen.fill (WHITE)

  if current_status == 'menu':
    menu.draw (screen)

  pygame.display.flip ()

  clock.tick (60)

pygame.quit ()
