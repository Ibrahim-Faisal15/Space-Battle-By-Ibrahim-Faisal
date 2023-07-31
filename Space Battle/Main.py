import pygame
from pygame.locals import *
import sys
import Classes

pygame.init()
pygame.font.init()
Clock = pygame.time.Clock()

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# DISPLAY
WIDTH, HEIGHT = 900, 600
SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
CAPTION = pygame.display.set_caption("Space Battle by @Ibrahim Faisal")

# Background
image = pygame.image.load("space.jpg")
image2 = pygame.image.load("download.jpeg")
image = pygame.transform.smoothscale(image, (900, 600))
image2 = pygame.transform.smoothscale(image2, (WIDTH, HEIGHT))

bg1 = pygame.image.load("bois.png")
bg1 = pygame.transform.smoothscale(bg1, (900, 600))

bg2 = pygame.image.load("bois2.png")
bg2 = pygame.transform.smoothscale(bg2, (900, 600))


def welcome():
    main()


def main():
    global Keys
    Run = True

    font = pygame.font.Font(None, 30)

    # Player_img
    player_img = pygame.image.load("spaceship.png")
    player2_img = pygame.image.load("spaceship2.png")

    # Bullets_img
    bullet_img = pygame.image.load("bullet.png")
    bullet_img2 = pygame.image.load("bullet2.png")
    bullets = []
    bullets2 = []

    # Player_1
    Spaceship_1 = Classes.Player_1(75, HEIGHT // 2, player_img, SURFACE)
    Spaceship_2 = Classes.Player_2(75 * 10, HEIGHT // 2, player2_img, SURFACE)

    shooting1 = False
    shooting2 = False

    shoot_timer1 = 1
    shoot_timer2 = 0

    health_1 = 10
    health_2 = 10

    game_over = False

    Player_1_lose = False
    Player_2_lose = False

    shoot_delay = 300

    font2 = pygame.font.SysFont("Dungeon", 45)

    while Run:
        if game_over:
            # SURFACE.fill(WHITE)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    Run = False
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_x:
                        welcome()
            if Player_1_lose:
                SURFACE.blit(image2, (0, 0))
                Lose = font2.render("Player 1 loses", True, (WHITE))
                SURFACE.blit(Lose, (WIDTH - 610, 325))
                SURFACE.blit(bg2, (0, 0))

            elif Player_2_lose:
                SURFACE.blit(image2, (0, 0))
                Lose = font2.render("Player 2 loses", True, (WHITE))
                SURFACE.blit(Lose, (WIDTH - 610, 325))
                SURFACE.blit(bg1, (0, 0))
            pygame.display.update()

        else:
            for event in pygame.event.get():
                if event.type == QUIT:
                    Run = False
                    sys.exit()

                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        shooting1 = True
                    elif event.key == K_RETURN:
                        shooting2 = True

                elif event.type == KEYUP:
                    if event.key == K_SPACE:
                        shooting1 = False
                    elif event.key == K_RETURN:
                        shooting2 = False

            Keys = pygame.key.get_pressed()

            if shooting1 and pygame.time.get_ticks() - shoot_timer1 > shoot_delay:
                new_bullet1 = Classes.Bullet1(
                    Spaceship_1.rect.right, Spaceship_1.rect.centery, 10, bullet_img
                )
                bullets.append(new_bullet1)
                shoot_timer1 = pygame.time.get_ticks()

            if shooting2 and pygame.time.get_ticks() - shoot_timer2 > shoot_delay:
                new_bullet2 = Classes.Bullet2(
                    Spaceship_2.rect.right, Spaceship_2.rect.centery, 10, bullet_img2
                )
                bullets2.append(new_bullet2)
                shoot_timer2 = pygame.time.get_ticks()

            Spaceship_1.Move(Keys)
            Spaceship_2.Move()

            # BACKGROUND
            SURFACE.blit(image, (0, 0))

            for bullet in bullets:
                bullet.update()
                if new_bullet1.hit(Spaceship_2, 1):
                    bullets.remove(bullet)
                    health_2 -= 2
                    if health_2 <= 0:
                        game_over = True
                        Player_2_lose = True
                SURFACE.blit(bullet_img, bullet.rect)

            for bullet in bullets2:
                bullet.update()
                if new_bullet2.hit(Spaceship_1, 1):
                    bullets2.remove(bullet)
                    health_1 -= 2
                    if health_1 <= 0:
                        game_over = True
                        Player_1_lose = True
                SURFACE.blit(bullet_img2, bullet.rect)

            Spaceship_1.Borders()
            Spaceship_1.Draw()

            Spaceship_2.Borders()
            Spaceship_2.Draw()

            # Line
            pygame.draw.line(
                SURFACE, (100, 100, 100), (WIDTH / 2, 0), (WIDTH / 2, 600), 8
            )

            # Display player health

            health_text = font.render(
                f"Remaining Health: {health_1}", True, (255, 255, 255)
            )
            SURFACE.blit(health_text, (10, 10))

            health_text2 = font.render(
                f"Remaining Health: {health_2}", True, (255, 255, 255)
            )
            SURFACE.blit(health_text2, (WIDTH - 250, 10))

            pygame.display.update()
            Clock.tick(60)


if __name__ == "__main__":
    main()
