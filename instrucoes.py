import pygame
import random
from os import path
from assets import *
from config import *


def instr_screen(screen):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()

    # Carrega o fundo da tela inicial

    font1 = assets[SCORE_FONT_40]
    font2 = assets[SCORE_FONT_20]
    text1 = font1.render('INSTRUÇÕES PARA JOGAR:', True, YELLOW)
    text2 = font2.render('• Fuja dos carros de polícia!', True, YELLOW)
    text3 = font2.render('• Serão 3 níveis: 1, 2 e 3', True, YELLOW)
    text4 = font2.render('• Cada nível terá um número de carros de polícia', True, YELLOW)
    text5 = font2.render('maior que o anterior', True, YELLOW)
    text6 = font2.render('• O jogador deve se movimentar utilizando as setas do teclado', True, YELLOW)    
    

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

        screen.blit(assets[INSTR_IMG], (0, 0))        
        
        # # RETANGULO TRANSLUCIDO PRETO
        # pygame.draw.rect (screen, (0, 0, 0), (0, 0, WIDTH, HEIGHT))

        # s = pygame.Surface((WIDTH,HEIGHT))  # the size of your rect
        # s.set_alpha(255)                # alpha level
        # s.fill((0,0,0))           # this fills the entire surface
        # screen.blit(s, (0,0))    # (0,0) are the top-left coordinates

        text1_rect = text1.get_rect(center=(WIDTH/2, 150))
        screen.blit(text1, text1_rect)
        text2_rect = text2.get_rect(center=(WIDTH/2, HEIGHT/2 - 30))
        screen.blit(text2, text2_rect)
        text3_rect = text3.get_rect(center=(WIDTH/2, HEIGHT/2 +50))
        screen.blit(text3, text3_rect)
        text4_rect = text4.get_rect(center=(WIDTH/2, HEIGHT/2 +130))
        screen.blit(text4, text4_rect)
        text5_rect = text5.get_rect(center=(WIDTH/2, HEIGHT/2 +180))
        screen.blit(text5, text5_rect)
        text6_rect = text6.get_rect(center=(WIDTH/2, HEIGHT/2 + 260))
        screen.blit(text6, text6_rect)

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state
