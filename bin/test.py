import pygame
from rounded import rect_round


pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("rounded, test")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

    rect_round(screen, (0, 0, 50, 50), (255, 0, 0), 1)
    pygame.display.flip()

