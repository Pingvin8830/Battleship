#!/bin/python3

import pygame
from color_vars import WHITE, BLACK, RED, BLUE, GREEN

class Cell (object):
  '''Ячейка поля'''
  STATUSES = {
    'clear':   WHITE,
    'wounded': RED,
    'kill':    BLUE,
    'miss':    BLACK,
    'ship':    RED,
    'oreol':   BLUE,
  }

  SIZE = {
    'x': 30,
    'y': 30,
  }

  def __init__ (self):
    self.is_visible = False
    self.status = 'clear'

  def draw (self, screen, x, y):
    pygame.draw.rect (screen, BLACK, [x, y, self.SIZE ['x'], self.SIZE ['y']], 1)
    if self.is_visible: pygame.draw.rect (screen, self.STATUSES [self.status], [x + 1, y + 1, self.SIZE ['x'] - 2, self.SIZE ['y'] - 2])
    
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

  def update (self, list_cells, status):
    for cell in list_cells:
      if cell in self.list_cells: self.list_cells [cell].status = status

class Ship (object):
  '''Корабль'''
  def __init__ (self, length):
    self.length      = length
    self.start_cell  = [4, 4]
    self.orient      = 'horizont'
    self.oreol       = []
    self.list_cells  = []
    self.is_set      = False
    self.list_damage = []
    self.set_status  = True

  def draw (self, screen, type):
    if self.orient == 'horizont':
      if type == 'human':
        if self.set_status: color = GREEN
        else:               color = RED
        pygame.draw.rect (screen, color, [15 + self.start_cell [0] * Cell.SIZE ['x'], 15 + self.start_cell [1] * Cell.SIZE ['y'], Cell.SIZE ['x'] * self.length - 10, Cell.SIZE ['y'] - 10])
    else:
      if type == 'human':
        if self.set_status: color = GREEN
        else:               color = RED
        pygame.draw.rect (screen, color, [15 + self.start_cell [0] * Cell.SIZE ['x'], 15 + self.start_cell [1] * Cell.SIZE ['y'], Cell.SIZE ['x'] - 10, Cell.SIZE ['y'] * self.length - 10])

  def update_set_status (self, list_cells):
    self.set_status = True
    start_x = self.start_cell [0] - 1
    start_y = self.start_cell [1] - 1
    end_x   = self.start_cell [0] + self.length + 1
    end_y   = self.start_cell [1] + self.length + 1
    if self.orient == 'horizont': end_y = self.start_cell [1] + 2
    else:                         end_x = self.start_cell [0] + 2

    self.oreol      = []
    self.list_cells = []
    if self.orient == 'horizont':
      for x in range (self.start_cell [0], self.start_cell [0] + self.length):
        self.list_cells.append ((x, self.start_cell [1]))
    else:
      for y in range (self.start_cell [1], self.start_cell [1] + self.length):
        self.list_cells.append ((self.start_cell [0], y))
    for y in range (start_y, end_y):
      for x in range (start_x, end_x):
        self.oreol.append ((x, y))
        try:
          cell = list_cells [(x, y)]
        except:
          cell = list_cells [(self.start_cell [0], self.start_cell [1])]
        if cell.status == 'ship': self.set_status = False

class Player (object):
  '''Игрок'''
  def __init__ (self, type):
    self.type  = type
    self.field = Field ()
    self.list_ships = [
      Ship (4),
      Ship (3),
      Ship (3),
      Ship (2),
      Ship (2),
      Ship (2),
      Ship (1),
      Ship (1),
      Ship (1),
      Ship (1),
    ]
    self.is_active = False

if __name__ == '__main__':
  print ('Модуль с игровыми классами')
