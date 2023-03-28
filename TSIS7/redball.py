import pygame

pygame.init()

screen = pygame.display.set_mode((700, 600))
RED = (255, 0, 0)
x = 337.5
y = 287.5
pos = (x, y)
pygame.display.set_caption("Red Ball")
clock = pygame.time.Clock()
running = True
fps = 30

while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if x > 25:
            x -= 25
    if keys[pygame.K_RIGHT]:
        if x < 775:
            x += 25
    if keys[pygame.K_UP]:
        if y > 25:
            y -= 25
    if keys[pygame.K_DOWN]:
        if y < 575:
            y += 25
    pos = (x, y)


    screen.fill((0, 200, 200))
    pygame.draw.circle(screen, RED, pos, 25)
    pygame.display.flip()