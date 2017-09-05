import getch
import RPi.GPIO as GPIO
import time
# start application with python3


SlideStepPin = 23
PanStepPin = 8
TiltStepPin = 16

GPIO.setmode(GPIO.BCM)

GPIO.setup(21,GPIO.OUT)

GPIO.setup(SlideStepPin,GPIO.OUT)#step pin
GPIO.setup(24,GPIO.OUT)#dir pin

GPIO.setup(PanStepPin,GPIO.OUT)#step pin
GPIO.setup(7,GPIO.OUT)#dir pin

GPIO.setup(TiltStepPin,GPIO.OUT)#step pin
GPIO.setup(20,GPIO.OUT)#dir pin

GPIO.setup(22,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)

GPIO.output(24,GPIO.HIGH)
GPIO.output(7,GPIO.LOW)
GPIO.output(20,GPIO.LOW)
GPIO.output(21,GPIO.LOW)

GPIO.output(22,GPIO.HIGH)
GPIO.output(11,GPIO.HIGH)
GPIO.output(19,GPIO.HIGH)

stepsize = 1
try:
    while True:
        choice = getch.getch()
        if choice == "w":
            print("up")
            for x in range (0,stepsize):
                GPIO.output(20,GPIO.LOW)
                GPIO.output(TiltStepPin,GPIO.LOW)
                time.sleep(0.001)
                GPIO.output(TiltStepPin,GPIO.HIGH)
                time.sleep(0.001)
        if choice == "s":
            print("down")
            for x in range (0,stepsize):
                GPIO.output(20,GPIO.HIGH)
                GPIO.output(TiltStepPin,GPIO.LOW)
                time.sleep(0.001)
                GPIO.output(TiltStepPin,GPIO.HIGH)
                time.sleep(0.001)
        if choice == "a":
            print("left")
            for x in range (0,stepsize):
                GPIO.output(7,GPIO.HIGH)
                GPIO.output(PanStepPin,GPIO.LOW)
                time.sleep(0.001)
                GPIO.output(PanStepPin,GPIO.HIGH)
                time.sleep(0.001)
        if choice == "d":
            print("right")
            for x in range (0,stepsize):
                GPIO.output(7,GPIO.LOW)
                GPIO.output(PanStepPin,GPIO.LOW)
                time.sleep(0.001)
                GPIO.output(PanStepPin,GPIO.HIGH)
                time.sleep(0.001)
        if choice == "z":
            print("slide left")
            GPIO.output(24,GPIO.LOW)
            for x in range (0,stepsize):
                GPIO.output(SlideStepPin,GPIO.LOW)
                time.sleep(0.001)
                GPIO.output(SlideStepPin,GPIO.HIGH)
                time.sleep(0.001)
        if choice == "x":
            print("slide right")
            GPIO.output(24,GPIO.HIGH)
            for x in range (0,stepsize):
                GPIO.output(SlideStepPin,GPIO.LOW)
                time.sleep(0.001)
                GPIO.output(SlideStepPin,GPIO.HIGH)
                time.sleep(0.001)
        if choice == "1":
            print("right")
            stepsize = int(choice)
        if choice == "2":
            print("right")
            stepsize = int(choice)*2
except:
    print("exit")
    GPIO.cleanup()

