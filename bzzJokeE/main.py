import network
import espnow
from machine import Pin, PWM

import time
import asyncio as asyncio

# Extra vars
switch = False
# Inicializa ESP-NOW
e = espnow.ESPNow()
e.active(True)

# MAC
mac = [b'pK\xca\x8f7\xa0',b'pK\xca\x8f\x12\xf4']

# Configura Wi-Fi en modo estación
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.config(channel=1)  # mismo canal que el receptor

#led = Pin(14, Pin.OUT)    # Button
push_button = Pin(13, Pin.IN)  # 23 number pin is input
push_2 = Pin(12, Pin.IN)
led = Pin(2, Pin.OUT)

# Agrega el peer
for peer in mac:
  e.add_peer(peer)

e.send("Hola muendo") # Mensaje de prueva

while True: # Mensaje al oprimir el boton
  
  logic_state = push_button.value()
  logic_2 = push_2.value()
  if logic_state or logic_2:     # if pressed the push_button
      led.value(1)             # led will turn ON
      if not switch:
        print("ON")
        e.send("ON")
        if logic_state:
            print("hgh")
            e.send("hgh")
        elif logic_2:
            print("low")
            e.send("low")
        switch = True
  else:                       # if push_button not pressed
      led.value(0)  
      if switch:
          print("OFF")
          e.send("OFF")
          switch = False  
        
    
e.send(b'end') # Cortar conexion
