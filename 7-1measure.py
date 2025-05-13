import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

leds = [2, 3, 4, 17, 27, 22, 10, 9]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
max_signal = 255
max_voltage = 2.7

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)

GPIO.output(troyka, 0)

def dec2bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i
        GPIO.output(dac, [int(bit) for bit in bin(k)[2:].zfill(8)])
        time.sleep(0.008)

        if GPIO.input(comp) == GPIO.HIGH:
            k -= 2**i

    return k

def show_num_on_leds(num):
    bin_num = dec2bin(num)
    GPIO.output(dac, bin_num)
    return 0

voltage_meas = []
time_meas = []

try:
    experiment_start = time.time()
    troyka_signal = 0

    GPIO.output(troyka, 1)
    while(troyka_signal < 207):
        troyka_signal = adc()
        print("signal:", troyka_signal)
        print("voltage:", troyka_signal / (max_signal + 1) * max_voltage)
        
        voltage_meas.append(troyka_signal)
        time_meas.append(time.time() - experiment_start)
    GPIO.output(troyka, 0)

    while(troyka_signal > 170):
        troyka_signal = adc()
        print("second part")
        print("signal:", troyka_signal)
        print("voltage:", troyka_signal / (max_signal + 1) * max_voltage)
 
        voltage_meas.append(troyka_signal)
        time_meas.append(time.time() - experiment_start)

    experiment_end = time.time()
    experiment_duration = experiment_end - experiment_start

finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup()

with open("settings.txt", "w") as file:
    file.write(str(len(voltage_meas) / experiment_duration))
    file.write(str(max_voltage / (max_signal+1)))

voltage_meas_text = "\n".join([str(i) for i in voltage_meas])

with open("data.txt", "w") as file:
    file.write(voltage_meas_text)


print("---Experiment report---")
print("Experiment duration:", experiment_duration, "s")
print("Measurements period:", experiment_duration / len(voltage_meas), "s")
print("Sampling frequency:", len(voltage_meas) / experiment_duration, "Hz")
print("ADC quantization shift:", max_voltage / (max_signal+1), "V")

plt.plot(time_meas, voltage_meas)
plt.show()