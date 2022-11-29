import pygame
import random
from os import path

from config import *


def instr_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial

    font1 = pygame.font.SysFont(None, 90)
    text1 = font1.render('INSTRUÇÕES PARA JOGAR:', True, WHITE)
    font2 = pygame.font.SysFont(None, 60)
    text2 = font2.render('• Fuja dos carros de polícia! \n• Serão 3 níveis: 1, 2 e 3', True, WHITE)

    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False

            if event.type == pygame.KEYUP:
                state = GAME
                running = False

        # A cada loop, redesenha o fundo e os sprites
        screen.fill(BLACK)

        text1_rect = text1.get_rect(center=(WIDTH/2, 100))
        screen.blit(text1, text1_rect)
        text2_rect = text2.get_rect(center=(WIDTH/2, HEIGHT/2))
        screen.blit(text2, text2_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state