import pyfirmata
import time
import logging

logging.basicConfig(level=logging.INFO)

comport = 'COM4'

def led(fingerUp, led_pins):
    """Function to set the LED states based on finger up status."""
    if len(fingerUp) == 5:
        for i, pin in enumerate(led_pins):
            pin.write(fingerUp[i])
    else:
        logging.error("Invalid fingerUp list. It should contain 5 elements.")

def open_port(board):
    """Ensure the board is properly connected and the port is open."""
    if not board.sp.isOpen():
        logging.info("Port is not open. Attempting to open...")
        board.sp.open()
    else:
        logging.info("Port is already open.")

def close_port(board):
    """Close the port properly."""
    if board.sp.isOpen():
        logging.info("Closing port...")
        board.sp.close()

try:
    logging.info("Trying to connect to the board...")
    board = pyfirmata.Arduino(comport, timeout=5)  
    logging.info("Board connected.")
    time.sleep(1)

    led_pins = [
        board.get_pin('d:8:o'),
        board.get_pin('d:9:o'),
        board.get_pin('d:10:o'),
        board.get_pin('d:11:o'),
        board.get_pin('d:12:o')
    ]

    open_port(board)

    patterns = [
        [0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0],
        [0, 1, 1, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1]
    ]

    for pattern in patterns:
        logging.info(f"Setting LEDs to: {pattern}")
        led(pattern, led_pins)
        time.sleep(1)

except pyfirmata.util.SerialException as e:
    logging.error(f"Serial error: {e}")
except Exception as e:
    logging.error(f"Unexpected error: {e}")

finally:
    try:
        logging.info("Turning off LEDs and closing board.")
        led([0, 0, 0, 0, 0], led_pins)   
        logging.info("Disconnected from Arduino.")
    except Exception as e:
        logging.error(f"Error during cleanup: {e}")



