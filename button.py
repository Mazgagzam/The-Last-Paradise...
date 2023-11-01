import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, **kwargs):
        if not kwargs["start"]:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(255)
