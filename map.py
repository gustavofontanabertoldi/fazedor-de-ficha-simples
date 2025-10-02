import pygame
import sys

pygame.init()

# Configura janela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mapinha RPG")

# Cores
WHITE = (255, 255, 255)
RED   = (200, 50, 50)
BLUE  = (50, 50, 200)

# Tokens como retângulos
tokens = [
    pygame.Rect(100, 100, 60, 60),  # quadrado vermelho
    pygame.Rect(300, 200, 60, 60)   # quadrado azul
]
colors = [RED, BLUE]

dragging = None  # qual token está sendo arrastado

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Pressionar mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # botão esquerdo
                for i, token in enumerate(tokens):
                    if token.collidepoint(event.pos):
                        dragging = i
                        mouse_x, mouse_y = event.pos
                        offset_x = token.x - mouse_x
                        offset_y = token.y - mouse_y

        # Soltar mouse
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = None

        # Mover mouse
        if event.type == pygame.MOUSEMOTION:
            if dragging is not None:
                mouse_x, mouse_y = event.pos
                tokens[dragging].x = mouse_x + offset_x
                tokens[dragging].y = mouse_y + offset_y

    # Desenho
    screen.fill(WHITE)
    for i, token in enumerate(tokens):
        pygame.draw.rect(screen, colors[i], token)
    pygame.display.flip()
    clock.tick(60)
