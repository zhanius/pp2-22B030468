import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((255, 255, 255))
    pygame.display.flip()

    clock.tick(60)
