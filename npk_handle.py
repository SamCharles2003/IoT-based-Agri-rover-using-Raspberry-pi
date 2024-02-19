import RPi.GPIO as GPIO
import soil_test
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import time
factory = PiGPIOFactory()
servo = Servo(10,pin_factory=factory)

def test():
    servo.mid()
    soil_test.test()
    servo.min()


def handle(mode):
    if mode == "DOWN":
        servo.mid()
    else:
        servo.min()