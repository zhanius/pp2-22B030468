from collections import namedtuple
import pygame
import sys

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

Point = namedtuple('Point', ['x', 'y'])


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class GameObject:
    def update(self, curr_point):
        return

    def draw(self):
        return


class RectButton(GameObject):
    def __init__(self):
        self.width = 50
        self.rect = pygame.Rect(SCREEN_HEIGHT // 2 - self.width // 2, 20, self.width, self.width)

    def draw(self, surf):
        pygame.draw.rect(surf, (255, 0, 0), self.rect)


class CircleButton(GameObject):
    def __init__(self):
        self.radius = 25
        self.rect = pygame.draw.circle(screen, (255, 0, 0), (SCREEN_HEIGHT // 2 + 2 * self.radius, self.radius + 20),
                                       self.radius)

    def draw(self, surf):
        pygame.draw.circle(screen, (255, 0, 0), (SCREEN_HEIGHT // 2 + 2 * self.radius, self.radius + 20), self.radius)


class Pen(GameObject):
    def __init__(self, *args, **kwargs):
        self.points: list(Point, ...) = []

    def draw(self, surf):
        for id, curr_point in enumerate(self.points[:-1]):
            next_point = self.points[id + 1]
            pygame.draw.line(surf, (0, 0, 0),
                             (curr_point.x, curr_point.y), (next_point.x, next_point.y), width=5)

    def update(self, curr_point):
        self.points.append(Point(*curr_point))


class Rectangle(GameObject):
    def __init__(self, init_point, *args, **kwargs):
        self.start_point = Point(*init_point)
        self.end_point = Point(*init_point)

    def draw(self, surf):
        start_point_x = min(self.start_point.x, self.end_point.x)
        start_point_y = min(self.start_point.y, self.end_point.y)

        end_point_x = max(self.start_point.x, self.end_point.x)
        end_point_y = max(self.start_point.y, self.end_point.y)

        pygame.draw.rect(surf, (0, 0, 0),
                         (start_point_x, start_point_y, end_point_x - start_point_x, end_point_y - start_point_y),
                         width=5)

    def update(self, curr_point):
        self.end_point.x, self.end_point.y = curr_point


class Circle(GameObject):
    def __init__(self, init_point, *args, **kwargs):
        self.center_point = Point(*init_point)
        self.radius = 0
        self.circle = pygame.draw.circle(screen, (0, 0, 0), init_point, self.radius, width=5)

    def draw(self, surf):
        pygame.draw.circle(surf, (0, 0, 0), (self.center_point.x, self.center_point.y), self.radius, width=5)

    def update(self, curr_point):
        self.radius = curr_point[0] - self.center_point.x


def main():
    game_obj = GameObject()
    active_obj = game_obj
    curr_shape = Pen
    rect_button = RectButton()
    circle_button = CircleButton()
    objects = [rect_button, circle_button]

    while True:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect_button.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = Rectangle
                elif circle_button.rect.collidepoint(pygame.mouse.get_pos()):
                    curr_shape = Circle
                else:
                    active_obj = curr_shape(init_point=pygame.mouse.get_pos())
                    objects.append(active_obj)
            if event.type == pygame.MOUSEMOTION:
                active_obj.update(curr_point=pygame.mouse.get_pos())
            if event.type == pygame.MOUSEBUTTONUP:
                active_obj = game_obj

            for obj in objects:
                obj.draw(screen)

            pygame.display.flip()
            clock.tick(FPS)


if __name__ == "__main__":
    main()
