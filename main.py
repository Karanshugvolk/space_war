from setting import *
from redship import RedShip
from yellowship import YellowShip
from Bullet import Bullet

pg.init()
pg.font.init()

screen = pg.display.set_mode((W, H))
pg.display.set_caption("Space war!")

red_health = 10
yellow_health = 10

font = pg.font.SysFont('Arial', 36)

all_sprite = pg.sprite.Group()
red_ship = RedShip()
yellow_ship = YellowShip()
all_sprite.add(red_ship)
all_sprite.add(yellow_ship)

bullets_red = pg.sprite.Group()
bullets_yellow = pg.sprite.Group()


def shoot_yellow():
    bullet_y = Bullet(yellow_ship.rect.center, "yellow")
    bullets_yellow.add(bullet_y)
    all_sprite.add(bullets_yellow)


def shoot_red():
    bullet_r = Bullet(red_ship.rect.center, "red")
    bullets_red.add(bullet_r)
    all_sprite.add(bullets_red)


def game_over():
    all_sprite.empty()
    screen.blit(back_ground_lose, (0, 0))
    game_over_text = font.render("Game Over", True, 'white')
    screen.blit(game_over_text, (W / 2 - 100, H / 2))
    pg.mixer.pause()
    if red_health <= 0:
        yellow_winner_text = font.render("Победа жёлтых", True, 'white')
        screen.blit(yellow_winner_text, (W / 2 - 100, H / 2 + 50))

    elif yellow_health <= 0:
        red_winner_text = font.render("Победа красных", True, 'white')
        screen.blit(red_winner_text, (W / 2 - 100, H / 2 + 50))


run = True
while run:
    health_text = font.render(f"{round(red_health, 2)}                                    {round(yellow_health, 2)}", True, 'white')

    health_text_rect = health_text.get_rect()

    health_text_rect.center = screen.get_rect().center

    screen.blit(background_img, (0, 0))
    clock.tick(60)

    screen.blit(health_text, (health_text_rect.w, 40))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
            pg.quit()

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_RCTRL:
                shoot_yellow()
                blaster_sound.play()
            elif event.key == pg.K_LCTRL:
                shoot_red()
                blaster_sound.play()

    if pg.sprite.spritecollide(red_ship, bullets_yellow, False, pg.sprite.collide_circle):
        red_health -= 0.1


    if pg.sprite.spritecollide(yellow_ship, bullets_red, False, pg.sprite.collide_circle):
        yellow_health -= 0.1

    if red_health <= 0:
        game_over()

    if yellow_health <= 0:
        game_over()



    all_sprite.update()
    all_sprite.draw(screen)

    pg.display.flip()

pg.quit()
