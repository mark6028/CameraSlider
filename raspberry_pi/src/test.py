import sys
import getch

try:
    while True:
        choice = getch.getch()
        if choice == "w":
            print("up")
        if choice == "s":
            print("down")
        if choice == "a":
            print("left")
        if choice == "d":
            print("right")
except:
    print("exit")
