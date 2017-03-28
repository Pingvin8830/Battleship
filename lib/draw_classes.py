#!/usr/bin/python3

import pygame
from color_vars   import RED, GREEN, BLACK, WHITE
from game_classes import Cell
from screen_vars  import SCREEN_SIZE

class Item (object):
  '''Пункт меню'''
  COLORS = {
    'active':  RED,
    'passive': BLACK,
    'hidden':  WHITE,
    'click':   GREEN,
  }

  def __init__ (self, x, y, text, doing, status = 'passive'):
    self.text   = text
    self.status = status
    self.x      = x
    self.y      = y
    self.doing  = doing
    self.font = pygame.font.Font (None, 30)

  def draw (self, screen):
    self.color = self.COLORS [self.status]
    text = self.font.render (self.text, True, self.color)
    screen.blit (text, [self.x, self.y])

class Menu (object):
  '''Меню'''
  def __init__ (self, type = 'main'):
    self.items = []
    if type == 'main':
      self.items = [
        Item (10,  10, 'Начать игру', 'new_game', 'active'),
        Item (10,  50, 'Настройки',   'settings'          ),
        Item (10,  90, 'Справка',     'help'              ),
        Item (10, 130, 'Планы',       'planes'            ),
        Item (10, 170, 'Выход',       'quit'              ),
      ]

  def draw (self, screen):
    background = pygame.image.load ('/data/git/Battleship/images/main_background.jpg').convert ()
    screen.blit (background, [0, 0])
    i = 0
    for item in self.items: item.draw (screen)

  def moving (self, route):
    for i in range (len (self.items)):
      item = self.items [i]
      if item.status == 'active':
        item.status = 'passive'
        if route == 'next':
          try:
            item = self.items [i + 1]
          except:
            item = self.items [i]
        elif route == 'prev':
          if i != 0:
            item = self.items [i - 1]
          else:
            item = self.items [i]
        item.status = 'active'
        break

  def get_status (self):
    for item in self.items:
      if item.status == 'active':
        doing = item.doing
        break
    return doing

class Sight (object):
  '''Прицел'''
  def __init__ (self):
    self.position = {
      'x': 4,
      'y': 4,
    }

  def draw (self, screen):
    start_x = self.position ['x'] * Cell.SIZE ['x'] + 320
    start_y = self.position ['y'] * Cell.SIZE ['y'] +  10
    center_x = start_x + Cell.SIZE ['x'] / 2
    center_y = start_y + Cell.SIZE ['y'] / 2
    end_x = start_x + Cell.SIZE ['x']
    end_y = start_y + Cell.SIZE ['y']
    pygame.draw.ellipse (screen, RED, [start_x + 2,  start_y + 2, Cell.SIZE ['x'] - 4, Cell.SIZE ['y'] - 4], 1)
    pygame.draw.line    (screen, RED, [start_x,      center_y    ], [center_x - 3, center_y    ], 1)
    pygame.draw.line    (screen, RED, [center_x + 3, center_y    ], [end_x,        center_y    ], 1)
    pygame.draw.line    (screen, RED, [center_x,     start_y     ], [center_x,     center_y - 3], 1)
    pygame.draw.line    (screen, RED, [center_x,     center_y + 3], [center_x,     end_y       ], 1)

if __name__ == '__main__':
  print ('Модуль с классами для отображения')
