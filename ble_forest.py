#!/usr/bin/env python3
# created: 20/14/2020
# authors: Noah Kernis & Sue Roh

import os
import pygame
import random
import time

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

### Rating For Effects ###

aml_media_path = mda_dir + aml_dir

# NOTE:
# may want to randomize volume for every time
# a sound is played. will "feel" more dynamic...?

# good

aml_killdeer_path = aml_media_path + aml_killdeer + '.wav'
aml_frogs_path = aml_media_path + aml_frogs + '.wav'
aml_american_woodcock_path = aml_media_path + aml_american_woodcock + '.wav'
aml_peacock_path = aml_media_path + aml_peacock + '.wav'
aml_crow_path = aml_media_path + aml_crow + '.wav'
aml_eurasian_collared_dove_call_path = aml_media_path + \
    aml_eurasian_collared_dove_call + '.wav'
aml_woodpecker_pecking_path = aml_media_path + \
    aml_woodpecker_pecking + '.wav'  # don't overuse

# long - needs edit
aml_meadowlark_path = aml_media_path + aml_meadowlark + '.wav'
aml_warbling_vireo_path = aml_media_path + aml_warbling_vireo + '.wav'
aml_quail_call_path = aml_media_path + aml_quail_call + '.wav'
aml_crane_call_path = aml_media_path + aml_crane_call + '.wav'
aml_tawny_owl_call_path = aml_media_path + aml_tawny_owl_call + '.wav'
# potentially annoying...
aml_cuckoo_bird_song_path = aml_media_path + aml_cuckoo_bird_song + '.wav'

# -----> Init Pygame <-----


bg_sound_volume = 0.5

# init pygame
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.init()

# set number of channels (default: 8)
pygame.mixer.set_num_channels(500)

# -----> apple_ble Data <-----

# NOTE: Use apple_ble vars to track changes (find them...)
previous_data = []

# data = [
#     phone,
#     phones[phone]['state'],
#     phones[phone]['device'],
#     phones[phone]['wifi'],
#     phones[phone]['os'],
#     phones[phone]['phone'],
#     phones[phone]['time'],
#     phones[phone]['notes']
# ]

# device_action_sound_map = {
#     'phone': pygame.mixer.Sound(aml_frogs_path),
#     'MacBook': pygame.mixer.Sound(aml_american_woodcock_path),
#     'Watch': pygame.mixer.Sound(aml_killdeer_path),
#     'airpods': pygame.mixer.Sound(aml_meadowlark_path),
#     'Idle': pygame.mixer.Sound(aml_peacock_path),
#     'Lock screen': pygame.mixer.Sound(aml_warbling_vireo_path),
#     'Home screen': pygame.mixer.Sound(aml_quail_call_path),
#     'Off': pygame.mixer.Sound(aml_crane_call_path),
#     'Music': pygame.mixer.Sound(aml_crow_path),
#     'Disabled': pygame.mixer.Sound(aml_cuckoo_bird_song_path),
#     'Case:open': pygame.mixer.Sound(aml_eurasian_collared_dove_call_path),
#     'Case:Closed': pygame.mixer.Sound(aml_tawny_owl_call_path),
#     'Case:All out': pygame.mixer.Sound(aml_woodpecker_pecking_path),
# }

# -----> Init Background Audio <-----

bg_media_dir = mda_dir + bg_dir

# has light thunder throughout
bg_gentle_rain_path = bg_media_dir + bg_gentle_rain + '.wav'

# better audio
# more running water
# short
bg_light_rain_path = bg_media_dir + bg_light_rain + '.wav'

bg_thunder_lightning_rain_path = bg_media_dir + bg_thunder_lightning_rain + '.wav'

# load bg sound
bg_path = bg_media_dir + bg_rainforest_ambiance + '.wav'
pygame.mixer.music.load(bg_path)

# set init bg sound volume
pygame.mixer.music.set_volume(bg_sound_volume)

# init bg sound - loop forever
pygame.mixer.music.play(loops=-1)


# -----> Data Handlers <-----


def handle_new_data(data):
    print("new data", data)

# NOTE: switch examples

# 1
# def which_type(data):
#     switch = {
#         "os_a": "January",
#         "os_b": "February",
#     }

#     	func = switch.get(data.type)
#     	print(func, "invalid os")
#     	return func

# 2
# def parse_os_wifi_code(code, dev):
#     if code == '1c':
#         if dev == 'MacBook':
#             return ('Mac OS', 'On')
#         else:
#             return ('iOS12', 'On')
#     elif code == '18':
#         if dev == 'MacBook':
#             return ('Mac OS', 'Off')
#         else:
#             return ('iOS12', 'Off')
#     elif code == '10':
#         return ('iOS11', '<unknown>')
#     elif code == '1e':
#         return ('iOS13', 'On')
#     elif code == '1a':
#         return ('iOS13', 'Off')
#     elif code == '0e':
#         return ('iOS13', 'Connecting')
#     elif code == '0c':
#         return ('iOS12', 'On')
#     elif code == '04':
#         return ('iOS13', 'On')
#     elif code == '00':
#         return ('iOS10', '<unknown>')
#     elif code == '09':
#         return ('Mac OS', '<unknown>')
#     elif code == '14':
#         return ('Mac OS', 'On')
#     elif code == '98':
#         return ('WatchOS', '<unknown>')
#     else:
#         return ('', '')

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
