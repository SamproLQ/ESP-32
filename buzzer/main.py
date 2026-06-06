import network
import espnow
from machine import Pin, PWM

import time
import asyncio as asyncio

push_buttonf = Pin(13, Pin.IN)
push_buttond = Pin(12, Pin.IN)
buzzer = PWM(Pin(14), freq=1000, duty=1000)
can = True

async def able():
    global can
    await asyncio.sleep(.5)
    can = True

while True: # Mensaje al oprimir el boton
    
  
  logic_state1 = push_buttonf.value()
  if logic_state1 == True:     # if pressed the push_button
    #led.value(1) 
    if can == True:
        can = False
        try:
            buzzer.freq(buzzer.freq()+100)  
        except:
            buzzer.freq(20000)
        asyncio.run(able())
        print(buzzer.freq())
          
  
  logic_state2 = push_buttond.value()
  if logic_state2 == True:     # if pressed the push_button
      #led.value(1)             # led will turn ON
      if can == True:
        can = False
        try:
            buzzer.freq(buzzer.freq()-100)
        except:
            buzzer.freq(1)
        asyncio.run(able()) 
        print(buzzer.freq())