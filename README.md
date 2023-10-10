# Keylogger Project

## DISCLAIMER
This project is purely educational and is intended to demonstrate the capabilities of Python in the realm of cybersecurity. Unauthorized keylogging is illegal. I am not responsible for any misuse or damage caused by this script.

## Overview
This project is a simple Python keylogger that logs key presses and optionally sends them to a specified host and port via netcat. It was developed as a learning exercise to understand the principles of keylogging, network communication, and differant ways python can be used / misused.

## What I Learned

### 1. Python Programming
- **File Handling:** Learned how to create, write, and manage log files using Python’s `os` and `logging` modules.
- **Exception Handling:** Understood the importance of handling exceptions to manage runtime errors, especially in network communications and key event handling.

### 2. Keylogging Principles
- **Event Listening:** Explored the `pynput` library to listen to keyboard events and learned how to handle key press and release events.
- **Asynchronous Programming:** Understood the concept of asynchronous programming, as the keylogger listens for key events in the background while performing other tasks (e.g., logging or sending data via netcat).

### 3. Network Communication
- **Socket Programming:** Learned the basics of socket programming in Python, establishing TCP connections, and sending data over the network using the `socket` module.
- **Data Transmission:** Explored how to transmit data (key logs) securely and reliably from one system to another over the network.

### 4. Ethical Considerations
- **Ethical Use:** Understood the ethical implications and legal boundaries related to keylogging and data transmission. Emphasized the importance of respecting privacy and using cybersecurity knowledge responsibly and legally.
- **User Consent:** Learned the importance of obtaining user consent and ensuring transparency when developing and deploying cybersecurity tools.

## Usage
This keylogger allows users to:
- Log key presses to a local text file.
- Optionally send key logs to a remote server via netcat.

### Prerequisites
- Python 3.x
- `pynput` library

### Running the Keylogger
1. Ensure all prerequisites are installed.
2. Run the script using Python: `python keylogger.py`
3. Follow the prompts to configure netcat logging if desired.
4. Press the 'Escape' key to stop the keylogger.

## Future Improvements
- Implement encryption for key logs during transmission to enhance security.
- Develop a GUI for user-friendly interaction and configuration.
- Enhance the keylogger to capture more types of input and system events.
- Add a feature that if closed, sends the .txt file to an email as a fail-safe.

## Conclusion
This project served as a practical application of Python programming, network communication, and cybersecurity principles. It emphasized the importance of ethical considerations and responsible use of cybersecurity knowledge.

## License
This project is for educational purposes and is not intended for malicious use. Ensure to comply with all applicable local, state, and federal laws regarding cybersecurity and data protection.
