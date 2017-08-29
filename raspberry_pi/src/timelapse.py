import time
import RPi.GPIO as GPIO

SlideStepPin = 23
PanStepPin = 8
TiltStepPin = 16

SlidePos = 0
PanPos = 0
TiltPos = 0

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
GPIO.output(TiltStepPin,GPIO.HIGH)

def stepnumberoftime(steps,stepPin):
    global SlidePos
    global PanPos
    global TiltPos
    for y in range(0,steps):
        GPIO.output(stepPin,GPIO.LOW)
        time.sleep(0.001)
        GPIO.output(stepPin,GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(stepPin,GPIO.HIGH)
        if stepPin == 23:
            SlidePos+=1
        elif stepPin == 8:
            PanPos+=1
        else stepPin == 16:
            TiltPos+=1

def enablemotors():
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(11,GPIO.HIGH)
    GPIO.output(19,GPIO.HIGH)

def disablemotors():
    GPIO.output(22,GPIO.LOW)
    GPIO.output(11,GPIO.LOW)
    GPIO.output(19,GPIO.LOW)
try:
    for x in range(0,815): #815 amount of photos in one night
        if x == 407:
            GPIO.output(TiltStepPin,GPIO.LOW)
        enablemotors()
        stepnumberoftime(4,PanStepPin)
        stepnumberoftime(10,TiltStepPin)
        stepnumberoftime(2,SlideStepPin)
        disablemotors()
        time.sleep(0.9)
        GPIO.output(21,GPIO.HIGH)
        print(x)
        print("photo\n")
        print("SlidePos:")
        print(SlidePos)
        print("PanPos:")
        print(PanPos)
        print("TiltPos:")
        print(TiltPos)
        time.sleep(1)# shutterspeed: number of seconds
        GPIO.output(21,GPIO.LOW)
except:
    disablemotors()
    GPIO.cleanup()


