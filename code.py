import time
import audioio
import board
import digitalio

buttonA = digitalio.DigitalInOut(board.BUTTON_A)
buttonA.direction = digitalio.Direction.INPUT
buttonA.pull = digitalio.Pull.DOWN

wave_file = open("test.wav", "rb")
wave = audioio.WaveFile(wave_file)
audio = audioio.AudioOut(board.A0)

while True:
    while not buttonA.value:
        pass
    audio.play(wave)
    print("Done!")