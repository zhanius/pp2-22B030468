import pygame


class InterfaceElement(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image):
        super().__init__()
        self.image = pygame.image.load()
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.isPressed = False


class PlayButton(InterfaceElement):
    def __init__(self, pos_x, pos_y, image):
        super().__init__(pos_x, pos_y, image)


class PauseButton(InterfaceElement):
    def __init__(self, pos_x, pos_y, image):
        super().__init__(pos_x, pos_y, image)


class PrevButton(InterfaceElement):
    def __init__(self, pos_x, pos_y, image):
        super().__init__(pos_x, pos_y, image)


class NextButton(InterfaceElement):
    def __init__(self, pos_x, pos_y, image):
        super().__init__(pos_x, pos_y, image)


class ShuffleButton(InterfaceElement):
    def __init__(self, pos_x, pos_y, image):
        super().__init__(pos_x, pos_y, image)


class VolumeUpButton(InterfaceElement):
    def __init__(self, pos_x, pos_y, image):
        super().__init__(pos_x, pos_y, image)
