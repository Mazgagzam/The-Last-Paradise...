import pygame

from images import background, background2


class Background(pygame.sprite.Sprite):
    def __init__(self, start_react):
        pygame.sprite.Sprite.__init__(self)
        self.start_react = start_react

        self.image = background2
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

        self.menu = True
        self.FPS = 60

    def update1(self, **kwargs):
        keys = kwargs["keys"]
        events = kwargs["events"]

        if keys[pygame.K_r]:
            self.image = background2
            self.menu = True
            self.FPS = 60

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_react.collidepoint(event.pos):
                    self.image = background
                    self.menu = False
                    self.FPS = 6
