import network
import time
from machine import Pin
import dht

SSID = 'WiFi_SSID'
PASSWORD = 'WiFi_Şifresi'

dht_pin = Pin(5)
relay_pin = Pin(4, Pin.OUT)
sensor = dht.DHT11(dht_pin)

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    while not wlan.isconnected():
        time.sleep(1)

def control_temperature():
    try:
        sensor.measure()
        temp = sensor.temperature()
        hum = sensor.humidity()
        if temp > 30:
            relay_pin.on()
        else:
            relay_pin.off()
    except Exception as e:
        pass

def main():
    connect_wifi()
    while True:
        control_temperature()
        time.sleep(5)

if __name__ == "__main__":
    main()















---