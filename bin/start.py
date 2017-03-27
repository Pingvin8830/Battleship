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
import random
from color_vars   import BLACK, WHITE
from draw_classes import Menu, Sight
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

      elif current_status == 'game':
        if player.is_active:
          if   event.key == pygame.K_UP:    sight.position ['y'] -= 1
          elif event.key == pygame.K_DOWN:  sight.position ['y'] += 1
          elif event.key == pygame.K_LEFT:  sight.position ['x'] -= 1
          elif event.key == pygame.K_RIGHT: sight.position ['x'] += 1

          if   sight.position ['x'] < 0:                    sight.position ['x'] = 0
          elif sight.position ['x'] > Field.SIZE ['x'] - 1: sight.position ['x'] = Field.SIZE ['x'] - 1

          if   sight.position ['y'] < 0:                    sight.position ['y'] = 0
          elif sight.position ['y'] > Field.SIZE ['y'] - 1: sight.position ['y'] = Field.SIZE ['y'] - 1

          if event.key == 13:
            player.fire (comp, sight.position ['x'], sight.position ['y'])

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
    if is_set:
      for i in range (len (comp.list_ships)):
        ship = comp.list_ships [i]
        while not ship.is_set:
          is_good = False
          while not is_good:
            ship.orient = random.choice (('horizont', 'vertical'))
            ship.start_cell = (random.randrange (Field.SIZE ['x']), random.randrange (Field.SIZE ['y']))
            is_good = True
            if ship.orient == 'horizont' and ship.start_cell [0] + ship.length > Field.SIZE ['x']: is_good = False
            if ship.orient == 'vertical' and ship.start_cell [1] + ship.length > Field.SIZE ['y']: is_good = False
          ship.update_set_status (comp.field.list_cells)
          if ship.set_status:
            ship.is_set = True
            comp.field.update (ship.oreol,      'oreol')
            comp.field.update (ship.list_cells, 'ship')
            comp.list_ships [i] = ship
      current_status = 'game'
      sight = Sight ()
      is_win = False

  if current_status == 'game' and comp.is_active:
    x = random.randrange (Field.SIZE ['x'])
    y = random.randrange (Field.SIZE ['y'])
    comp.fire (player, x, y)

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
  elif current_status == 'game':
    player.field.draw (screen,  10, 10)
    comp.field.draw   (screen, 320, 10)
    if player.is_active: sight.draw (screen)

  pygame.display.flip ()

  clock.tick (60)

pygame.quit ()
