#!/usr/bin/env python3
# created: 20/14/2020
# authors: Noah Kernis & Sue Roh

import pygame
import random
import time

mda_dir = 'media/'
bg_dir = 'background/'
aml_dir = 'animal/'

# TODO: pick 
animal_sounds = ['rain.wav', 'frogs.wav', 'waterfall.wav']

# TODO: pick bg sounds
loop_files = ['frogs.wav']

pygame.mixer.init()

# channels 
# pygame.mixer.set_num_channels(10) (default: 8)
idx_0 = 0
idx_1 = 1
idx_2 = 2
idx_3 = 3
idx_4 = 4
idx_5 = 5
idx_6 = 6
idx_7 = 7

def play_sound(sound, sec, idx):
    pygame.mixer.Channel(idx).play(sound, -1, sec)


for filename in files:
    pygame.mixer.music.load(media + filename)
    sound = pygame.mixer.Sound(media + filename)

    channel = pygame.mixer.Channel(idx).play(sound, -1)
    sound.set_volume(0.5)
    idx += 1

for filename in loop_files:
    def playsounds():
        print(idx)
        play_sound(sound, 2000, idx)
    pygame.mixer.music.load(media + filename)
    sound = pygame.mixer.Sound(media + filename)
    setInterval(playsounds, 1)
    idx += 1

# plays occasional thunder sounds
duration = var.thunder_sound.get_length()  # duration of thunder in seconds
while True:  # infinite while-loop
    # play thunder sound if random condition met
    if random.randint(0, 80) == 10:
        channel2.play(var.thunder_sound)
    # pause while-loop for duration of thunder
    time.sleep(duration)
