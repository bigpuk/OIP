import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

dac = [26, 19, 13, 6, 5, 11, 9, 10]

def decimal2binary(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


try:
    x = input("Введите значение времени сигнала: ")
    try:
        while True:
            y = float(x)

            for i in range(256):
                GPIO.output(dac, d)


except ValueError:
    print("Inapropriate period!")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")