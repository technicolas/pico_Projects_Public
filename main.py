from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
from oled import Write, GFX, SSD1306_I2C
from oled.fonts import ubuntu_mono_15, ubuntu_mono_20
import utime

led_interne = Pin(25, Pin.OUT)
led_rouge = Pin(15, Pin.OUT)
led_jaune = Pin(14, Pin.OUT)
led_verte = Pin(13, Pin.OUT)

WIDTH =128
HEIGHT= 64
i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)
write15 = Write(oled, ubuntu_mono_15)
write20 = Write(oled, ubuntu_mono_20)

def afficheur(text):
    oled.fill(0)
    write20.text("LED", 0, 0)
    write15.text("Allumee:", 20, 20)
    oled.text(text, 20, 40)
    oled.show()

def cligno(t):
    led_rouge.value(1)
    utime.sleep(t)
    led_rouge.toggle()
    utime.sleep(7*t)
    
    led_jaune.value(1)
    utime.sleep(t)
    led_jaune.toggle()
    utime.sleep(7*t)
    
    led_verte.value(1)
    utime.sleep(t)
    led_verte.toggle()
    utime.sleep(7*t)
    
def cligno2(t,r,j,v):
    led_rouge.value(r)
    led_jaune.value(j)
    led_verte.value(v)
    utime.sleep(t)

def cligno3(t):
    led_interne.value(1)
    utime.sleep(t)
    led_interne.toggle()
    utime.sleep(t)

while True:
#     cligno(0.2)
    afficheur("ROUGE")
    cligno2(1,1,0,0)
    afficheur("ORANGE")
    cligno2(2,0,1,0)
    afficheur("VERTE")
    cligno2(1,0,0,1)
    afficheur("ORANGE")
    cligno2(2,0,1,0)
#     cligno3(1)
