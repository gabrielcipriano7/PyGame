import pygame
from config import FPS, WIDTH, HEIGHT, BLACK, YELLOW, RED
from assets import load_assets, DESTROY_SOUND, BOOM_SOUND, BACKGROUND, SCORE_FONT
from sprites import Mice, Police

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    # Criando um grupo de meteoros
    all_sprites = pygame.sprite.Group()
    all_police = pygame.sprite.Group()
    
    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_police'] = all_police

    # Criando o jogador
    player = Mice(groups, assets)
    all_sprites.add(player)
    


    DONE = 0
    PLAYING = 1
    EXPLODING = 2
    state = PLAYING

    keys_down = {}
    score = 0

    lives = 3 

    x1 = 0
    x2 = 0
    x3 = 0

    # ===== Loop principal =====
    pygame.mixer.music.play(loops=-1)
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE
            # Só verifica o teclado se está no estado de jogo
            if state == PLAYING:
                # Verifica se apertou alguma tecla.
                if event.type == pygame.KEYDOWN:
                    # Dependendo da tecla, altera a velocidade.
                    keys_down[event.key] = True
                    if event.key == pygame.K_DOWN:
                        player.speedy += 8
                    if event.key == pygame.K_UP:
                        player.speedy -= 8
                    if event.key == pygame.K_RIGHT:
                        player.speedx += 8
                    if event.key == pygame.K_LEFT:
                        player.speedx -= 8
                # Verifica se soltou alguma tecla.
                if event.type == pygame.KEYUP:
                    # Dependendo da tecla, altera a velocidade.
                    if event.key in keys_down and keys_down[event.key]:
                        if event.key == pygame.K_DOWN:
                            player.speedy -= 8
                        if event.key == pygame.K_UP:
                            player.speedy += 8
                        if event.key == pygame.K_RIGHT:
                            player.speedx -= 8
                        if event.key == pygame.K_LEFT:
                            player.speedx += 8

        # ----- Atualiza estado do jogo
        # Atualizando a posição dos carros de policia
        all_sprites.update()


        if state == PLAYING:

            
            score += 1

            if score <= 1000:
                if x1 < 1:
                    
                        # Criando os carros de polícia
                    for i in range(2):
                        police = Police(assets)
                        all_sprites.add(police)
                        all_police.add(police)
                        
                        x1 += 1
            

            elif score > 1000 and score < 2000:
                if x2 < 1:
                    
                        # Criando os carros de polícia
                    for i in range(2):
                        police = Police(assets)
                        all_sprites.add(police)
                        all_police.add(police)
                        x2 += 1
                    police.speedx = -6

            elif score >= 2000:
                if x3 < 1:
                    
                        # Criando os carros de polícia
                    for i in range(2):
                        police = Police(assets)
                        all_sprites.add(police)
                        all_police.add(police)
                        x3 += 1
                    police.speedx = -9

                    

            # Verifica se houve colisão entre rato e policia
            hits = pygame.sprite.spritecollide(player, all_police, True, pygame.sprite.collide_mask)
            if len(hits) > 0:
                # Toca o som da colisão
                assets[BOOM_SOUND].play()
                player.kill()
                police.kill()
                lives -= 1
                state = EXPLODING
                keys_down = {}
              
            

        elif state == EXPLODING:

            if lives == 0:
                state = DONE
            else:
                state = PLAYING
                player = Mice(groups, assets)
                all_sprites.add(player)

        # ----- Gera saídas
        window.fill(BLACK)  # Preenche com a cor branca
        window.blit(assets[BACKGROUND], (0, 0))
        # Desenhando meteoros
        all_sprites.draw(window)

        # Desenhando o score
        text_surface = assets[SCORE_FONT].render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 2,  10)
        window.blit(text_surface, text_rect)

        # Desenhando as vidas
        text_surface = assets[SCORE_FONT].render(chr(9829) * lives, True, RED)
        text_rect = text_surface.get_rect()
        text_rect.bottomleft = (10, HEIGHT - 10)
        window.blit(text_surface, text_rect)

        pygame.display.update()  # Mostra o novo frame para o jogador
