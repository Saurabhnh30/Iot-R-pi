import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
ldr_thrhold = 1000
LDR_PIN=17
IR_PIN =27
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

def readIR(pin):
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)
    time.sleep(0.1)
    GPIO.setup(pin,GPIO.IN)
    if GPIO.input(pin) == True:
        print("Intruder Detected")
    else:
        print("No intruder")   

try:
    while True:
        r  = readLDR(LDR_PIN)
        time.sleep(0.1)
        if r > ldr_thrhold:
            readIR(IR_PIN)
        else:
            flag = 1
        time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()
