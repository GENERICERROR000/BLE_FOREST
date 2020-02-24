#!/usr/bin/env python3
# created: 02/24/2020
# authors: Noah Kernis & Sue Roh

import pygame
import time

mda_dir = 'media/'
bg_dir = 'background/'
bg_rainforest_ambiance = 'rainforest_ambiance_01'
bg_media_dir = mda_dir + bg_dir
bg_rainforest_path = bg_media_dir + bg_rainforest_ambiance + '.wav'

pygame.mixer.pre_init()
pygame.mixer.init(48000, -16, 1, 1024)
pygame.init()

# load bg sound
pygame.mixer.music.load(bg_rainforest_path)

# set init bg sound volume
pygame.mixer.music.set_volume(0.3)

# init bg sound and loop forever
pygame.mixer.music.play(loops=-1)

time.sleep(2000)
