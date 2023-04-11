import numpy as np
import pygame
import random
import sys
from pygame import Rect
from pygame.math import Vector2

fps = 60
cell_size = 25
row_number = 20
col_number = 30
screen_size = (cell_size * col_number, cell_size * row_number)
speed = 150
level = 1


# Class inherited from Sprite for Fruit object
class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.randomize()

    # drawing fruit
    def draw(self, surf):
        surf.blit(self.image, self.rect)

    # randomly placing fruit
    def randomize(self):
        self.pos = Vector2(random.randint(1, col_number - 1), random.randint(1, row_number - 1))
        self.image = pygame.transform.scale(pygame.image.load('cherry.png'), (cell_size, cell_size))
        # create rectangle
        self.rect = Rect(int(self.pos.x * cell_size), int(self.pos.y * cell_size), cell_size, cell_size)


# Sprite class inherited from pygame Sprite for Snake 
class Snake(pygame.sprite.Sprite):
    # Initializing snaek
    def __init__(self):
        super().__init__()
        # list that holds all snake body parts
        self.pos_list = [Vector2(8, 10), Vector2(7, 10), Vector2(6, 10)]
        # direction attribute for moving in a specific direction
        self.direction = Vector2(1, 0)

        # many attributes for different parts of snake for smooth visualization
        self.head_up = pygame.transform.scale(pygame.image.load("head.png"), (cell_size, cell_size))
        self.head_down = pygame.transform.scale(pygame.image.load("head_down.png"), (cell_size, cell_size))
        self.head_right = pygame.transform.scale(pygame.image.load("head_right.png"), (cell_size, cell_size))
        self.head_left = pygame.transform.scale(pygame.image.load("head_left.png"), (cell_size, cell_size))

        self.tail_up = pygame.transform.scale(pygame.image.load("tail.png"), (cell_size, cell_size))
        self.tail_down = pygame.transform.scale(pygame.image.load("tail_down.png"), (cell_size, cell_size))

        self.tail_right = pygame.transform.scale(pygame.image.load("tail_right.png"), (cell_size, cell_size))
        self.tail_left = pygame.transform.scale(pygame.image.load("tail_left.png"), (cell_size, cell_size))

        self.body_vertical = pygame.transform.scale(pygame.image.load("body_vrt.png"), (cell_size, cell_size))
        self.body_horizontal = pygame.transform.scale(pygame.image.load("body_hr.png"), (cell_size, cell_size))

        self.body_tr = pygame.transform.scale(pygame.image.load("body_tr.png"), (cell_size, cell_size))
        self.body_tl = pygame.transform.scale(pygame.image.load("body_tl.png"), (cell_size, cell_size))
        self.body_br = pygame.transform.scale(pygame.image.load("body_br.png"), (cell_size, cell_size))
        self.body_bl = pygame.transform.scale(pygame.image.load("body_bl.png"), (cell_size, cell_size))

        self.head = self.head_right
        self.tail = self.tail_right

        # sound attributed for fruit eating sound
        self.sound = pygame.mixer.Sound('munch.mp3')
        # snake speed attribute
        self.speed = 200

    # drawing snake 
    def draw(self, surf):
        for i, pos in enumerate(self.pos_list):
            # Rect for positioning
            rect = Rect(int(pos.x * cell_size), int(pos.y * cell_size), cell_size, cell_size)
            # comples drawing of snake based on many different conditions
            if i == 0:
                self.update_head_graphics()
                surf.blit(self.head, rect)
            elif i == len(self.pos_list) - 1:
                self.update_tail_graphics()
                surf.blit(self.tail, rect)
            else:
                prev_pos = self.pos_list[i + 1] - pos
                next_pos = self.pos_list[i - 1] - pos

                if prev_pos.y == next_pos.y:
                    surf.blit(self.body_vertical, rect)
                elif prev_pos.x == next_pos.x:
                    surf.blit(self.body_horizontal, rect)
                else:
                    if prev_pos.x == -1 and next_pos.y == -1 or prev_pos.y == -1 and next_pos.x == -1:
                        surf.blit(self.body_tl, rect)
                    if prev_pos.x == -1 and next_pos.y == 1 or prev_pos.y == 1 and next_pos.x == -1:
                        surf.blit(self.body_bl, rect)
                    if prev_pos.x == 1 and next_pos.y == -1 or prev_pos.y == -1 and next_pos.x == 1:
                        surf.blit(self.body_tr, rect)
                    if prev_pos.x == 1 and next_pos.y == 1 or prev_pos.y == 1 and next_pos.x == 1:
                        surf.blit(self.body_br, rect)

    # method for moving snake
    def move(self):
        # copy the list of snake body parts
        pos_list_copy = self.pos_list[:-1]
        # add additional element at the end of the snake
        pos_list_copy.insert(0, pos_list_copy[0] + self.direction)
        # assign the modified list to the attribute list
        self.pos_list = pos_list_copy

    # snake eating fruit and increasing its size by 1
    def eat(self):
        pos_list_copy = self.pos_list[:]
        last_index = len(pos_list_copy) - 1
        pos_list_copy.insert(last_index, pos_list_copy[last_index] + self.direction)
        self.pos_list = pos_list_copy

        if self.speed > 100:
            self.speed = self.speed - 10 * level

        pygame.time.set_timer(screen_update, self.speed)

    # updating snake head graphics for correct visuals depending on the direction of snake
    def update_head_graphics(self):
        if self.direction == Vector2(0, -1):
            self.head = self.head_up
        elif self.direction == Vector2(0, 1):
            self.head = self.head_down
        elif self.direction == Vector2(1, 0):
            self.head = self.head_right
        elif self.direction == Vector2(-1, 0):
            self.head = self.head_left

    # updating tail graphics depending on the tail position and direction
    def update_tail_graphics(self):
        tail_direction = self.pos_list[-2] - self.pos_list[-1]

        if tail_direction == Vector2(0, -1):
            self.tail = self.tail_up
        if tail_direction == Vector2(0, 1):
            self.tail = self.tail_down
        if tail_direction == Vector2(1, 0):
            self.tail = self.tail_right
        if tail_direction == Vector2(-1, 0):
            self.tail = self.tail_left

    # playing eating sound
    def play_sound(self):
        self.sound.play()

    # reset method in the case of game over
    def reset(self):
        self.pos_list = [Vector2(8, 10), Vector2(7, 10), Vector2(6, 10)]
        self.speed = 150
        pygame.time.set_timer(screen_update, self.speed)


# Class with general logic of the game
class GameLogic:
    # initializing snake and fruit instances
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.map = np.ones((col_number, row_number))
        self.map[1:-1, 1:-1] = np.random.choice([0, 1], size=(col_number - 2, row_number - 2),
                                                p=[(100 - 5 * level) / 100, level * 5 / 100])
        self.walls_list = []

    # updating the state of the game
    def update(self):
        self.snake.move()
        self.check_collision()
        self.check_fail_states()

    # drawing game elements
    def draw_elements(self, surf, font, score_text):
        self.draw_dirt(surf)
        self.draw_walls(surf)
        self.snake.draw(surf)
        self.fruit.draw(surf)
        self.draw_score(surf, score_text, font)

    # checking for collision of snake with fruit
    def check_collision(self):
        if self.fruit.pos == self.snake.pos_list[0]:
            self.fruit.randomize()
            self.snake.eat()
            self.snake.play_sound()

        for pos in self.snake.pos_list:
            if pos == self.fruit.pos:
                self.fruit.randomize()

        for wall in self.walls_list:
            if wall == self.fruit.pos:
                self.fruit.randomize()

    # method running game over case
    def game_over(self):
        self.snake.reset()

    # method for checking all game over states
    def check_fail_states(self):
        # checking if snake collides with walls
        if not 0 <= self.snake.pos_list[0].x < col_number or not 0 <= self.snake.pos_list[0].y < row_number:
            self.game_over()

        # checking if snake head collides with itself
        for snake_part in self.snake.pos_list[1:]:
            if snake_part == self.snake.pos_list[0]:
                self.game_over()
        # if snake hits walls
        for wall in self.walls_list:
            if wall == self.snake.pos_list[0]:
                self.game_over()

    # method for drawing score on the screen
    def draw_score(self, surf, score_text, font):
        score_text = f"""{len(self.snake.pos_list) - 3} / {level} lvl"""
        score_surf = font.render(score_text, True, (56, 76, 12))
        score_surf_pos = (int(cell_size * col_number - 40), int(cell_size * row_number - 20))
        score_rect = score_surf.get_rect(center=score_surf_pos)
        surf.blit(score_surf, score_rect)
        apple = self.fruit.image
        apple_rect = apple.get_rect(midright=(score_rect.left, score_rect.centery))
        surf.blit(apple, apple_rect)

    # method for drawing dirt on the ground
    def draw_dirt(self, surf):
        dirt_color = (150, 105, 65)
        for row in range(row_number):
            if row % 2 == 0:
                for col in range(0, col_number, 2):
                    dirt_rect = Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(surf, dirt_color, dirt_rect)
            else:
                for col in range(1, col_number, 2):
                    dirt_rect = Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                    pygame.draw.rect(surf, dirt_color, dirt_rect)

    # method for drawing walls
    def draw_walls(self, surf):
        wall_img = pygame.image.load('wall.png')
        wall_img = pygame.transform.scale(wall_img, (cell_size, cell_size))
        wall_rect = wall_img.get_rect()
        for i, y in enumerate(self.map):
            for j, x in enumerate(y):
                if x == 1:
                    self.walls_list.insert(0, Vector2(i, j))
                    wall_rect.topleft = (i * cell_size, j * cell_size)
                    surf.blit(wall_img, wall_rect)


# main method of the game
def main():
    # initializing pygame module
    pygame.init()

    # initialzing screen object
    screen = pygame.display.set_mode(screen_size)

    # initializing clock object
    clock = pygame.time.Clock()

    # initialzing the general game logic 
    snake_game = GameLogic()
    # adding font for score
    game_font = pygame.font.Font('Blessed.ttf', 20)

    # screen update for checking every user event to 
    global screen_update, level
    screen_update = pygame.USEREVENT

    # setting timer on user event for artificial laggy gameplay
    pygame.time.set_timer(screen_update, speed)

    while True:
        # running for every user input
        for event in pygame.event.get():
            # quit event type
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # updating the game on each user event
            if event.type == screen_update:
                snake_game.update()
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_UP:
                        if snake_game.snake.direction != Vector2(0, 1):
                            snake_game.snake.direction = Vector2(0, -1)
                    case pygame.K_DOWN:
                        if snake_game.snake.direction != Vector2(0, -1):
                            snake_game.snake.direction = Vector2(0, 1)
                    case pygame.K_RIGHT:
                        if snake_game.snake.direction != Vector2(-1, 0):
                            snake_game.snake.direction = Vector2(1, 0)
                    case pygame.K_LEFT:
                        if snake_game.snake.direction != Vector2(1, 0):
                            snake_game.snake.direction = Vector2(-1, 0)
        # calculating the score
        score = str(len(snake_game.snake.pos_list) - 3)
        # increasing level and resetting the game
        if score == 5:
            level += 1
            score = 0
            snake_game = GameLogic()
            snake_game.game_over()
        screen.fill((173, 121, 75))
        snake_game.draw_elements(screen, game_font, score)
        pygame.display.update()
        clock.tick(fps)


if __name__ == "__main__":
    main()
