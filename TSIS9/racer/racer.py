import random
import time
import pygame
import sys
from pygame import mixer

# initial game configuration
screen_width = 800
screen_height = 600
fps = 60
car_speed = 1

# some configuration for enemy cars
side_list = ['left', 'middle', 'right']


# class for animating background
class Background(pygame.sprite.Sprite):
    def __init__(self):
        self.size = (screen_width, screen_height)
        self.bg_num = 1
        self.image = pygame.transform.scale(pygame.image.load(f"bg{self.bg_num}.png"), self.size)
        self.score = 0

    def draw(self, surf):
        surf.blit(self.image, (0, 0))
        if self.bg_num < 2:
            self.bg_num += 1
        else:
            self.bg_num = 1

    def draw_score(self, surf, font, score):
        score_text = f"Score: {score}"
        score_surf = font.render(score_text, True, (255, 0, 0))
        score_rect = score_surf.get_rect(center=(750, 50))
        surf.blit(score_surf, score_rect)


# class for coins
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = (30, 30)
        self.pos = (random.randint(50, 750), 550)
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])
        self.image = pygame.transform.scale(pygame.image.load(f'coin.jpeg'), self.size)

    def move(self):
        pass


# class for enemy car
class EnemyCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size = [75, 50]
        self.side = side_list[random.randint(0, 2)]
        self.image = pygame.transform.scale(pygame.image.load(f"{random.randint(1, 4)}_car_{self.side}.png"),self.size)
        self.rect = self.image.get_rect()
        match self.side:
            case 'left':
                self.rect.center = (370, 390)
            case 'middle':
                self.rect.center = (420, 390)
            case 'right':
                self.rect.center = (470, 390)

    def move(self):
        match self.side:
            case 'left':
                self.rect.move_ip(-2.5, car_speed - 0.2)
            case 'middle':
                self.rect.move_ip(0, car_speed)
            case 'right':
                self.rect.move_ip(2.5, car_speed - 0.2)
        if self.rect.bottom > 600:
            self.side = side_list[random.randint(0, 2)]
            self.image = pygame.transform.scale(
                pygame.image.load(f"{random.randint(1, 4)}_car_{self.side}.png"), self.size)
            match self.side:
                case 'left':
                    self.rect.center = (370, 390)
                case 'middle':
                    self.rect.center = (420, 390)
                case 'right':
                    self.rect.center = (470, 390)


# class for player car
class PlayerCar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("main_car_middle.png"), (150, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (420, 550)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left < 150:
            self.image = pygame.transform.scale(pygame.image.load('main_car_left.png'), (150, 100))
        elif self.rect.right > 650:
            self.image = pygame.transform.scale(pygame.image.load('main_car_right.png'), (150, 100))
        else:
            self.image = pygame.transform.scale(pygame.image.load('main_car_middle.png'), (150, 100))

        if self.rect.left > 0 and self.rect.right < 780:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(10, 0)
        if self.rect.right < 800 and self.rect.left > 20:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-10, 0)


def main():
    global car_speed
    car_speed = 1
    score = 0

    # default pygame initialization
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Night Rider")

    # loading background image
    bg_image = pygame.image.load('bg1.png')
    bg_image = pygame.transform.scale(bg_image, (800, 600))

    # initializing background class 
    bg = Background()

    # initializing enemy and player cars
    enemy_car1 = EnemyCar()
    player_car = PlayerCar()
    coin = Coin()

    # creating sprite group for enemy cars
    enemy_sprites = pygame.sprite.Group()
    enemy_sprites.add(enemy_car1)

    coin_group = pygame.sprite.Group()
    coin_group.add(coin)

    # creating sprite group for all cars
    all_sprites = pygame.sprite.Group()
    all_sprites.add(enemy_car1)
    all_sprites.add(player_car)
    all_sprites.add(coin)

    # increasing speed of the enemy cars
    inc_speed = pygame.USEREVENT + 1
    pygame.time.set_timer(inc_speed, 1000)

    # loading music
    mixer.music.load('bg_music.mp3')
    mixer.music.play()

    font = pygame.font.Font('Blessed.ttf', 20)

    while True:
        for event in pygame.event.get():
            if event.type == inc_speed:
                car_speed += 0.1

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # drawing background on the screen
        screen.fill((255, 255, 255))
        bg.draw(screen)
        bg.draw_score(screen, font, score)

        # drawing all sprites on the screen
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect)
            sprite.move()

        # collision detection of player car with enemy cars
        if pygame.sprite.spritecollideany(player_car, enemy_sprites):
            screen.fill((255, 0, 0))
            pygame.display.update()
            for sprite in all_sprites:
                sprite.kill()
            mixer.music.pause()
            time.sleep(2)
            pygame.quit()
            sys.exit()

        # checking when player collects coins, increasing score and redrawing coin
        if pygame.sprite.spritecollideany(player_car, coin_group):
            score += 1
            for coin in coin_group:
                coin.kill()
            coin = Coin()
            coin_group.add(coin)
            all_sprites.add(coin)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()