import pygame
import math
import random
from pygame import mixer

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load("space_background.png")

mixer.music.load("Mr Snorty pig.wav")
mixer.music.play(-1)

running = True

pygame.display.set_caption("most annoying game in the world")
icon = pygame.image.load("lightsaber_logo.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load("space-invaders.png")
player_x = 370
player_y = 480
player_change = 0

enemyImg = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
number_of_enemies = 6
enemy_x_change_2 = 0

for i in range(number_of_enemies):
    enemyImg.append(pygame.image.load("ghost.png"))
    enemy_x.append(random.randint(0, 736))
    enemy_y.append(random.randint(50, 150))
    enemy_x_change.append(0.5)
    enemy_y_change.append(48)

# ready - the bullet is ready to be shot and you cant see it
# fire - the bullet is currently moving

bulletImg = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 480
bullet_x_change = 0
bullet_y_change = 5
bullet_state = "ready"

# score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 50)

text_x = 10
text_y = 10

game_over_font = pygame.font.Font("freesansbold.ttf", 70)


def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# game over function
def game_over_text():
    over_text = game_over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def is_collision(enemy_x, enemy_y, bullet_x, bullet_y):
    distance = math.sqrt((math.pow(enemy_x - bullet_x, 2)) + math.pow(enemy_y - bullet_y, 2))
    if distance <= 27:
        return True
    else:
        return False


while running:

    # Rgb red, green, blue
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_change = -4
            if event.key == pygame.K_RIGHT:
                player_change = 4
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound("Shut up.wav")
                    bullet_sound.play()
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_change = 0

    player_x += player_change
    enemy_x += enemy_x_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 736:
        player_x = 736

    # enemy movement
    for i in range(number_of_enemies):

        if enemy_y[i] > 440:
            for i in range(number_of_enemies):
                enemy_y[i] = 2000
            game_over_text()
            break

        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0:
            enemy_x_change[i] = 0.5 + enemy_x_change_2
            enemy_y[i] += enemy_y_change[i]
        elif enemy_x[i] >= 736:
            enemy_x_change[i] = -0.5 + -enemy_x_change_2
            enemy_y[i] += enemy_y_change[i]

        collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            collision_sound = mixer.Sound("Pig brigade.wav")
            collision_sound.play()
            bullet_y = 480
            bullet_state = "ready"
            score_value += 1
            enemy_x_change_2 += 0.1
            enemy_x[i] = random.randint(0, 736)
            enemy_y[i] = random.randint(50, 150)

        enemy(enemy_x[i], enemy_y[i], i)

    if bullet_state is "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_y_change

    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"

    player(player_x, player_y)
    show_score(text_x, text_y)
    pygame.display.update()
