import pygame
import random
import sys

pygame.init()
pygame.mouse.set_visible(False)

# Colors
red = (255, 0, 0)           # color for warning messages
green_light = (9, 230, 24)  # color for snake.....
green_dark = (69, 161, 86)
black = (0, 0, 0)
blue = (37, 107, 219)
yellow = (250, 218, 7)
white = (255, 255, 255)

font = "twcen"

# Screen size
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 900

# for total duration
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("The Snake Game")


def leave_game():
    pygame.quit()
    sys.exit(0)


def draw_snake(snake_body):   # draw's the body of snake
    block = 20

    for x in snake_body:
        pygame.draw.rect(screen, green_light, (x[0], x[1], block, block))

    # draws snake head and eyes
    pygame.draw.rect(screen, green_dark, (snake_body[-1][0], snake_body[-1][1], block + 8, block + 8))
    pygame.draw.rect(screen, green_light, (snake_body[-1][0], snake_body[-1][1], block + 8, block + 8), 2)
    pygame.draw.circle(screen, black, (round(snake_body[-1][0] + 10), round(snake_body[-1][1] + 15)), 3)
    pygame.draw.circle(screen, black, (round(snake_body[-1][0] + 18), round(snake_body[-1][1] + 15)), 3)


def draw_food(food_x, food_y):   # to draw food
    block = 20
    pygame.draw.rect(screen, yellow, (food_x, food_y, block, block))


def start_flag():                 # to draw the start flag at the top right of the screen
    flag_square_Y = 36
    for row in range(4):
        if row % 2 == 0:
            flag_square_X = 150
            squares_to_print = 5
        else:
            flag_square_X = 143
            squares_to_print = 4

        for column in range(squares_to_print):
            pygame.draw.rect(screen, white, (SCREEN_WIDTH - flag_square_X, flag_square_Y, 6, 6))
            flag_square_X -= 15
        flag_square_Y += 8

current_high_score = 0

def display_info(score, game_round):  # displays score, title and high score

    global current_high_score
    title_Font = pygame.font.SysFont(font, 20, True)
    show_title = title_Font.render("THE SNAKE GAME", True, green_light)
    screen.blit(show_title, [round((SCREEN_WIDTH / 2)) - 95, 5])

    score_Font = pygame.font.SysFont(font, 30, True)
    show_score = score_Font.render("Your Score: " + str(score), True, yellow)
    screen.blit(show_score, [round((SCREEN_WIDTH / 2)) - 100, 40])

    escape_prompt_Font = pygame.font.SysFont(font, 25, True)
    escape_prompt = escape_prompt_Font.render("Press Esc to quit the game", True, white)
    screen.blit(escape_prompt, [22, SCREEN_HEIGHT - 40])

    high_score_Font = pygame.font.SysFont(font, 30, True)
    if game_round == 1:
        high = high_score_Font.render("HI: " + str(score), True, green_light)
        screen.blit(high, [40, 20])
        current_high_score = score

    if game_round != 1:     # during the 1st round high score is equal to score
        if current_high_score < score:
            current_high_score = score
            high = high_score_Font.render("HI: " + str(current_high_score), True, green_light)
            screen.blit(high, [40, 20])

        else:
            high = high_score_Font.render("HI: " + str(current_high_score), True, green_light)
            screen.blit(high, [40, 20])


def display_prompt(prompt):
    title_Font = pygame.font.SysFont(font, 23, True)
    show_title = title_Font.render(prompt, True, green_light)
    screen.blit(show_title, [SCREEN_WIDTH - 250, 5])


def main():                          # controls both game and in-game actions
    game_loop = True

    in_game = True

    game_round = 1

    food_draw = 1

    snake_roll_over = False           # change this for snake roll over effect

    while game_loop:                  # the start of the game loop

        X = round(SCREEN_WIDTH / 2)
        Y = round(SCREEN_HEIGHT / 2)

        dir_x = 0
        dir_y = 0
        x_change = 0
        y_change = 0

        rate = 20           # adjust the value of rate for snake's speed

        key = " "

        pause_game = False

        snake_body = []
        snake_length = 0

        start = 1

        score = 0

        food_x = round(random.randint(23, SCREEN_WIDTH - 40))
        food_y = round(random.randint(75, SCREEN_HEIGHT - 125))

        if food_draw == 1:                          # to draw food at the start of the game
            food_x = round(random.randint(23, SCREEN_WIDTH - 40))
            food_y = round(random.randint(75, SCREEN_HEIGHT - 128))
            draw_food(food_x, food_y)
            food_draw += 1


        while in_game:                             # loop to control the in game actions

            screen.fill(black)
            pygame.draw.rect(screen, blue, (20, 70, SCREEN_WIDTH - 40, SCREEN_HEIGHT - 115), 4)

            if start == 1:
                display_prompt("Use arrow keys to start")
                start_flag()

            display_info(score, game_round)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    leave_game()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_LEFT:
                        x_change = -rate
                        y_change = 0
                        key = "LEFT"
                        start = 2

                    if event.key == pygame.K_RIGHT:
                        x_change = rate
                        y_change = 0
                        key = "RIGHT"
                        start = 2

                    if event.key == pygame.K_UP:
                        x_change = 0
                        y_change = -rate
                        key = "UP"
                        start = 2

                    if event.key == pygame.K_DOWN:
                        x_change = 0
                        y_change = rate
                        key = "DOWN"
                        start = 2

                    if event.key == pygame.K_p:
                        pause_game = True

                    if event.key == pygame.K_c:
                        pause_game = False

                    if event.key == pygame.K_ESCAPE:
                        leave_game()

            if pause_game:
                if start != 1:
                    display_prompt("Press C to Continue")
                    pygame.draw.rect(screen, white, (SCREEN_WIDTH - 150, 35, 5, 25))
                    pygame.draw.rect(screen, white, (SCREEN_WIDTH - 135, 35, 5, 25))

            else:
                if start >= 2:
                    points = ((SCREEN_WIDTH - 150, 35), (SCREEN_WIDTH - 126, 47), (SCREEN_WIDTH - 150, 60))
                    pygame.draw.polygon(screen, white, points)

                snake_head = []

                if start != 1:
                    display_prompt("Press P to Pause")


                if key == "UP" and dir_y == rate:          # the if conditions ensure that
                    y_change = rate                        # the snake cannot traverse in the
                                                           # opposite direction  immediately
                if key == "DOWN" and dir_y == -rate:
                    y_change = -rate

                if key == "RIGHT" and dir_x == -rate:
                    x_change = -rate

                if key == "LEFT" and dir_x == rate:
                    x_change = rate

                

                if snake_roll_over:
                    if X >= SCREEN_WIDTH - 55:                      # if cond. here ensures that snake
                        X = 36                                      # exiting in one direction enters
                                                                    # from the opposite direction
                    if Y >= SCREEN_HEIGHT - 105:
                        Y = 81

                    if X <= 35:
                        X = SCREEN_WIDTH - 45

                    if Y <= 80:
                        Y = SCREEN_HEIGHT - 106
                
                else:
                    if X >= SCREEN_WIDTH - 60 or Y >= SCREEN_HEIGHT - 100 or X <= 40 or Y <= 80:
                        in_game = False
                
                
                X += x_change
                Y += y_change

                dir_x = x_change
                dir_y = y_change

                snake_head.append(X)
                snake_head.append(Y)

                if len(snake_body) > snake_length:
                    del snake_body[0]

                for x in snake_body[::-1]:
                    if x == snake_head:
                        in_game = False

                snake_body.append(snake_head)

            draw_food(food_x, food_y)
            draw_snake(snake_body)

            if X - 20 <= food_x <= X + 20 and Y - 20 <= food_y <= Y + 20:
                food_x = round(random.randint(23, SCREEN_WIDTH - 50))
                food_y = round(random.randint(76, SCREEN_HEIGHT - 128))
                snake_length += 1
                score += 1

            if not in_game:
                pygame.draw.rect(screen, red, [SCREEN_WIDTH - 260, 10, 240, 50])
                title_Font = pygame.font.SysFont(font, 20, True)
                game_over = title_Font.render("GAME OVER", True, green_light)
                screen.blit(game_over, [SCREEN_WIDTH - 190, 10])

                title_Font = pygame.font.SysFont(font, 20, True)
                space = title_Font.render("Press SPACE to play again", True, green_light)
                screen.blit(space, [SCREEN_WIDTH - 250, 35])
                pygame.display.update()

            pygame.display.update()
            clock.tick(rate)

#           the in-game loop fails once the player gets out

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                leave_game()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:  # option to play again
                    in_game = True
                    game_round += 1
                    food_draw = 1

                if event.key == pygame.K_ESCAPE:
                    leave_game()

        pygame.display.update()
        clock.tick(rate)


main()
