import imageio as iio
import requests
from PIL import Image
import io
import RPi.GPIO as GPIO
from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
import time
factory = PiGPIOFactory()
servo = Servo(17,pin_factory=factory)



def detect(direction):
    try:
        if direction == "LEFT":
            print("cam left")
            servo.max()

        elif direction == "RIGHT":
            servo.min()

        camera = iio.get_reader("<video0>")
        screenshot = camera.get_data(0)
        camera.close()
        pil_image = Image.fromarray(screenshot)
        image_io = io.BytesIO()
        pil_image.save(image_io, format='JPEG')
        image_bytes = image_io.getvalue()
        url = "http://192.168.55.215:5500/image"
        files = {'file': image_bytes}
        response = requests.post(url, files=files)
        prediction = response.text
        servo.mid()

        print(prediction)
    except Exception as e:
        return e