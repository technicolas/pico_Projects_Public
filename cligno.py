from machine import Pin
import utime

led_interne = Pin(25, Pin.OUT)
led_rouge = Pin(15, Pin.OUT)
led_jaune = Pin(14, Pin.OUT)
led_verte = Pin(13, Pin.OUT)
   
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
    cligno2(0.2,1,0,0)
    cligno2(0.5,0,1,0)
    cligno2(0.2,0,0,1)
    cligno2(0.5,0,1,0)
#     cligno3(1)
