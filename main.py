import pygame

pygame.init()

screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)

planets = ["one.png", "two.png", "three.png"]
p_index = 0

background = pygame.image.load("background.png")
planet = pygame.image.load(planets[p_index])
spaceship = pygame.image.load("spaceship.png")
bullet = pygame.image.load("bullet.png")

planet_x = 140
move_direction = "right"

bullet_y = 500
fired = False

clock = pygame.time.Clock()

keep_alive = True
while keep_alive:

    pygame.event.get()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        fired = True
        print("Space Key Pressed")

    if move_direction == "right":
        planet_x = planet_x + 5
        if planet_x == 300:
            move_direction = "left"

    else:
        planet_x = planet_x - 5
        if planet_x == 0:
            move_direction = "right"

    if fired is True:
        bullet_y = bullet_y - 5
        if bullet_y == 50:
            fired = False
            bullet_y = 500

    screen.blit(background, [0, 0])
    screen.blit(planet, [planet_x, 50])
    screen.blit(bullet, [180, bullet_y])
    screen.blit(spaceship, [160, 500])

    if bullet_y < 110 and 120 < planet_x < 180:
        p_index = p_index + 1
        if p_index < len(planets):
            planet = pygame.image.load(planets[p_index])
            planet_x = 10
        else:
            print("You Win")
            keep_alive = False
        print("boom")

    pygame.display.update()

    clock.tick(60)
