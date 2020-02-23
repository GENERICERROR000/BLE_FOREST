#!/usr/bin/env python3
# created: 20/14/2020
# authors: Noah Kernis & Sue Roh


import pygame
import re
# import os
# import time


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

# animal sound paths
aml_media_path = mda_dir + aml_dir
aml_killdeer_path = aml_media_path + aml_killdeer + '.wav'
aml_american_woodcock_path = aml_media_path + aml_american_woodcock + '.wav'
aml_peacock_path = aml_media_path + aml_peacock + '.wav'
aml_crow_path = aml_media_path + aml_crow + '.wav'
aml_meadowlark_path = aml_media_path + aml_meadowlark + '.wav'
aml_warbling_vireo_path = aml_media_path + aml_warbling_vireo + '.wav'
aml_quail_call_path = aml_media_path + aml_quail_call + '.wav'
aml_crane_call_path = aml_media_path + aml_crane_call + '.wav'
aml_tawny_owl_call_path = aml_media_path + aml_tawny_owl_call + '.wav'
aml_cuckoo_bird_song_path = aml_media_path + aml_cuckoo_bird_song + '.wav'
aml_eurasian_collared_dove_call_path = aml_media_path + \
    aml_eurasian_collared_dove_call + '.wav'
aml_woodpecker_pecking_path = aml_media_path + \
    aml_woodpecker_pecking + '.wav'


# -----> Init Pygame <-----

# init pygame
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.init()

# set number of channels (default: 8)
pygame.mixer.set_num_channels(500)

device_status_sound_map = {
    'idle':  pygame.mixer.Sound(aml_eurasian_collared_dove_call_path),
    'lock_screen': pygame.mixer.Sound(aml_woodpecker_pecking_path),
    'home_screen': pygame.mixer.Sound(aml_killdeer_path),
    'off': pygame.mixer.Sound(aml_meadowlark_path),
    'case_actions': pygame.mixer.Sound(aml_peacock_path),
    'iphone': pygame.mixer.Sound(aml_quail_call_path),
    'airpods_action': pygame.mixer.Sound(aml_crane_call_path),
    'ipad': pygame.mixer.Sound(aml_cuckoo_bird_song_path),
    'macos': pygame.mixer.Sound(aml_american_woodcock_path),
    'airpods': pygame.mixer.Sound(aml_tawny_owl_call_path),
    'beats': pygame.mixer.Sound(aml_crow_path),
    'default': pygame.mixer.Sound(aml_warbling_vireo_path)
}

# -----> apple_bleee Data <-----


state = {}

# NOTE:
# state structure example
#
# state = {
#     'C8:69:CD:0E:13:E4': {
#         'state': 'Disabled',
#         'device': 'iPhone',
#         'wifi': 'On',
#         'os': 'iOS13',
#         'phone': '',
#         'time': 1581980104,
#         'notes': ''
#     },
#     "...": {...}
# }


# -----> Init Background Audio <-----


bg_media_dir = mda_dir + bg_dir

bg_gentle_rain_path = bg_media_dir + bg_gentle_rain + '.wav'
bg_light_rain_path = bg_media_dir + bg_light_rain + '.wav'
bg_thunder_lightning_rain_path = bg_media_dir + bg_thunder_lightning_rain + '.wav'

# load bg sound
bg_path = bg_media_dir + bg_rainforest_ambiance + '.wav'
pygame.mixer.music.load(bg_path)

# set init bg sound volume
pygame.mixer.music.set_volume(0.5)

# init bg sound and loop forever
pygame.mixer.music.play(loops=-1)


# -----> Data Handlers <-----


def handle_new_data(data):

    # NOTE: kill display
    # npyscreen.blank_terminal()

    # print('new data')
    f = open("ble_forest.log", "a")
    f.write(". \n\n")
    f.close()

    update_state(data)


def update_state(raw_data):
    devices = raw_data.copy()

    for dev in devices:
        dev_data = devices[dev]

        if dev in state:
            # TODO: WARN:
            # 				this is probs not working the way i think it should
            # if state != devices:
            # f = open("ble_forest.log", "a")
            # f.write("state ")
            # f.write(str(state[dev]['state']))
            # f.write("\n")

            # f.write("new data ")
            # f.write(str(dev_data['state']))
            # f.write("\n")

            # f.write(str(state[dev]['state'] != dev_data['state']))
            # f.write("\n\n")
            # f.close()
            if state[dev]['state'] != dev_data['state']:
                f = open("ble_forest.log", "a")
                f.write("not equal!!!!! \n\n")
                f.close()
                handle_device_status_change(dev, dev_data)

        if dev not in state:
            handle_new_device(dev, dev_data)


def handle_new_device(dev, dev_data):
    # print('new device')
    f = open("ble_forest.log", "a")
    f.write("new device \n\n")
    f.close()

    state[dev] = dev_data

    carl = state[dev]

    f = open("ble_forest.log", "a")
    f.write(str(carl))
    f.write("\n\n")
    f.close()

    sound = which_sound_device(dev_data['device'])
    play_sound(sound)
    set_bg_volume()


def handle_device_status_change(dev, dev_data):
    # print('device status has changed')
    f = open("ble_forest.log", "a")
    f.write("device status has changed \n\n")
    f.close()

    sound = which_sound_state(dev_data['device'], dev_data['state'])
    play_sound(sound)


def remove_from_state(dev):
    # print('removing device')
    f = open("ble_forest.log", "a")
    f.write("removing device \n\n")
    f.close()

    del state[dev]


# -----> Sound Handlers <-----


def set_bg_volume():
    num_devices = len(state)

    if num_devices <= 20:
        pygame.mixer.music.set_volume(0.2)
    elif num_devices > 40 and num_devices <= 30:
        pygame.mixer.music.set_volume(0.4)
    elif num_devices > 60 and num_devices <= 45:
        pygame.mixer.music.set_volume(0.6)
    elif num_devices > 80:
        pygame.mixer.music.set_volume(0.8)
    else:
        pygame.mixer.music.set_volume(0.2)


def which_sound_device(device):
    if device == 'iPad':
        return device_status_sound_map['ipad']
    elif device == 'iPhone':
        return device_status_sound_map['iphone']
    elif device == 'MacOS':
        return device_status_sound_map['macos']
    elif device == 'AirPods':
        return device_status_sound_map['airpods']
    elif device == 'Powerbeats3' or 'BeatsX' or 'Beats Solo3':
        return device_status_sound_map['beats']
    else:
        return device_status_sound_map['default']


def which_sound_state(device, state):
    if device == 'iPad' or 'iPhone' or 'MacOS':
        if state == 'Idle':
            return device_status_sound_map['idle']
        elif state == 'Lock screen':
            return device_status_sound_map['lock_screen']
        elif state == 'Home screen':
            return device_status_sound_map['home_screen']
        elif state == 'Off':
            return device_status_sound_map['off']
        else:
            return device_status_sound_map['default']
    elif device == 'AirPods' or 'Powerbeats3' or 'BeatsX' or 'Beats Solo3':
        if state == 'Case:Closed' or 'Case:open':
            return device_status_sound_map['case_action']
        elif re.search(r'\bout\b', state) or re.search(r'\bin\b', state):
            return device_status_sound_map['airpods_action']
        else:
            return device_status_sound_map['default']
    else:
        return device_status_sound_map['default']


def play_sound(sound, volume=0.5):
    sound.set_volume(volume)

    # NOTE:
    # find_channel(): find and return an inactive Channel.
    # if no inactive channels and the force argument is True,
    # will find the Channel with the longest running Sound and return it.
    pygame.mixer.find_channel(True).play(sound)
