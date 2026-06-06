import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

mac = wlan.config('mac')

print(mac)