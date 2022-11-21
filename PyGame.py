import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen import init_screen
from game_screen import game_screen
from end_screen import end_screen


pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The great bank robbery!')


def load_assets():
    assets = {}
    assets['background'] = pygame.image.load('assets/img/cenario.png').convert()
    assets['police_img'] = pygame.image.load('assets/img/carro.png').convert_alpha()
    assets['police_img'] = pygame.transform.scale(assets['meteor_img'], (POLICE_WIDTH, POLICE_HEIGHT))
    assets['mice_img'] = pygame.image.load('assets/img/rato.png').convert_alpha()
    assets['ship_img'] = pygame.transform.scale(assets['ship_img'], (MICE_WIDTH, MICE_HEIGHT))

    # Carrega os sons do jogo
    pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
    pygame.mixer.music.set_volume(0.4)
    assets['boom_sound'] = pygame.mixer.Sound('assets/snd/expl3.wav')
    assets['destroy_sound'] = pygame.mixer.Sound('assets/snd/expl6.wav')
    return assets

game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(assets['background'], (0, 0))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do pygame que finaliza os recursos utilizados

