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
        self.speed.y = 0
        self.groups = groups
        self.assets = assets


    def update(self):
        # Atualização da posição do rato
        self.rect.y += self.speed.y

        # Mantem dentro da tela
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
        if self.rect.top < 0:
            self.rect.top = 0

class Police (pygame.sprite.Sprite):
    def __init__(self, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[POLICE_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, WIDTH-POLICE_WIDTH)
        self.rect.y = random.randint(-100, -POLICE_HEIGHT)
        self.speedx = random.randint(-3, 3)
        self.speedy = random.randint(2, 9)

    def update(self):
        # Atualizando a posição do meteoro
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        # Se o meteoro passar do final da tela, volta para cima e sorteia
        # novas posições e velocidades
        if self.rect.top > HEIGHT or self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0, WIDTH-POLICE_WIDTH)
            self.rect.y = random.randint(-100, -POLICE_HEIGHT)
            self.speedx = random.randint(-3, 3)
            self.speedy = random.randint(2, 9)