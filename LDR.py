import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
ldr_thrhold = 100000
LDR_PIN=18
LIGHT_PIN=26
GPIO.setup(LIGHT_PIN,GPIO.OUT)
GPIO.output(LIGHT_PIN,False)
def readLDR(pin):
    reading=0
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)
    time.sleep(0.1)
    GPIO.setup(pin,GPIO.IN)
    while(GPIO.input(pin)==False):
        reading+=1
        if reading>ldr_thrhold:
            break
    return reading
def switchon(pin):
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,True)
def switchoff(pin):
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)
try:
    while True:
        ldr_reading = readLDR(LDR_PIN)
        print(ldr_reading)
        if ldr_reading<ldr_thrhold:
            switchoff(LIGHT_PIN)
        else:
            switchon(LIGHT_PIN)
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()
