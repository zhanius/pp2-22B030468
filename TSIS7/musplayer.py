import pygame
import sys
from pygame import mixer

class InterfaceElement(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, image):
        super().__init__()
        self.image = pygame.image.load(f"{image}")
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


def main():

    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    pygame.display.set_caption('Music player')
    isMusicOn = False
    isFirstPlayed = False
    songs_list = ['gorillaz_tranz.mp3', 'parcels_overnight.mp3','dark_necessities_rhcp.mp3']
    i = 0
    mixer.init()

    # button images
    album_logo = InterfaceElement(400, 200, "logoo.png")
    play_btn = PlayButton(400, 400, "play_button.png")
    pause_btn = PauseButton(400, 400, "pause_button.png")
    prev_btn = PrevButton(300, 400, "prev_button.png")
    next_btn = NextButton(500, 400, "next_button.png")
    
    btn_list = [pause_btn, prev_btn, next_btn]

    interface_elements_group = pygame.sprite.Group()

    for btn in btn_list:
        interface_elements_group.add(btn)

    while True:
        for event in pygame.event.get():
            match event.type:
                case pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                case pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_SPACE:
                            if not isMusicOn:
                                if not isFirstPlayed:
                                    mixer.music.load(songs_list[i])
                                    mixer.music.play()
                                    isFirstPlayed = True
                                    interface_elements_group.add(album_logo)
                                    interface_elements_group.remove(play_btn)
                                    interface_elements_group.add(pause_btn)
                                else:
                                    mixer.music.unpause()
                                    interface_elements_group.remove(play_btn)
                                    interface_elements_group.add(pause_btn)
                            else:
                                mixer.music.pause()
                                interface_elements_group.remove(pause_btn)
                                interface_elements_group.add(play_btn)

                            isMusicOn = not isMusicOn

                        case pygame.K_RIGHT:
                            if i < len(songs_list) - 1:
                                i += 1
                            else:
                                i = 0
                            mixer.music.load(songs_list[i])
                            mixer.music.play()

                            if not interface_elements_group.has(play_btn):
                                interface_elements_group.remove(pause_btn)
                                interface_elements_group.add(play_btn)
                        case pygame.K_LEFT:
                            if i > 0:
                                i -= 1
                            else:
                                i = len(songs_list) - 1
                            if not interface_elements_group.has(play_btn):
                                interface_elements_group.remove(pause_btn)
                                interface_elements_group.add(play_btn)
                            mixer.music.load(songs_list[i])
                            mixer.music.play()

                case pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()

                    if 370 < mouse_x < 430 and 370 < mouse_y < 430:
                        if not isMusicOn:
                            if not isFirstPlayed:
                                mixer.music.load(songs_list[i])
                                mixer.music.play()
                                isFirstPlayed = True
                                interface_elements_group.add(album_logo)
                            else:
                                mixer.music.unpause()
                            interface_elements_group.remove(play_btn)
                            interface_elements_group.add(pause_btn)
                        else:
                            mixer.music.pause()
                            interface_elements_group.remove(pause_btn)
                            interface_elements_group.add(play_btn)
                        isMusicOn = not isMusicOn

                    if 470 < mouse_x < 530 and 370 < mouse_y < 430:
                        if i < len(songs_list) - 1:
                            i += 1
                        else:
                            i = 0
                        mixer.music.load(songs_list[i])
                        mixer.music.play()
                        if not interface_elements_group.has(play_btn):
                            interface_elements_group.remove(pause_btn)
                            interface_elements_group.add(play_btn)

                    if 270 < mouse_x < 330 and 370 < mouse_y < 430:
                        if i > 0:
                            i -= 1
                        else:
                            i = len(songs_list) - 1
                        if not interface_elements_group.has(play_btn):
                            interface_elements_group.remove(pause_btn)
                            interface_elements_group.add(play_btn)
                        mixer.music.load(songs_list[i])
                        mixer.music.play()

        screen.fill((0, 0, 0))
        interface_elements_group.draw(screen)
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
