import random
import pygame
from config import WIDTH, HEIGHT, POLICE_WIDTH, POLICE_HEIGHT, MICE_WIDTH, MICE_HEIGHT
from assets import MICE_IMG, POLICE_IMG, EXPLOSION_ANIM

class Mice(pygame.sprite.Sprite):
    def __init__(self, groups, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[MICE_IMG]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT / 2
        self.rect.left = WIDTH/2 - MICE_WIDTH/2 - 25
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



class Explosion(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, assets):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de explosão
        self.explosion_anim = assets[EXPLOSION_ANIM]

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.explosion_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.explosion_anim):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
            