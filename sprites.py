import random
import pygame
from config import WIDTH, HEIGHT, POLICE_WIDTH, POLICE_HEIGHT, MICE_WIDTH, MICE_HEIGHT
from assets import MICE_IMG, POLICE_IMG

class Mice(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[MICE_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT / 2
        self.rect.left = WIDTH - (WIDTH -10)
        self.speedy = 0
        self.speedx = 0
        self.groups = groups
        self.assets = assets


    def update(self):
        # Atualização da posição do rato
        self.rect.y += self.speedy
        self.rect.x += self.speedx

        # Mantem dentro da tela
        if self.rect.bottom > HEIGHT - MICE_HEIGHT - HEIGHT/5.5:
            self.rect.bottom = HEIGHT - MICE_HEIGHT - HEIGHT/5.5
        if self.rect.top < HEIGHT/3.5:
            self.rect.top = HEIGHT/3.5
        if self.rect.left < WIDTH - (WIDTH -10):
            self.rect.left = WIDTH - (WIDTH -10)
        if self.rect.right > WIDTH - MICE_WIDTH - 10:
            self.rect.right = WIDTH - MICE_WIDTH - 10

class Police_control ():
    speedx = -4



class Police (pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        lista_posicoes = [HEIGHT/4.3, HEIGHT/2.8, HEIGHT/2.05]
        self.image = assets[POLICE_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH
        self.rect.y = random.choice(lista_posicoes)
        self.speedx = -4

    def update(self):
        self.speedx = Police_control.speedx
        # Atualizando a posição da policia
        self.rect.x += self.speedx
        self.rect.y = self.rect.y
        # Se a policia passar do final da tela, volta para a direita e sorteia
        # novas posições e velocidades
        lista_posicoes = [HEIGHT/4.3, HEIGHT/2.8, HEIGHT/2.05]
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = WIDTH
            self.rect.y = random.choice(lista_posicoes)
            