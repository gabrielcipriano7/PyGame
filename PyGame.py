# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen import init_screen
from game_screen import game_screen
from end_screen import end_screen
from instrucoes import instr_screen


pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('The great bank robbery!')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
        state = instr_screen(window)
    elif state == GAME:
        state = game_screen(window)
    else:
        state = QUIT

if state == QUIT:
    state = end_screen(window)

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

