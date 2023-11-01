import pygame
import base64, io


# Цвета
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)

WIDTH = 960
HEIGHT = 640


def delete_white(*args):
    for arg in args:
        if isinstance(arg, list):
            for element in arg:
                element.set_colorkey(white)
            continue

        arg.set_colorkey(white)


def text_image(text: str):
    image_data = base64.b64decode(text)
    return pygame.image.load(io.BytesIO(image_data))


right_images = [
    pygame.image.load("person2/right1.png"),
    pygame.image.load("person2/right2.png"),
    pygame.image.load("person2/right3.png"),
]

left_images = [
    pygame.image.load("person2/left1.png"),
    pygame.image.load("person2/left2.png"),
    pygame.image.load("person2/left3.png"),
]

up_images = [
    pygame.image.load("person2/up1.png"),
    pygame.image.load("person2/back.png"),
    pygame.image.load("person2/up2.png"),
]

down_images = [
    pygame.image.load("person2/down1.png"),
    pygame.image.load("person2/front.png"),
    pygame.image.load("person2/down2.png"),
]
delete_white(down_images, up_images, right_images, left_images)
count_frames = 3

background = pygame.image.load("person2/background.png")
background2 = pygame.image.load("person2/background2.png")

start_image = pygame.image.load("person2/start.png")
