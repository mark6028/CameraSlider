from pynput import keyboard

def on_press(key):
    try:
        k = key.name # other keys
        if key == keyboard.Key.esc: return False # stop listener
        if k == 'down':
            print("down")
        elif k == 'up':
            print("up")
        elif k == 'right':
            print("right")
        elif k == 'left':
            print("left")
    except:
        return False
lis = keyboard.Listener(on_press=on_press)
lis.start() # start to listen on a separate thread
lis.join() # no this if main thread is polling self.keys
