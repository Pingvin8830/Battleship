#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

from sys import path as SYSPATH
SYSPATH.append ('lib')
from menu import Menu

VERSION = '0.0'

MainMenu = Menu()
Doing = ''

while Doing != 'Выход':
	Doing = MainMenu.render()
