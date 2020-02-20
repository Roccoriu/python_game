import pygame
from random import randrange
from rounded import rect_round

## global variables
## =================

# screen variables
fps             = pygame.time.Clock()
width           = 1280
height          = 720
turning_radius  = 20
play_area       = [(width - 40), (height - 40)]


# snake
snake_pos       = [400, 260]
snake_bod       = []
snake_size      = [turning_radius, turning_radius]


# food
food            = [turning_radius, turning_radius]
food_pos        = [randrange(0, width, 20), randrange(80, height, 20)]
food_exists     = False


# snake movement
movement_speed  = 20
direction       = 'r'


# other game variables
exit_game       = False
optimus_font    = "bin/assets/OptimusPrinceps.ttf"
you_died_sound  = "bin/assets\sounds/Dark Souls ' You Died ' Sound Effect.mp3"
score           = 0

## colors
white           = (255, 255, 255)
black           = (0, 0, 0)
red             = (255, 0, 0)



## init screen and sounds
## =================
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load(you_died_sound)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Makey Makey snake")



## functions
## =================

def init_body(body_size):
    snake_bod.append([snake_pos[0], snake_pos[1]])

    for i in range(1, body_size):
        snake_bod.append([snake_pos[0]-(i*snake_size[0]), snake_pos[1]])


def game_over():
    pygame.mixer.music.play()

    font = pygame.font.Font(optimus_font, 140)
    game_over_text = font.render('You Died', True,  red)
    game_over_cp = game_over_text.copy()

    game_over_plane = game_over_text.get_rect()
    game_over_plane.midtop = ((width /2), (height /4))

    alpha_surf = pygame.Surface(game_over_cp.get_size(), pygame.SRCALPHA)

    alpha = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        if alpha < 255:
            alpha += 0.1
            game_over_cp = game_over_text.copy()
            alpha_surf.fill((255, 255, 255, alpha))
            game_over_cp.blit(alpha_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)


        screen.fill(black)
        screen.blit(game_over_cp, game_over_plane)
        pygame.display.flip()



def show_score(score_new):
    score_new = 0
    font = pygame.font.Font(optimus_font, 40)
    score_writing = font.render("score: " + str(score), True, white)

    score_pos = score_writing.get_rect()
    score_pos.midtop = ((90, 18))
    screen.blit(score_writing, score_pos)


## Main loop
## =================

init_body(8)

while not exit_game:
    if turning_radius < 20:
        turning_radius += movement_speed

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and direction != 'u' and turning_radius == 20:
                direction = 'd'
                turning_radius = 0

            if event.key == pygame.K_UP and direction != 'd' and turning_radius == 20:
                direction = 'u'
                turning_radius = 0

            if event.key == pygame.K_LEFT and direction != 'r' and turning_radius == 20:
                direction = 'l'
                turning_radius = 0

            if event.key == pygame.K_RIGHT and direction != 'l' and turning_radius == 20:
                direction = 'r'
                turning_radius = 0


    if direction == 'l' and snake_pos[0] - movement_speed >= 0:
        snake_pos[0] -= movement_speed

    elif direction == 'r' and snake_pos[0] + movement_speed < 1280:
        snake_pos[0] += movement_speed

    elif direction == 'u' and snake_pos[1] - movement_speed >= 80:
        snake_pos[1] -= movement_speed

    elif direction == 'd' and snake_pos[1] + movement_speed < 720:
        snake_pos[1] += movement_speed

    else:
        game_over()


    snake_bod.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_exists = False
    else:
        snake_bod.pop()


    if not food_exists:
        food_exists = True
        food_pos = [randrange(0, width, 20), randrange(80, height, 20)]



    screen.fill(black)
    show_score(score)
    pygame.draw.line(screen, white, (0, 79),  (1280, 79))



    for joint in snake_bod:
        pygame.draw.rect(screen, white, (joint[0], joint[1], snake_size[0], snake_size[1]))


    rect_round(screen, (food_pos[0], food_pos[1], food[0], food[1]), red, 1)


    for block in snake_bod[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()


    pygame.display.flip()
    fps.tick(8)


pygame.quit()
exit(0)