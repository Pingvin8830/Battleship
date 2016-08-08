#!/usr/bin/python
# -*- coding: utf-8 -*-

VERSION = '0.0'

from os import system as OS_SYSTEM
from sys import path as SYSPATH
SYSPATH.append ('lib')
from menu import Menu

MainMenu = Menu()
Doing = 'Начать игру'

while Doing != 'Выход':

	OS_SYSTEM ('clear')
	Doing = MainMenu.render()
