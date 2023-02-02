# Redis Boilerplate for MicroPython

A boilerplate [MicroPython](https://micropython.org/) script for getting started with Redis on microcontrollers (tested on [Raspberry Pi Pico W](https://www.raspberrypi.com/products/raspberry-pi-pico/)).

I'll add more details later!  For now, check out the comments in `main.py`.

This project uses (and contains a copy of) the [picoredis](https://github.com/SpotlightKid/picoredis) Redis client by [Christopher Arndt](https://github.com/SpotlightKid).  picoredis is made available under the terms of the MIT license which also apply to this repository.

There are many ways to get this project up and running on your microcontroller.  I've tested it using a Raspberry Pi Pico W and [VSCode](https://code.visualstudio.com/) with the [Pico W Go extension](https://marketplace.visualstudio.com/items?itemName=paulober.pico-w-go) running on macOS Ventura.  Note that you'll need the W version of the Raspberry Pi Pico to be able to connect to wifi and reach the Redis Server.

If you're not sure how to get the MicroPython runtime installed on your Pico W, check out Raspberry Pi's official guide [here](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html).

* If you find this useful, or have any questions... come chat with us in the `#internet-of-things` channel on the [Redis Discord server](https://discord.gg/redis).
* If you need a Redis server, sign up for a free fully-functional 30mb cloud instance of Redis Stack [here](https://redis.com/try-free/).
* Want to learn more about Redis?  Take a free course at [Redis University](https://university.redis.com).

Projects using picoredis on the Raspberry Pi Pico W:

* [Monitoring Redis Streams Consumer Group lag with LED display](https://github.com/simonprickett/redis-streams-lag-pi-pico-w)
* [Sending temperature / humidity / light readings to Redis and controlling a fan](https://github.com/simonprickett/raspberry-pi-pico-redis)
