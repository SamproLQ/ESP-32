import network

wlan = network.WLAN(network.STA_IF)  # interfaz WiFi en modo estación
mac = wlan.config('mac')             # devuelve bytes

print(mac)                           # formato raw (bytes)
print(':'.join('{:02X}'.format(b) for b in mac))  # formato legible
