import pygame

from background import Background
from player import Player
from button import Button

from images import (
    right_images,
    left_images,
    up_images,
    down_images,
    background,
    background2,
    count_frames,
    start_image,
    WIDTH,
    HEIGHT
)

pygame.init()
pygame.font.init()

font = pygame.font.Font("fonts/undertale_battle_font.ttf", 20)
dialog = pygame.image.load("person2/dialogue.jpg")
dialog.set_colorkey((255, 255, 255))
dialog.set_alpha(150)

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("The Last Paradise...")

all_sprites = pygame.sprite.Group()

player = Player()
start = Button(start_image, 330, 280)
background = Background(start.rect)

all_sprites.add(background)
all_sprites.add(start)
all_sprites.add(player)

clock = pygame.time.Clock()


speed = 10
running = True
menu = False
panel = False
mouse = False

main_menu = True
while running:
    pygame.display.flip()
    clock.tick(background.FPS)

    events = pygame.event.get()
    keys = pygame.key.get_pressed()
    """
    if main_menu:
        screen.blit(background2, (0, 0))
        screen.blit(start_image, (330, 280))

        for event in events:
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_react.collidepoint(event.pos):
                    main_menu = False
                    FPS = 6

        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            main_menu = True
            FPS = 60

        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            menu = not menu

        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            panel = not panel

    # Очистка экрана (удаление предыдущего изображения)
    screen.blit(background, (0, 0))

    # Определение нажатых клавиш для управления анимацией

    keys = pygame.key.get_pressed()


    if menu:
        f = pygame.font.Font("fonts/undertale_battle_font.ttf", 16)
        text = f.render("Съешь этих французских булочек.", True,
                        (255, 0, 0))
        name = f.render("Султан", True,
                        (255, 255, 255))

        screen.blit(dialog, (-20, 530))

        rectangle = pygame.Surface((500, 75))
        rectangle.fill((53, 53, 53))
        rectangle.set_alpha(150)
        screen.blit(rectangle, (76, 575))

        screen.blit(name, (83, 553))
        screen.blit(text, (80, 580))
        down_images[1].set_colorkey((255, 255, 255))

        screen.blit(down_images[1], (0, 550))
    """
    background.update1(keys=keys, events=events)

    all_sprites.update(keys=keys, events=events, start=background.menu)
    all_sprites.draw(screen)

pygame.quit()
