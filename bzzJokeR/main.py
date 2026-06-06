import network
import espnow
from machine import Pin, PWM

# Extra
frst = False
freqs = [4345, 2765]

# Configura Wi-Fi en modo estación (STA_IF)
sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.config(channel=1)  # mismo canal que el transmisor

# Inicializa ESP-NOW
e = espnow.ESPNow()
e.active(True)

led = Pin(2, Pin.OUT)
buzzer = PWM(Pin(14), freq=1000, duty=0)

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
        buzzer.duty(1000)
        led.value(1)
    if msg == b"OFF":
        buzzer.duty(0)
        led.value(0)
    if msg == b"hgh":
        buzzer.freq(freqs[0])
    if msg == b"low":
        buzzer.freq(freqs[1])
        
    

    # Si llega el mensaje de finalización, rompe el bucle
    if msg == b'end':
        print("Mensaje de finalización recibido. Saliendo...")
        break