import pygame
import random
from os import path

from config import IMG_DIR, BLACK, FPS, GAME, QUIT


def end_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    # Carrega o fundo da tela inicial

    font1 = pygame.font.SysFont(None, 60)
    text1 = font1.render('GAME OVER!', True, (255, 0, 0))
    font2 = pygame.font.SysFont(None, 36)
    text2 = font2.render('Pressione qualquer tecla para sair.', True, (255, 255, 255))

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
        screen.blit(text1, (110, 270))
        screen.blit(text2, (40, 400))

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
