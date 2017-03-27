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
from draw_classes import Menu
from game_classes import Player, Field
from main_vars    import VERSION
from screen_vars  import SCREEN_SIZE

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
      elif current_status == 'set_ships':
        if player.is_active:
          for i in range (len (player.list_ships)):
            ship = player.list_ships [i]
            if not ship.is_set:
              if   event.key == pygame.K_LEFT:  ship.start_cell [0] -= 1
              elif event.key == pygame.K_RIGHT: ship.start_cell [0] += 1
              elif event.key == pygame.K_UP:    ship.start_cell [1] -= 1
              elif event.key == pygame.K_DOWN:  ship.start_cell [1] += 1
              elif event.key == pygame.K_SPACE:
                if    ship.orient == 'horizont': ship.orient = 'vertical'
                else:                            ship.orient = 'horizont'

              if   ship.start_cell [0] < 0: ship.start_cell [0] = 0
              elif ship.start_cell [0] > Field.SIZE ['x'] - ship.length and ship.orient == 'horizont': ship.start_cell [0] = Field.SIZE ['x'] - ship.length
              elif ship.start_cell [0] > Field.SIZE ['x'] - 1           and ship.orient == 'vertical': ship.start_cell [0] = Field.SIZE ['x'] - 1

              if   ship.start_cell [1] < 0: ship.start_cell [1] = 0
              elif ship.start_cell [1] > Field.SIZE ['y'] - ship.length and ship.orient == 'vertical': ship.start_cell [1] = Field.SIZE ['y'] - ship.length
              elif ship.start_cell [1] > Field.SIZE ['y'] - 1           and ship.orient == 'horizont': ship.start_cell [1] = Field.SIZE ['y'] - 1

              ship.update_set_status (player.field.list_cells)
              if event.key == 13:
                if ship.set_status:
                  ship.is_set = True
                  player.field.update (ship.oreol,      'oreol')
                  player.field.update (ship.list_cells, 'ship')

              player.list_ships [i] = ship
              break

  if current_status == 'new_game':
    player = Player ('human')
    player.is_active = True
    for koord in player.field.list_cells:
      cell = player.field.list_cells [koord]
      cell.is_visible = True
    comp   = Player ('AI')
    current_status = 'set_ships'

  if current_status == 'set_ships':
    is_set   = True
    for ship in player.list_ships:
      if not ship.is_set:
        is_set = False
        break
    for ship in comp.list_ships:
      if not ship.is_set:
        is_set = False

  screen.fill (WHITE)

  if current_status == 'menu':
    menu.draw (screen)
  elif current_status == 'set_ships':
    player.field.draw (screen,  10, 10)
    comp.field.draw   (screen, 320, 10)
    for ship in player.list_ships:
      if ship.is_set: ship.draw (screen, player.type)
      else:
        ship.update_set_status (player.field.list_cells)
        ship.draw (screen, player.type)
        break

  pygame.display.flip ()

  clock.tick (60)

pygame.quit ()
