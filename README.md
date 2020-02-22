# BLE FOREST

## apple_ble

All code for ble sniffing and utils comes from [apple_bleee - hexway ](https://github.com/hexway/apple_bleee)

## TODO

### Code

[apple_ble fork](https://github.com/nkernis/apple_bleee)

- [ ] Pick Sounds
- [ ] Background audio
	- Intensity mapped to # of devices
- [ ] Map events to unique sounds
- [ ] Connect music to apple_ble data
	- Fn to get data from
		- [def print_results():](https://github.com/nkernis/apple_bleee/blob/master/ble_read_state.py#L591)
	- Fn to trigger cleaning data
		- [def clear_zombies():](https://github.com/nkernis/apple_bleee/blob/master/ble_read_state.py#L577)

### Fabrication

- [ ] Design enclosure
- [ ] Test finishing process
	- Sand, prime, sand, paint
- [ ] LED?

## Resources

### Code

- https://www.pygame.org/docs/ref/music.html
- https://github.com/hexway/apple_bleee
	- https://hexway.io/research/apple-bleee/

#### Setting Up RPI

- How to instal
	- https://github.com/nkernis/apple_bleee
- If issue with `LC_ALL` and the rest
	- https://raspberrypi.stackexchange.com/questions/43550/unable-to-reconfigure-locale-in-raspberry-pi
- Install python3 on Raspian
	- `sudo apt install python3 -y`
	- If need to remove manual installation
		- `apt-get autoremove python3`
- Fix for Pillow (just requirements)
	- https://github.com/python-pillow/Pillow/issues/3077#issuecomment-518978148
- bs4
	- https://stackoverflow.com/questions/11783875/importerror-no-module-named-bs4-beautifulsoup
- socket.AF_BLUETOOTH (WARN: must be done before compiling python3)
	- https://stackoverflow.com/questions/29107537/missing-socket-af-bluetooth-in-anaconda-python
- can't install pygame
	- https://forum.ubiquityrobotics.com/t/im-trying-to-install-some-software-packages-but-i-keep-getting-errors/363/3

### Fabrication

- https://www.makerbot.com/professional/post-processing/painting/

### Sounds

Funny one? http://soundbible.com/2039-Tree-Fall-Small.html

#### http://soundbible.com/

- *Background*
	- http://soundbible.com/1818-Rainforest-Ambience.html
- *Animals*
	- http://soundbible.com/2033-Frogs.html#Frogs%20Sound
	- http://soundbible.com/2180-Meadowlark.html
	- http://soundbible.com/1849-Killdeer-Song.html
	- http://soundbible.com/1846-Warbling-Vireo.html
	- http://soundbible.com/1430-Peacock.html
	- http://soundbible.com/1200-American-Woodcock.html
- *Not Natural*
	- http://soundbible.com/1645-Pling.html
	- http://soundbible.com/2067-Blop.html

#### http://soundbible.com/

- *Background*
	- http://www.orangefreesounds.com/gentle-rain-sounds/
	- http://www.orangefreesounds.com/thunder-lightning-with-rain/
	- http://www.orangefreesounds.com/light-rain-sound-effect/
- *Animals*
	- http://www.orangefreesounds.com/eurasian-collared-dove-call/
	- http://www.orangefreesounds.com/woodpecker-pecking-sound/
	- http://www.orangefreesounds.com/crow-voice/
	- http://www.orangefreesounds.com/bobwhite-quail-call/
	- http://www.orangefreesounds.com/tawny-owl-call/
	- http://www.orangefreesounds.com/crane-bird-call-sounds/
	- http://www.orangefreesounds.com/cuckoo-bird-song/
