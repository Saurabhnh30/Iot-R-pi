import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
PIR_PIN=40
LIGHT_PIN=26
GPIO.setup(LIGHT_PIN, GPIO.OUT)
GPIO.output(LIGHT_PIN, False)
def readPIR(pin):
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)
    time.sleep(0.1)
    GPIO.setup(pin, GPIO.IN)
    i = GPIO.input(pin)
    if i == False:
        print("NO INTRUDERS", i)
        GPIO.output(LIGHT_PIN, False)
    elif i == True:
        print("INTRUDERS DETECTED", i)
        GPIO.output(LIGHT_PIN, True)
try:
    while True:
        readPIR(PIR_PIN)
except KeyboardInterrupt:
    GPIO.cleanup()
    exit()
