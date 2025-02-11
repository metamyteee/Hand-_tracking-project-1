import cv2
from cvzone.HandTrackingModule import HandDetector
import controller as cnt
import serial
import time

def open_serial_port():
    try:
        ser = serial.Serial('COM4', 9600)  
        print("Trying to open port...")
        
        if ser.is_open:
            print("Port is open")
        else:
            ser.open()
            print("Port was closed. It is now open.")
        return ser
    except serial.SerialException as e:
        print(f"Error opening port: {e}")
        return None

ser = open_serial_port()

detector = HandDetector(detectionCon=0.8, maxHands=1)
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)  
    
    hands, img = detector.findHands(frame)  
    
    if hands:
        hand = hands[0]
        lmList = hand["lmList"] 
        fingerUp = detector.fingersUp(hand)  

        print(f"Detected fingers: {fingerUp}")
        
        if ser is not None and ser.is_open:
            print("Port is open, writing data...")
            try:
                
                ser.write(bytes([fingerUp[1]]))  
            except Exception as e:
                print(f"Error while writing to the serial port: {e}")
        else:
            print("Port is closed, trying to reopen...")
            ser = open_serial_port()  

        cnt.led(fingerUp, cnt.led_pins)
        
        if fingerUp == [0, 0, 0, 0, 0]:
            cv2.putText(frame, 'Finger count: 0', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 0, 0, 0]:
            cv2.putText(frame, 'Finger count: 1', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 1, 0, 0]:
            cv2.putText(frame, 'Finger count: 2', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 1, 1, 0]:
            cv2.putText(frame, 'Finger count: 3', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [0, 1, 1, 1, 1]:
            cv2.putText(frame, 'Finger count: 4', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)
        elif fingerUp == [1, 1, 1, 1, 1]:
            cv2.putText(frame, 'Finger count: 5', (20, 460), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow("frame", frame)

    k = cv2.waitKey(1)
    if k == ord("k"):
        break

video.release()
cv2.destroyAllWindows()

if ser is not None and ser.is_open:
    ser.close()
    print("Serial port closed.")
