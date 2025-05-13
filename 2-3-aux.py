import RPi.GPIO as RG 
import time 
leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]
RG.setmode (RG.BCM)
RG.setup(leds, RG.OUT)
RG.setup(aux, RG.IN)
while True:
    for i in range (8):
        RG.output(leds[i], RG.input(aux[i]))

RG.output (leds, 0)
RG.cleanup()