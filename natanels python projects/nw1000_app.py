import pygame
import math
import random
from pygame import mixer

sound = True
music = True

main = True

while main:
    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    background = pygame.image.load("space_background.png")

    pygame.mouse.set_cursor(*pygame.cursors.arrow)
    pygame.mouse.set_visible(True)

    #sound = True
    #music = True

    settings = False
    running = False

    home = True
    out = False
    bomb_activated = False
    bomb_activation = False

    pygame.display.set_caption("nw1000 app")
    icon = pygame.image.load("lightsaber_logo.png")
    pygame.display.set_icon(icon)

    transparent = (0, 0, 0, 0)
    bomb_charge = 0
    bomb_mode = False

    onSwitch_image = pygame.image.load("on_switch.png")
    offSwitch_image = pygame.image.load("off_switch.png")

    back_arrow = pygame.image.load("back_arrow.png")
    back_arrow_x = 670
    back_arrow_y = 50

    bombImg = pygame.image.load("bomb.jpeg")
    bomb_x = 10
    bomb_y = 10

    playImg = pygame.image.load("Play_Button.png")
    play_x = 225
    play_y = 225

    settingsImg = pygame.image.load("settings.png")
    settings_x = 336
    settings_y = 390

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
    font = pygame.font.SysFont("calibri.ttf", 70)

    text_x = 10
    text_y = 10

    game_over_font = pygame.font.SysFont("calibri.ttf", 110)
    score_font = pygame.font.SysFont("calibri.ttf", 70)
    score_font_game_over = pygame.font.SysFont("calibri.ttf", 90)
    bomb_charged_font = pygame.font.SysFont("calibri.ttf", 50)
    settings_font = pygame.font.SysFont("calibri.ttf", 70)
    settings_title_font = pygame.font.SysFont("calibri.ttf", 110)


    def button_clicked(button_coordinates_x, button_coordinates_y, width, height):
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_coordinates_x + height > mouse_position[0] > button_coordinates_x and button_coordinates_y + width > mouse_position[1] > button_coordinates_y:
                    return True


    def show_score(x, y):
        score = font.render("Score : " + str(score_value), True, (255, 255, 255))
        screen.blit(score, (x, y))


    # game over function
    def game_over_text():
        over_text = game_over_font.render("GAME OVER", True, (0, 0, 0))
        screen.blit(over_text, (175, 250))


    def high_score_text():
        over_text = game_over_font.render("HIGH SCORE", True, (0, 0, 0))
        screen.blit(over_text, (175, 250))


    def settings_title():
        title_text = settings_title_font.render("Settings", True, (255, 255, 255))
        screen.blit(title_text, (225, 50))


    def settings_text(text, line):
        setting_text = settings_font.render(text, True, (255, 255, 255))
        y = line * 70 + 100
        screen.blit(setting_text, (190, y))


    def bomb_activated_text(x, y):
        over_text = bomb_charged_font.render("bomb activated", True, (255, 255, 255))
        screen.blit(over_text, (x, y))


    def last_score():
        last_score_value = open("score.txt", "r")
        is_readable = last_score_value.readable()
        if is_readable:
            last_score_value_text = last_score_value.read()

        last_score_text = score_font.render("last score: " + last_score_value_text, True, (255, 255, 255))
        screen.blit(last_score_text, (245, 150))


    def your_score():
        last_score_value = open("score.txt", "r")
        is_readable = last_score_value.readable()
        if is_readable:
            last_score_value_text = last_score_value.read()

        last_score_text = score_font_game_over.render("you scored " + last_score_value_text, True, (0, 0, 0))
        screen.blit(last_score_text, (200, 140))


    def high_score():
        high_score_num = open("high_score.txt", "r")
        is_readable = high_score_num.readable()
        if is_readable:
            high_score_value_text = high_score_num.read()

        high_score_text = score_font.render("high score: " + high_score_value_text, True, (255, 255, 255))
        screen.blit(high_score_text, (236, 100))


    def bomb_charged(x, y):

            score = bomb_charged_font.render("bomb charge: " + str(bomb_charge) + "/" + str(), True, (255, 255, 255))
            screen.blit(score, (x, y))



    def play_button(x, y):
        screen.blit(playImg, (x, y))


    def settings_button(x, y):
        screen.blit(settingsImg, (x, y))


    def back_button(x, y):
        screen.blit(back_arrow, (x, y))


    def on_switch(x, y):
        screen.blit(onSwitch_image, (x, y))


    def off_switch(x, y):
        screen.blit(offSwitch_image, (x, y))


    def bomb(x, y):
        screen.blit(bombImg, (x, y))


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


    def settings_switches_setup(setting, line):
        obj_y = line * 70 + 90
        obj_x = 540
        if setting is True:
            on_switch(obj_x, obj_y)
        elif setting is False:
            off_switch(obj_x, obj_y)


    def settings_click(setting, line):
        obj_y = line * 70 + 90
        obj_x = 540
        variable = setting

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            pygame.time.delay(75)
            if obj_x + 64 > mouse_pos[0] > obj_x and obj_y + 48 > mouse_pos[1] > obj_y + 16:
                if setting is False:
                    on_switch(obj_x, obj_y)
                    variable = True
                elif setting is True:
                    off_switch(obj_x, obj_y)
                    variable = False

        return variable


    while home:

        screen.fill((0, 0, 0))
        play_button(play_x, play_y)
        settings_button(settings_x, settings_y)
        pygame.mouse.set_visible(True)
        last_score()
        high_score()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                home = False
                running = False
                settings = False
                main = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_x + 350 > mouse_pos[0] > play_x and play_y + 150 > mouse_pos[1] > play_y:
                    running = True
                    home = False

                if settings_x + 128 > mouse_pos[0] > settings_x and settings_y + 128 > mouse_pos[1] > settings_y:
                    settings = True
                    home = False

    if event.type == pygame.QUIT:
        home = False
        running = False
        main = False

    if running:
        bomb_value = 30
        mixer.music.load("background.wav")
        if music is True:
            mixer.music.play(-1)

    if home:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                home = False
                running = False
                main = False

    while settings:
        back = False
        screen.fill((0, 0, 0))
        settings_title()
        back_button(back_arrow_x, back_arrow_y)

        settings_text("sound", 1)
        settings_text("music", 2)

        settings_switches_setup(sound, 1)
        sound = settings_click(sound, 1)
        print(sound)
        settings_switches_setup(music, 2)
        music = settings_click(music, 2)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                home = False
                running = False
                settings = False
                main = False
            mouse_position = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_arrow_x + 63 > mouse_position[0] > back_arrow_x and back_arrow_y + 100 > mouse_position[1] > back_arrow_y:
                    home = True
                    settings = False

    while running:
        print("its running")
        # Rgb red, green, blue
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))
        pygame.mouse.set_visible(False)

        bomb_charge = score_value

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                main = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_change = -4
                if event.key == pygame.K_RIGHT:
                    player_change = 4
                if event.key == pygame.K_SPACE:
                    if bullet_state == "ready":
                        bullet_sound = mixer.Sound("laser.wav")
                        if sound is True:
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
            # game over
            if enemy_y[i] > 420:

                high_score_num = open("high_score.txt", "r")
                is_readable = high_score_num.readable()
                if is_readable:
                    high_score_value_text = high_score_num.read()

                for i in range(number_of_enemies):
                    if int(high_score_value_text) < score_value:
                        high_score_num = open("high_score.txt", "w")
                        high_score_num.write(str(score_value))
                        high_score_num.close()

                        score_num = open("score.txt", "w")
                        score_num.write(str(score_value))
                        score_num.close()

                        high_score_bool = True
                        out = True
                        running = False
                    else:
                        score_num = open("score.txt", "w")
                        score_num.write(str(score_value))
                        score_num.close()
                        high_score_bool = False
                        out = True
                        running = False

            enemy_x[i] += enemy_x_change[i]
            if enemy_x[i] <= 0:
                enemy_x_change[i] = 0.5 + enemy_x_change_2
                enemy_y[i] += enemy_y_change[i]
            elif enemy_x[i] >= 736:
                enemy_x_change[i] = -0.5 + -enemy_x_change_2
                enemy_y[i] += enemy_y_change[i]

            collision = is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
            if collision:
                collision_sound = mixer.Sound("explosion.wav")
                if sound is True:
                    collision_sound.play()

                bullet_y = 480
                bullet_state = "ready"
                score_value += 1
                enemy_x_change_2 += 0.1
                enemy_x[i] = random.randint(0, 736)
                enemy_y[i] = random.randint(50, 150)

            enemy(enemy_x[i], enemy_y[i], i)

        if bullet_state == "fire":
            fire_bullet(bullet_x, bullet_y)
            bullet_y -= bullet_y_change

        if bullet_y <= 0:
            bullet_y = 480
            bullet_state = "ready"

        if bomb_mode is False:
            print("bomb is ready for action")
            if score_value == current_charge:
                bomb_activation = True
                print("bomb activated")

            if bomb_activation is True:
                bomb_activated_text(280, 550)
                bomb_activated = True
                bomb_mode = False
                print("bomb mode is false")
                bomb_activation = False

        if bomb_activated:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_b:
                    bomb_mode = True
                    screen.fill((255, 255, 255))
                    pygame.display.update()
                    pygame.time.delay(1000)
                    running = True
                    bomb_activated = False

        if score_value != 40 and score_value != 50 and score_value != 60 and score_value != 70 and score_value != 2 and score_value != 1:
            bomb_mode = False

        player(player_x, player_y)
        show_score(text_x, text_y)
        bomb_charged(470, 10)
        pygame.display.update()

    while out:
        if high_score_bool == True:
            pygame.mixer.quit()
            screen.fill((0, 255, 0))
            high_score_text()
            your_score()
            pygame.display.update()
            pygame.time.delay(1000)
            home = True
            out = False
        else:
            pygame.mixer.quit()
            screen.fill((255, 0, 0))
            game_over_text()
            your_score()
            pygame.display.update()
            pygame.time.delay(1000)
            home = True
            out = False
