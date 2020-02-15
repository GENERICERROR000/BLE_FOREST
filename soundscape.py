import pygame
import time
import threading

directory = 'media/'
files = ['rain.wav', 'frogs.wav', 'waterfall.wav']
loop_files = ['frogs.wav']

pygame.mixer.init()

idx = 0

def setInterval(func, time):
    e = threading.Event()
    while not e.wait(time):
        func()

def play_sound(sound, sec, idx):
    pygame.mixer.Channel(idx).play(sound, -1, sec)

for filename in files:
    pygame.mixer.music.load(media + filename)
    sound = pygame.mixer.Sound(media + filename)

    channel = pygame.mixer.Channel(idx).play(sound, -1)
    sound.set_volume(0.5)
    idx += 1

idx = 0

for filename in loop_files:
    def playsounds():
        print(idx)
        play_sound(sound, 2000, idx)
    pygame.mixer.music.load(media + filename)
    sound = pygame.mixer.Sound(media + filename)
    setInterval(playsounds, 1)
    idx += 1

time.sleep(100000)