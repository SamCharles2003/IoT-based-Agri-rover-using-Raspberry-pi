import RPi.GPIO as GPIO
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import npk_handle
import time
factory = PiGPIOFactory()
servo = Servo(18,pin_factory=factory)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO_TRIG = 8
GPIO_ECHO = 10
GPIO.setup(GPIO_TRIG, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def read():
    while True:
        GPIO.output(GPIO_TRIG, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(GPIO_TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIG, GPIO.LOW)

        while GPIO.input(GPIO_ECHO) == 0:
            start_time = time.time()

        while GPIO.input(GPIO_ECHO) == 1:
            bounce_back_time = time.time()

        pulse_duration = bounce_back_time - start_time
        distance = round(pulse_duration * 17150, 2)
        return distance

    GPIO.cleanup()

def min_distance():
    npk_handle.handle("DOWN")
    servo.min()
    time.sleep(0.1)
    left_distance=read()
    time.sleep(0.1)
    servo.max()
    time.sleep(0.1)
    right_distance=read()
    time.sleep(0.1)
    servo.mid()
    if left_distance<right_distance:
        return "RIGHT"
    else:
        return "LEFT"
    npk_handle.handle("UP")

def alt_direction(init):
    if init == "RIGHT":
        return "LEFT"
    else:
        return "RIGHT"