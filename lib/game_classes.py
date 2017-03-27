#!/bin/python3

import pygame
from color_vars import WHITE, BLACK

class Cell (object):
  '''Ячейка поля'''
  STATUSES = {
    'clear': WHITE,
  }

  SIZE = {
    'x': 30,
    'y': 30,
  }

  def __init__ (self):
    self.status = 'clear'

  def draw (self, screen, x, y):
    pygame.draw.rect (screen, BLACK, [x, y, self.SIZE ['x'], self.SIZE ['y']], 1)
    
class Field (object):
  '''Игровое поле'''
  SIZE = {
    'x': 10,
    'y': 10,
  }

  def __init__ (self):
    self.list_cells = {}
    for y in range (self.SIZE ['y']):
      for x in range (self.SIZE ['x']):
        self.list_cells [(x, y)] = Cell ()

  def draw (self, screen, x, y):
    for x_cell, y_cell in self.list_cells:
      cell = self.list_cells [(x_cell, y_cell)]
      cell.draw (screen, x + x_cell * cell.SIZE ['x'], y + y_cell * cell.SIZE ['y'])

class Player (object):
  '''Игрок'''
  def __init__ (self, type):
    self.type  = type
    self.field = Field ()

if __name__ == '__main__':
  print ('Модуль с игровыми классами')
