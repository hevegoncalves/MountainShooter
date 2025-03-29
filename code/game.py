#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.menu import Menu


class Game:
    def __init__(self):
        # Base do codigo para iniciar a criação do jogo, que é a janela de abertura do jogo
        pygame.init()  # inicializar os modulos da biblioteca
        self.window = pygame.display.set_mode(size=(600, 480))  # pixels da imagem

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

        # check for all events (verificar todos os eventos)
            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:  # event QUIT is close, close the window
            #        pygame.quit()  # close window
            #        quit()  # end pygame
                    # finalização do codigo da janela de abertura do jogo
