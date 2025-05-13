import RPi.GPIO as RG 
import time 

leds = [21, 20, 16, 12, 7, 8, 25, 24]
RG.setmode(RG.BCM)
RG.setup(leds, RG.OUT)

for i in range (3):
    for j in range (8):
        RG.output(leds[j], 1)
        time.sleep(0.2)
        RG.output(leds[j], 0)

RG.output(leds, 0)
RG.cleanup()