from django.db import models
import time



from rpi_ws281x import *


# LED strip configuration:
LED_COUNT = 550       # Number of LED pixels.
LED_PIN = 18         # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

class Boulder(models.Model):
    boulder_description = models.CharField(max_length=300)
    boulder_difficulty = models.CharField(max_length=100)
    boulder_creator = models.CharField(max_length=15)
    boulder_name = models.CharField(max_length=50)
    boulder_data = models.CharField(max_length=400)


    def turn_off_led(self):
        def blankWipe(strip):
            for i in range(strip.numPixels()):
                strip.setPixelColor(i,Color(0,0,0))

        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.begin()
        blankWipe(strip)
        strip.show()


    def led_logic(self):
        def find_color(colorNum):
            if colorNum=="1":
                c = Color(255,0,0)
                return c
            if colorNum=="2":
                c = Color(0,255,0)
                return c
            if colorNum=="3":
                c = Color(0,0,255)
                return c
            if colorNum=="4":
                c = Color(255,255,0)
                return c
        def colorWipe(strip, color, wait_ms=50):

            for i in range(strip.numPixels()):
                strip.setPixelColor(i, color)
                strip.show()
                time.sleep(wait_ms / 1000.0)
        def set_pixel(strip, color,id):

            print("does it work?")
            strip.setPixelColor(id, color)
            strip.show()
        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.begin()
        #colorWipe(strip, Color(0, 0, 0))
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
            id = id.strip("0")
            print(color+" color and the id ",int(id))


            set_pixel(strip,find_color(color),int(id))
            strip.show()
