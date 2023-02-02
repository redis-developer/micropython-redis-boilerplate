import network
import secrets
import time
from picoredis import Redis

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)

while not wlan.isconnected() and wlan.status() >= 0:
    print("Connecting to wifi...")
    time.sleep(0.5)

# We should now have a network connection so let's connect to Redis...
r = Redis(host = secrets.REDIS_HOST, port = secrets.REDIS_PORT)

if len(secrets.REDIS_PASSWORD) > 0:
    # Authenticate to Redis.
    r.auth(secrets.REDIS_PASSWORD)

while True:
    response = r.ping()
    print(response)
    time.sleep(2)