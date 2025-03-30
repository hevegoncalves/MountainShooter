#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        pygame.init()  # inicializar os modulos da biblioteca
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))  # pixels da imagem

    def run(self):


        while True:
            menu = Menu(self.window)
            menu.run()
            pass