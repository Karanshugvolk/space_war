import os
import pygame as pg

pg.mixer.init()
W, H = 900, 500
FPS = int(60)
clock = pg.time.Clock()

game_folder = os.path.dirname(__file__)
media_folder = os.path.join(game_folder, 'media')
sound_folder = os.path.join(game_folder, 'sound')

red_ship_img = pg.image.load(os.path.join(media_folder, 'spaceship_red.png'))
yellow_ship_img = pg.image.load(os.path.join(media_folder, 'spaceship_yellow.png'))
background_img = pg.image.load(os.path.join(media_folder, 'space.png'))
back_ground_lose = pg.image.load(os.path.join(media_folder, 'back_ground_lose.jpg'))

blaster_sound = pg.mixer.Sound(os.path.join(sound_folder, 'blaster.wav'))
