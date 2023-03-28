import pygame 
from datetime import datetime

pygame.init()
w, h = 1200, 800
surface = pygae.display.set_mode((w,h))
clock = pygame.time.Clock()

curr_time = datetime.now()
curr_sec = datetime.now.second()
curr_min = fatetime.now.minute()
 
while True:
    surface.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

