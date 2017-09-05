import RPi.GPIO as GPIO
#import pygame
#from pygame.locals import *
import time
import sys
import Tkinter as tk

#pygame.init()
#pygame.display.set_mode((1,1))


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
stepsize = 0

try:

    def key(event):
        global stepsize
        """shows key or tk code for the key"""
        if event.keysym == 'Escape':
            root.destroy()
            GPIO.cleanup()
        if event.char == event.keysym:
            # normal number and letter characters
            print( 'Normal Key %r' % event.char )
            if event.keysym == "a":
                GPIO.output(24,GPIO.LOW)
                for x in range (0,stepsize):
                    GPIO.output(SlideStepPin,GPIO.LOW)
                    time.sleep(0.001)
                    GPIO.output(SlideStepPin,GPIO.HIGH)
                    time.sleep(0.001)
            elif event.keysym == "d":
                GPIO.output(24,GPIO.HIGH)
                for x in range (0,stepsize):
                    GPIO.output(SlideStepPin,GPIO.LOW)
                    time.sleep(0.001)
                    GPIO.output(SlideStepPin,GPIO.HIGH)
                    time.sleep(0.001)
        elif len(event.char) == 1:
            # charcters like []/.,><#$ also Return and ctrl/key
            print( 'Punctuation Key %r (%r)' % (event.keysym, event.char) )
        else:
            # f1 to f12, shift keys, caps lock, Home, End, Delete ...
            print( 'Special Key %r' % event.keysym )
            if "F" in event.keysym:
                stepsize = int(event.keysym[1:]) * 2
                print(stepsize)
            if event.keysym == "Down":
                GPIO.output(20,GPIO.HIGH)
                for x in range (0,stepsize):
                    GPIO.output(TiltStepPin,GPIO.LOW)
                    time.sleep(0.001)
                    GPIO.output(TiltStepPin,GPIO.HIGH)
                    time.sleep(0.001)
            elif event.keysym == "Up":
                GPIO.output(20,GPIO.LOW)
                for x in range (0,stepsize):
                    GPIO.output(TiltStepPin,GPIO.LOW)
                    time.sleep(0.001)
                    GPIO.output(TiltStepPin,GPIO.HIGH)
                    time.sleep(0.001)
            elif event.keysym == "Left":
                GPIO.output(7,GPIO.LOW)
                for x in range (0,stepsize):
                    GPIO.output(PanStepPin,GPIO.LOW)
                    time.sleep(0.001)
                    GPIO.output(PanStepPin,GPIO.HIGH)
                    time.sleep(0.001)
            elif event.keysym == "Right":
                GPIO.output(7,GPIO.HIGH)
                for x in range (0,stepsize):
                    GPIO.output(PanStepPin,GPIO.LOW)
                    time.sleep(0.001)
                    GPIO.output(PanStepPin,GPIO.HIGH)
                    time.sleep(0.001)

    root = tk.Tk()
    print( "Press a key (Escape key to exit):" )
    root.bind_all('<Key>', key)
    # don't show the tk window
    #root.withdraw()
    root.mainloop()

except:
    GPIO.cleanup()
