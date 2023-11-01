import pygame

from images import right_images, left_images, down_images, up_images, WIDTH, HEIGHT


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = down_images[1]
        self.rect = self.image.get_rect()
        self.rect.center = (100, 100)
        self.speed = 10
        self.frame = 0
        self.count_frames = 3

    def update(self, **kwargs):
        keys = kwargs["keys"]

        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH:
            self.rect.x += self.speed
            self.image = right_images[self.frame]
        elif keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
            self.image = left_images[self.frame]
        elif keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
            self.image = up_images[self.frame]
        elif keys[pygame.K_DOWN] and self.rect.y < 500:
            self.rect.y += self.speed
            self.image = down_images[self.frame]
        else:
            self.image = down_images[1]

        self.frame += 1
        self.frame %= self.count_frames
