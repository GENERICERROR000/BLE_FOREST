#!/usr/bin/env python3
# created: 20/14/2020
# authors: Noah Kernis & Sue Roh

import os
import pygame
import random
import re
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


state = {}

number_devices = 0

# carl = {
#     'C8:69:CD:0E:13:E4': {
#         'state': 'Disabled',
#         'device': 'iPhone',
#         'wifi': 'On',
#         'os': 'iOS13',
#         'phone': '',
#         'time': 1581980104,
#         'notes': ''
#     },
#     "...": {}
# }

device_action_sound_map = {
    'phone': pygame.mixer.Sound(aml_frogs_path),
    'MacBook': pygame.mixer.Sound(aml_american_woodcock_path),
    'Watch': pygame.mixer.Sound(aml_killdeer_path),
    'airpods': pygame.mixer.Sound(aml_meadowlark_path),
    'Idle': pygame.mixer.Sound(aml_peacock_path),
    'Lock screen': pygame.mixer.Sound(aml_warbling_vireo_path),
    'Home screen': pygame.mixer.Sound(aml_quail_call_path),
    'Off': pygame.mixer.Sound(aml_crane_call_path),
    'Music': pygame.mixer.Sound(aml_crow_path),
    'Disabled': pygame.mixer.Sound(aml_cuckoo_bird_song_path),
    'Case:open': pygame.mixer.Sound(aml_eurasian_collared_dove_call_path),
    'Case:Closed': pygame.mixer.Sound(aml_tawny_owl_call_path),
    'Case:All out': pygame.mixer.Sound(aml_woodpecker_pecking_path),
}


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


# TODO: How to handle apple_ble data
# - 1.0) `print_results()` is called (apple_ble)
#     - 1.1) `clear_zombies()` is called (apple_ble)
#       - 1.1.1) call custom fn to remove dev from custom audio state
#   	- 1.1.2) decrease number of dev's
#    - 1.2) custom data handler called (see 2.0)
# - 2.0) custom data handler
#    - 2.1) receive data and compare to state
#   	- 2.1.1) keep if in state
#    - 2.2) those not in state are new
#   	- 2.2.1) increase number of dev's
#   	- 2.2.2) play sound(use fn to determine type) for each new dev

def handle_new_data(data):
    print('new data')
    update_state(data)


def update_state(devices):
    for dev in devices:
        dev_data = devices[dev]

        if dev in state:
            handle_device_status_change(dev, dev_data)

        if dev not in state:
            handle_new_device(dev, dev_data)


def handle_device_status_change(dev, dev_data):
    print('device status has changed')
    sound = which_sound(dev_data['device'], dev_data['state'])
    play_sound(sound)


def handle_new_device(dev, dev_data):
    print('new device')
    state[dev] = dev_data

    # - increment number of devices
    # - play audio for device type
    # -

    # carl = {
    #     'C8:69:CD:0E:13:E4': {
    #         'state': 'Disabled',
    #         'device': 'iPhone',
    #         'wifi': 'On',
    #         'os': 'iOS13',
    #         'phone': '',
    #         'time': 1581980104,
    #         'notes': ''
    #     },
    #     "...": {}
    # }


# -----> Sound Handlers <-----

def which_sound(device, state):
    # WARN: RETURN THIS: `to_play = device_action_sound_map[sound_name]`

    if device == 'iPad' or 'iPhone' or 'MacOS':
        if state == 'Idle':
            return ''

        elif state == 'Lock screen':
            return ''

        elif state == 'Home screen':
            return ''

        elif state == 'Off':
            return ''

        else:
            return 'default_action'

    elif device == 'AirPods' or 'Powerbeats3' or 'BeatsX' or 'Beats Solo3':
        if state == 'Case:Closed':
            return ''

        elif state == 'Case:open':
            return ''

        elif state == 'Case:All out':
            return ''

        elif re.search(r'\bout\b', state):
            return ''

        elif re.search(r'\bin\b', state):
            return ''

        else:
            return 'default_action'

    else:
        return 'default_action'


def play_sound(sound, volume=0.5):
    # NOTE:
    # may want to randomize volume for every time
    # a sound is played. will "feel" more dynamic...?
    sound.set_volume(volume)

    # find_channel(): find and return an inactive Channel.
    # if no inactive channels and the force argument is True,
    # will find the Channel with the longest running Sound and return it.
    pygame.mixer.find_channel(True).play(sound)


# -----> Dev Helpers <-----


SOUND_LIST = [
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
        parth = SOUND_LIST[random.randint(0, 12)]

        test_animal_sound = pygame.mixer.Sound(parth)
        test_animal_sound.set_volume(0.4)

        duration = test_animal_sound.get_length()

        print(parth, 'duration:', duration)
        pygame.mixer.find_channel(True).play(test_animal_sound)
        # pygame.mixer.find_channel(True).play(TEST_ANIMAL_sound, maxtime=500)

        # pause for duration audio
        time.sleep(2)

# time.sleep(2000)
