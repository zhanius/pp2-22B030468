import pygame
import math
import random


class EnemyCar(pygame.sprite.Sprite):
    def __init__(self, side, image):
        self.size = [100, 50]
        self.image = pygame.transform.scale(pygame.image.load(image), self.size)
        self.init_image = self.image
        self.rect = self.image.get_rect()
        self.side = side
        match self.side:
            case 'left':
                self.rect.center = (370, 390)
            case 'middle':
                self.rect.center = (420, 390)
            case 'right':
                self.rect.center = (470, 390)

    def move(self):
        #self.size = [self.size[0] * 1, self.size[1] * 1.02]
       # self.image = pygame.transform.scale(self.image, self.size)
        match self.side:
            case 'left':
                self.rect.move_ip(-1.5, 1.5)
            case 'middle':
                self.rect.move_ip(0, 1.5)
            case 'right':
                self.rect.move_ip(1.5, 1.5)
        if self.rect.bottom > 600:
            self.size = [50, 37.5]
            self.image = self.init_image
            match self.side:
                case 'left':
                    self.rect.center = (370, 390)
                case 'middle':
                    self.rect.center = (420, 390)
                case 'right':
                    self.rect.center = (470, 390)

    def draw(self, surf):
        surf.blit(self.image, self.rect)


class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.transform.scale(pygame.image.load("main_car_middle.png"), (150, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (420, 550)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left < 150:
            self.image = pygame.transform.scale(pygame.image.load('main_car_left.png'), (150, 100))
        elif self.rect.right > 650:
            self.image = pygame.transform.scale(pygame.image.load('main_car_right.png'), (150, 100))
        else:
            self.image = pygame.transform.scale(pygame.image.load('main_car_middle.png'), (150, 100))


        if self.rect.left > 0 and self.rect.right < 780:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(20, 0)
        if self.rect.right < 800 and self.rect.left > 20:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-20, 0)
        
    def draw(self, surf):
        surf.blit(self.image, self.rect)

