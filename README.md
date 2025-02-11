# Hand Gesture Controlled LED System

## Overview
This project allows controlling LEDs using hand gestures detected via a webcam. It utilizes OpenCV for hand tracking and PyFirmata for Arduino communication.

## Features
- Real-time hand detection using OpenCV and `cvzone.HandTrackingModule`
- LED control based on the number of fingers detected
- Serial communication between the computer and an Arduino board

## Requirements
### Hardware:
- Arduino board (tested on Arduino Uno)
- LEDs (5x)
- Resistors (as needed for LEDs)
- Webcam

### Software:
- Python 3.x
- OpenCV (`cv2`)
- `cvzone` for hand detection
- `pyfirmata` for Arduino communication
- `serial` for serial port handling

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/hand-gesture-led.git
   cd hand-gesture-led
   ```
2. Install dependencies:
   ```sh
   pip install opencv-python pyfirmata cvzone pyserial
   ```

## File Description
### `controller.py`
- Establishes connection with the Arduino board
- Controls LED states based on detected hand gestures
- Handles serial communication errors

### `new.py`
- Captures video from the webcam
- Detects hand gestures using `cvzone.HandTrackingModule`
- Communicates with `controller.py` to control LEDs
- Displays the number of detected fingers on the screen

## Usage
1. Connect the Arduino board to your computer.
2. Upload the Firmata firmware to the Arduino.
3. Run the script:
   ```sh
   python new.py
   ```
4. Show hand gestures in front of the webcam to control LEDs.
5. Press 'k' to exit the application.

## Troubleshooting
- **Port issues:** Ensure the correct COM port is used in `controller.py` and `new.py`.
- **Hand detection not working?** Increase `detectionCon` in `HandDetector`.
- **LEDs not responding?** Verify Arduino connections and check if Firmata is uploaded.


