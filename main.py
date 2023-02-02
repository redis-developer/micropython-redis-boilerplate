import network
import secrets
import sys
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
try:
    r = Redis(host = secrets.REDIS_HOST, port = secrets.REDIS_PORT)
except OSError as e:
    # Failed to connect to Redis, likely as it isn't listening at the 
    # host and port defined in secrets.py.  e looks like this:
    # [Errno 104] ECONNRESET
    print(f"Issue connecting to Redis at {secrets.REDIS_HOST}:{secrets.REDIS_PORT}")
    print(e)
    sys.exit(1)
    
# Authenticate to Redis if needed, optionally with username and/or password.
if len(secrets.REDIS_PASSWORD) > 0:
    if len(secrets.REDIS_USER) > 0:
        r.auth(secrets.REDIS_USER, secrets.REDIS_PASSWORD)
    else:
        r.auth(secrets.REDIS_PASSWORD)

while True:
    try:
        # Call the Redis PING command and output the response.
        # Replace with your application logic.
        # See https://redis.io/commands/ for details of each Redis command.
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