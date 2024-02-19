import hall_counter as hlc
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO_IN1 = 13
GPIO_IN2 = 15
GPIO_IN3 = 16
GPIO_IN4 = 18

GPIO.setup(GPIO_IN1, GPIO.OUT)
GPIO.setup(GPIO_IN2, GPIO.OUT)
GPIO.setup(GPIO_IN3, GPIO.OUT)
GPIO.setup(GPIO_IN4, GPIO.OUT)

def movement(direction):
    if direction == "FORWARD":

        GPIO.output(GPIO_IN1, 1)  # LOW
        GPIO.output(GPIO_IN2, 0)  # HIGH
        GPIO.output(GPIO_IN3, 1)  # LOW
        GPIO.output(GPIO_IN4, 0)  # HIGH

    elif direction == "REVERSE":

        GPIO.output(GPIO_IN1, 0)  # LOW
        GPIO.output(GPIO_IN2, 1)  # HIGH
        GPIO.output(GPIO_IN3, 0)  # LOW
        GPIO.output(GPIO_IN4, 1)  # HIGH



def rotate(direction):
    if direction == "LEFT":

        GPIO.output(GPIO_IN1, 0)  # LOW
        GPIO.output(GPIO_IN2, 1)  # HIGH
        GPIO.output(GPIO_IN3, 1)  # HIGH
        GPIO.output(GPIO_IN4, 0)  # LOW

    elif direction == "RIGHT":

        GPIO.output(GPIO_IN1, 1)  # HIGH
        GPIO.output(GPIO_IN2, 0)  # LOW
        GPIO.output(GPIO_IN3, 0)  # LOW
        GPIO.output(GPIO_IN4, 1)  # HIGH




def passing():

    GPIO.output(GPIO_IN1, 1)  # HIGH
    GPIO.output(GPIO_IN2, 0)  # LOW
    GPIO.output(GPIO_IN3, 1)  # HIGH
    GPIO.output(GPIO_IN4, 0)  # LOW



def stop():
    GPIO.output(GPIO_IN1, 0)  # LOW
    GPIO.output(GPIO_IN2, 0)  # LOW
    GPIO.output(GPIO_IN3, 0)  # LOW
    GPIO.output(GPIO_IN4, 0)  # LOW