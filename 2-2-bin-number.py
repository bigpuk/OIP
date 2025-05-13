import RPi.GPIO as RG
import time 
import matplotlib.pyplot as plt 
plt.plot ([0, 5, 16, 32, 64, 127], [0.057, 0.137, 0.458, 0.869, 1.677, 3.255])
plt.show()

dac = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 0, 0, 1, 0, 0, 0, 0]
RG.setmode(RG.BCM)
RG.setup(dac, RG.OUT)
RG.output(dac, number)
time.sleep (12)
RG.output (dac, 0)
RG.cleanup()


