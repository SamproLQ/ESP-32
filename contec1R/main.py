import network
import espnow
from machine import Pin

# Extra
frst = False
cntBtn = 0

# Configura Wi-Fi en modo estación (STA_IF)
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.config(channel=1)  # mismo canal que el transmisor

# Inicializa ESP-NOW
e = espnow.ESPNow()
e.active(True)

led = Pin(2, Pin.OUT) 

print("Esperando mensajes...")

while True:
    host, msg = e.recv(timeout_ms=2000)  # espera 2 segundos
    
    if msg is None:
        continue  # no llegó nada, sigue esperando

    # Muestra el mensaje recibido y la MAC del emisor
    if not frst:
        print("De:", ':'.join('{:02x}'.format(b) for b in host), "Mensaje:", msg)
        frst = True
    else:
        print(" \n",msg.decode(), end=" ")
        
    if msg == b"ON":
        cntBtn+= 1
        print(cntBtn, end="")
        led.value(1)
    else:
        led.value(0)
        
    

    # Si llega el mensaje de finalización, rompe el bucle
    if msg == b'end':
        print("Mensaje de finalización recibido. Saliendo...")
        break