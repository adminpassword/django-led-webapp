from django.db import models
import time
from rpi_ws281x import *


# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create your models here.

class Boulder(models.Model):
    boulder_description = models.CharField(max_length=300)
    boulder_difficulty = models.CharField(max_length=100)
    boulder_creator = models.CharField(max_length=15)
    boulder_name = models.CharField(max_length=50)
    boulder_data = models.CharField(max_length=400)
    def find_color(colorNum):
        if colorNum=="1":
            return Color(255,0,0)
        if colorNum=="2":
            return Color(0,255,0)
        if colorNum=="3":
            return Color(0,0,255)
        if colorNum=="4":
            return Color(255,255,0)

    def led_logic(self):
            n=4
            chunks = [self.boulder_data[i:i+n] for i in range(0, len(self.boulder_data), n)]
            z=0
            color=""
            id=""
            for i in chunks:
                z=0
                id=""
                color = i[z]
                z=z+1
                id = id + i[z]
                z=z+1
                id = id + i[z]
                z=z+1
                id = id + i[z]

                print(color+" color and the id "+id)

                strip.setPixelColor(int(id), findColor(color))

                # Create NeoPixel object with appropriate configuration.
                strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
                # Intialize the library (must be called once before other functions).
                strip.begin()
                stip.show
                time.sleep(1000)
                colorWipe(strip, Color(0,0,0), 10)
