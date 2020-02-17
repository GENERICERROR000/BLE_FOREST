#!/usr/bin/env python3
# created: 20/14/2020
# authors: Noah Kernis & Sue Roh

import os
import pygame
import random
import time

# -----> APPLE_BLE Data <-----

currentState = {

}

deviceTypes = {

}

# -----> Media <-----

# dirs
mda_dir = 'media/'
bg_dir = 'background/'
aml_dir = 'animal/'

# background sounds
bg_rainforest_ambiance = 'rainforest_ambiance'
bg_gentle_rain = 'gentle_rain'
bg_light_rain = 'light_rain'
bg_thunder_lightning_rain = 'thunder_lightning_rain'

# animal sounds
aml_frogs = 'frogs'
aml_american_woodcock = 'american_woodcock'
aml_killdeer = 'killdeer'
aml_meadowlark = 'meadowlark'
aml_peacock = 'peacock'
aml_warbling_vireo = 'warbling_vireo'
aml_quail_call = 'quail_call'
aml_crane_call = 'crane_call'
aml_crow = 'crow'
aml_cuckoo_bird_song = 'cuckoo_bird_song'
aml_eurasian_collared_dove_call = 'eurasian_collared_dove_call'
aml_tawny_owl_call = 'tawny_owl_call'
aml_woodpecker_pecking = 'woodpecker_pecking'

# -----> Init Audio <-----


bg_sound_volume = 0.5

# init pygame
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.init()

# set number of channels (default: 8)
pygame.mixer.set_num_channels(500)


# -----> Init Background Audio <-----

# has light thunder throughout
bg_gentle_rain_path = mda_dir + bg_dir + bg_gentle_rain + '.wav'

# better audio
# more running water
# short
bg_light_rain_path = mda_dir + bg_dir + bg_light_rain + '.wav'

bg_thunder_lightning_rain_path = mda_dir + \
    bg_dir + bg_thunder_lightning_rain + '.wav'


# load bg sound
bg_path = mda_dir + bg_dir + bg_rainforest_ambiance + '.wav'
pygame.mixer.music.load(bg_path)

# set init bg sound volume
pygame.mixer.music.set_volume(bg_sound_volume)

# init bg sound - loop forever
pygame.mixer.music.play(loops=-1)


# -----> Data Handlers <-----


def handle_new_data(data):
    print("new data", data)

# NOTE: switch example
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
    # load bg sound
    # bg_path = mda_dir + bg_dir + bg_rainforest_ambiance + '.wav'
    # bg_sound = pygame.mixer.Sound(bg_path)

    # find_channel(): find and return an inactive Channel.
    # if no inactive channels and the force argument is True,
    # will find the Channel with the longest running Sound and return it.

    # set init bg sound volume
    # bg_sound.set_volume(bg_sound_volume)

    # init bg sound - loop forever
    # pygame.mixer.find_channel(True).play(bg_sound, -1)

# -----> State Handlers <----- (may not need)


# -----> Dev Helpers <-----


### Rating For Effects ###

# NOTE:
# may want to randomize volume for every time
# a sound is played. will "feel" more dynamic...?

# good
aml_killdeer_path = mda_dir + aml_dir + aml_killdeer + '.wav'
aml_frogs_path = mda_dir + aml_dir + aml_frogs + '.wav'
aml_american_woodcock_path = mda_dir + aml_dir + aml_american_woodcock + '.wav'
aml_peacock_path = mda_dir + aml_dir + aml_peacock + '.wav'
aml_crow_path = mda_dir + aml_dir + aml_crow + '.wav'
aml_eurasian_collared_dove_call_path = mda_dir + \
    aml_dir + aml_eurasian_collared_dove_call + '.wav'
aml_woodpecker_pecking_path = mda_dir + aml_dir + \
    aml_woodpecker_pecking + '.wav'  # don't overuse

# long - needs edit
aml_meadowlark_path = mda_dir + aml_dir + aml_meadowlark + '.wav'
aml_warbling_vireo_path = mda_dir + aml_dir + aml_warbling_vireo + '.wav'
aml_quail_call_path = mda_dir + aml_dir + aml_quail_call + '.wav'
aml_crane_call_path = mda_dir + aml_dir + aml_crane_call + '.wav'
aml_tawny_owl_call_path = mda_dir + aml_dir + aml_tawny_owl_call + '.wav'
# potentially annoying...
aml_cuckoo_bird_song_path = mda_dir + aml_dir + aml_cuckoo_bird_song + '.wav'

CARL = [
    aml_killdeer_path,
    aml_frogs_path,
    aml_american_woodcock_path,
    aml_peacock_path,
    aml_crow_path,
    aml_eurasian_collared_dove_call_path,
    aml_woodpecker_pecking_path,
    aml_meadowlark_path,
    aml_warbling_vireo_path,
    aml_quail_call_path,
    aml_crane_call_path,
    aml_tawny_owl_call_path,
    aml_cuckoo_bird_song_path,
]
duration = 0
parth = ''

# play sound randomly
while True:
    if random.randint(0, 1000000) == 10:
        parth = CARL[random.randint(0, 12)]

        test_animal_sound = pygame.mixer.Sound(parth)
        test_animal_sound.set_volume(0.4)

        duration = test_animal_sound.get_length()

        print(parth, 'duration:', duration)
        pygame.mixer.find_channel(True).play(test_animal_sound)
        # pygame.mixer.find_channel(True).play(TEST_ANIMAL_sound, maxtime=500)

        # pause for duration audio
        time.sleep(3)

# time.sleep(2000)
