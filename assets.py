import pygame
import os
from config import WIDTH, HEIGHT, POLICE_WIDTH, POLICE_HEIGHT, MICE_WIDTH, MICE_HEIGHT, IMG_DIR, SND_DIR, FNT_DIR


BACKGROUND = 'background_img'
POLICE_IMG = 'police_img'
MICE_IMG = 'mice_img'
SCORE_FONT = 'score_font'
BOOM_SOUND = 'boom_sound'
DESTROY_SOUND = 'destroy_sound'


def load_assets():
    assets = {}
    assets['background_img'] = pygame.image.load('assets/img/cenario.png').convert()
    assets['background_img'] = pygame.transform.scale(assets['background_img'], (WIDTH, HEIGHT))
    assets['police_img'] = pygame.image.load('assets/img/carro.png').convert_alpha()
    assets['police_img'] = pygame.transform.scale(assets['police_img'], (POLICE_WIDTH, POLICE_HEIGHT))
    assets['police_img'] = pygame.transform.rotate(assets['police_img'], 90)
    assets['mice_img'] = pygame.image.load('assets/img/rato.png').convert_alpha()
    assets['mice_img'] = pygame.transform.scale(assets['mice_img'], (MICE_WIDTH, MICE_HEIGHT))

    assets["score_font"] = pygame.font.Font('assets/font/PressStart2P.ttf', 28)
    
    # Carrega os sons do jogo
    pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
    pygame.mixer.music.set_volume(0.4)
    assets['boom_sound'] = pygame.mixer.Sound('assets/snd/expl3.wav')
    assets['destroy_sound'] = pygame.mixer.Sound('assets/snd/expl6.wav')
    return assets
