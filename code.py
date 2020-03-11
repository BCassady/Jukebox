import time
import audioio
import board
import digitalio
import neopixel
import os

pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, auto_write=False, brightness = 0.2)
buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.DOWN
buttonB = digitalio.DigitalInOut(board.BUTTON_B)
buttonB.direction = digitalio.Direction.INPUT
buttonB.pull = digitalio.Pull.DOWN
selection = 0 # Current song selection
pixels[selection] = (0, 0, 255)
pixels.show()
''' This is commented out until all songs are loaded in
songs = [song for song in os.listdir('songs/') if song.endswith('.wav')]
waves = []
for song in songs:
    wave_file = open(song, "rb")
    waves.append(audioio.WaveFile(wave_file))
'''
audio = audioio.AudioOut(board.A0)

while True:
    # Adjust song selection when button is pressed
    if buttonA.value:
        pixels[selection] = (0,0,0)
        selection += 1
        if(selection>9):
            selection = 0
        pixels[selection] = (0, 0, 255)
        pixels.show()
        time.sleep(0.25)
    if buttonB.value:
        #audio.play(waves[selection])
        continue