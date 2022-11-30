import pygame
import random
from os import path
from assets import *
from config import *


def end_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()

    # Carrega o fundo da tela inicial
    
    font2 = assets[SCORE_FONT_20]
    font1 = assets[SCORE_FONT_60]

    text1 = font1.render('GAME OVER!', True, RED)
    
    text2 = font2.render('Pressione qualquer tecla para sair', True, WHITE)

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

        text1_rect = text1.get_rect(center=(WIDTH/2, HEIGHT/2.3))
        screen.blit(text1, text1_rect)
        text2_rect = text2.get_rect(center=(WIDTH/2, HEIGHT/1.2))
        screen.blit(text2, text2_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
