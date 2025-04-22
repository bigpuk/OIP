import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = 1)
GPIO.setup(comp, GPIO.IN)

def dec2bin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]

def adc():
    for value in range(256):
        GPIO.output(dac, dec2bin(value))
        time.sleep(0.01)
        if GPIO.input(comp) == 1:
            return value
    return 256

try:
    while True:
        value = adc()
        voltage = float(value) / 256.0 * 3.3
        print(f" {voltage:.2f}V")
finally:
    GPIO.output(dac, 0)

    GPIO.cleanup()