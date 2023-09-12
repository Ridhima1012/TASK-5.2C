import RPi.GPIO as GPIO
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys

GPIO.setmode(GPIO.BCM)
RED_PIN = 17  
YELLOW_PIN = 19
GREEN_PIN = 21
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(YELLOW_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)


def RedLED_ON():
    GPIO.output(RED_PIN, GPIO.HIGH)
    GPIO.output(YELLOW_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)

def YellowLED_ON():
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(YELLOW_PIN, GPIO.HIGH)
    GPIO.output(GREEN_PIN, GPIO.LOW)
   
def GrennLED_ON():
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(YELLOW_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.HIGH)

def EXIT_IT():
    GPIO.output(RED_PIN, GPIO.LOW)
    GPIO.output(YELLOW_PIN, GPIO.LOW)
    GPIO.output(GREEN_PIN, GPIO.LOW)




app = QApplication([])
win = QMainWindow()
win.setWindowTitle("TASK 5.2C")
win.resize(500,200)
win.move(400,200)


label = QLabel("Blinking LEDS", win)
label.move(20,20)

RedLED = QPushButton("TO BLINK RED LED , PRESS HERE", win)
RedLED.move(20,40)
RedLED.clicked.connect(RedLED_ON)

YellowLED = QPushButton("TO BLINK YELLOW LED , PRESS HERE", win)
YellowLED.move(60,40)
YellowLED.clicked.connect(YellowLED_ON)

GreenLED = QPushButton("TO BLINK GREEN LED < PRESS HERE", win)
GreenLED.move(80,40)
GreenLED.clicked.connect(GrennLED_ON)

EXIT= QPushButton("TO BLINK GREEN LED < PRESS HERE", win)
EXIT.move(80,40)
EXIT.clicked.connect(EXIT_IT)

win.show()

sys.exit(app.exec_())