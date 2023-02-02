import network
import secrets
import time
from picoredis import Redis, RedisError

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)

while not wlan.isconnected() and wlan.status() >= 0:
    # If wifi configuration is incorrect, or the specified SSID can't be found
    # this will loop forever.  Consider adding logic to give up after a large
    # number of attempts...
    print("Connecting to wifi...")
    time.sleep(0.5)

# We should now have a network connection so let's connect to Redis...
r = Redis(host = secrets.REDIS_HOST, port = secrets.REDIS_PORT)

if len(secrets.REDIS_PASSWORD) > 0:
    # Authenticate to Redis, optionally with username.
    if len(secrets.REDIS_USER) > 0:
        r.auth(secrets.REDIS_USER, secrets.REDIS_PASSWORD)
    else:
        r.auth(secrets.REDIS_PASSWORD)

while True:
    try:
        response = r.ping()
        print(response)
    except RedisError as ex:
        # Some exception occurred, for example a NOPERM error
        # if using an ACL user that isn't allowed to run the 
        # command that was attempted.  Example output:
        #
        # ('NOPERM', "this user has no permissions to run the 'get' command")
        print(ex)

    time.sleep(2)