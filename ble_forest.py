#!/usr/bin/env python3
# created: 20/14/2020
# authors: Noah Kernis & Sue Roh

import os
import pygame
import random
import time

# -----> Media <-----

mda_dir = 'media/'
bg_dir = 'background/'
aml_dir = 'animal/'

aml_american_woodcock = 'american_woodcock'
aml_bluejay_0 = 'bluejay_0'
aml_bluejay_1 = 'bluejay_1'
aml_frogs = 'frogs'
aml_killdeer_0 = 'killdeer_0'
aml_killdeer_1 = 'killdeer_1'
aml_meadowlark = 'meadowlark'
aml_peacock = 'peacock'
aml_warbling_vireo = 'warbling_vireo'


bg_rainforest_ambiance = 'rainforest_ambiance'
bg_nature_ambiance = 'nature_ambiance'

# -----> Init Audio <-----

bg_sound_volume = 0.5

# init pygame
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.init()

# set number of channels (default: 8)
pygame.mixer.set_num_channels(500)

# NOTE:
# attempting to use music api to avoid
# conflicts with sound effects on channels

# load bg sound
bg_path = mda_dir + bg_dir + bg_rainforest_ambiance + ".wav"
# bg_sound = pygame.mixer.Sound(bg_path)

# find_channel(): find and return an inactive Channel.
# if no inactive channels and the force argument is True,
# will find the Channel with the longest running Sound and return it.

# set init bg sound volume
# bg_sound.set_volume(bg_sound_volume)

# init bg sound - loop forever
# pygame.mixer.find_channel(True).play(bg_sound, -1)

pygame.mixer.music.load(bg_path)
pygame.mixer.music.set_volume(bg_sound_volume)
pygame.mixer.music.play(loops=-1)

# -----> Data Handlers <-----


def handle_new_data(data):
    print("new data", data)

# def which_type(data):
#     switch = {
#         "os_a": "January",
#         "os_b": "February",
#     }

#     	func = switch.get(data.type)
#     	print(func, "invalid os")
#     	return func

# -----> Effect Handlers <-----


def play_sound(sound, sec, idx):
    pygame.mixer.Channel(idx).play(sound, -1, sec)

# -----> State Handlers <----- (may not need)


# -----> Dev Helpers <-----


### Rating for sounds ###

# NOTE:
# may want to randomize volume for every time
# a sound is played. will "feel" more dynamic...?

# GOOD

aml_american_woodcock_path = mda_dir + aml_dir + aml_american_woodcock + ".wav"
aml_frogs_path = mda_dir + aml_dir + aml_frogs + ".wav"
# a lot in hear, needs edit
aml_meadowlark_path = mda_dir + aml_dir + aml_meadowlark + ".wav"
aml_peacock_path = mda_dir + aml_dir + aml_peacock + ".wav"
# long
aml_warbling_vireo_path = mda_dir + aml_dir + aml_warbling_vireo + ".wav"

# OK (potentially annoying)

aml_bluejay_0_path = mda_dir + aml_dir + aml_bluejay_0 + ".wav"
aml_bluejay_1_path = mda_dir + aml_dir + aml_bluejay_1 + ".wav"
aml_killdeer_0_path = mda_dir + aml_dir + aml_killdeer_0 + ".wav"

# BAD

aml_killdeer_1_path = mda_dir + aml_dir + aml_killdeer_1 + ".wav"

TEST_ANIMAL_sound = pygame.mixer.Sound(aml_warbling_vireo_path)
TEST_ANIMAL_sound.set_volume(0.4)

duration = TEST_ANIMAL_sound.get_length()

# play sound randomly
while True:
    if random.randint(0, 1000000) == 10:
        print("hit")
        pygame.mixer.find_channel(True).play(TEST_ANIMAL_sound)
        # pygame.mixer.find_channel(True).play(TEST_ANIMAL_sound, maxtime=500)

        # pause for duration audio
        # time.sleep(.5)
        time.sleep(duration)
