import RPi.GPIO as GPIO
import pygame
from pygame.locals import *
import time
import sys


pygame.init()
pygame.display.set_mode((1,1))


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


try:
    while True:
    # Keyboard character retrieval method is called and saved
    # into variable
        keys = pygame.key.get_pressed()
    # The car will drive forward when the "w" key is pressed
        if keys[K_UP]:
            print("up")
            GPIO.output(20,GPIO.HIGH)
            GPIO.output(TiltStepPin,GPIO.LOW)
            time.sleep(0.001)
            GPIO.output(TiltStepPin,GPIO.HIGH)
            time.sleep(0.001)
    # The car will reverse when the "s" key is pressed
        if keys[K_DOWN]:
            print("down")
            GPIO.output(20,GPIO.LOW)
            GPIO.output(TiltStepPin,GPIO.LOW)
            time.sleep(0.001)
            GPIO.output(TiltStepPin,GPIO.HIGH)
            time.sleep(0.001)
    # The "a" key will toggle the steering left
        if keys[K_LEFT]:
            print("left")
            GPIO.output(7,GPIO.LOW)
            GPIO.output(PanStepPin,GPIO.LOW)
            time.sleep(0.001)
            GPIO.output(PanStepPin,GPIO.HIGH)
            time.sleep(0.001)

    # The "d" key will toggle the steering right
        if keys[K_RIGHT]:
            print("right")
            GPIO.output(7,GPIO.HIGH)
            GPIO.output(PanStepPin,GPIO.LOW)
            time.sleep(0.001)
            GPIO.output(PanStepPin,GPIO.HIGH)
            time.sleep(0.001)
        time.sleep(0,02)
    pygame.event.pump()
except:
    GPIO.cleanup()
