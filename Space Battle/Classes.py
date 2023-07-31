import pygame
from Main import *


class Player_1:  # Spaceship 1
    def __init__(self, x, y, img_path, surface):
        self.img = img_path
        self.rect = self.img.get_rect()
        self.velocity_y = 0
        self.velocity_x = 0
        self.main_velocity = 3.8
        self.surface = surface

        self.rect.x = x
        self.rect.y = y

    def Draw(self):
        self.surface.blit(self.img, self.rect)

    def Borders(self):  # Borders
        if self.rect.y >= 540:
            self.rect.y = 540
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.x <= 0:
            self.rect.x = 0

        # Line Border
        if self.rect.x >= 382:
            self.rect.x = 382

    def Move(self, keys):
        if keys[pygame.K_w]:
            self.velocity_y = -self.main_velocity
        elif keys[pygame.K_a]:
            self.velocity_x = -self.main_velocity
        elif keys[pygame.K_s]:
            self.velocity_y = self.main_velocity
        elif keys[pygame.K_d]:
            self.velocity_x = self.main_velocity
        else:
            self.velocity_y = 0
            self.velocity_x = 0

        self.rect.y += self.velocity_y
        self.rect.x += self.velocity_x


class Player_2:  # Spaceship 2
    def __init__(self, x, y, img_path, surface):
        self.img = img_path
        self.rect = self.img.get_rect()
        self.velocity_y = 0
        self.velocity_x = 0
        self.main_velocity = 3.9
        self.surface = surface

        self.rect.x = x
        self.rect.y = y

    def Draw(self):
        self.surface.blit(self.img, self.rect)

    def Borders(self):  # Borders
        if self.rect.y >= 540:
            self.rect.y = 540
        if self.rect.y <= 0:
            self.rect.y = 0
        if self.rect.x >= 837:
            self.rect.x = 837

        # Line Border
        if self.rect.x <= 454:
            self.rect.x = 454

    def Move(self):
        keys = pygame.key.get_pressed()  # Get keypresses here
        if keys[pygame.K_UP]:
            self.velocity_y = -self.main_velocity
        elif keys[pygame.K_LEFT]:
            self.velocity_x = -self.main_velocity
        elif keys[pygame.K_DOWN]:
            self.velocity_y = self.main_velocity
        elif keys[pygame.K_RIGHT]:
            self.velocity_x = self.main_velocity
        else:
            self.velocity_y = 0
            self.velocity_x = 0

        self.rect.y += self.velocity_y
        self.rect.x += self.velocity_x


class Bullet1:
    def __init__(self, x, y, speed, image):
        self.rect = image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed

    def update(self):
        self.rect.x += self.speed

    def hit(self, player_rect, health):
        if self.rect.colliderect(player_rect):
            return True
        return False


class Bullet2(Bullet1):
    def __init__(self, x, y, speed, image):
        self.rect = image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed

    def update(self):
        self.rect.x -= self.speed

    def hit(self, player_rect, health):
        if self.rect.colliderect(player_rect):
            return True
        return False
