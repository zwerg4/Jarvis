from itertools import cycle
import os
import sys
import time

from flux_led import BulbScanner, WifiLedBulb


def crossFade(bulb, color1, color2):

    r1, g1, b1 = color1
    r2, g2, b2 = color2

    steps = 100
    for i in range(1, steps + 1):
        r = r1 - int(i * float(r1 - r2) / steps)
        g = g1 - int(i * float(g1 - g2) / steps)
        b = b1 - int(i * float(b1 - b2) / steps)
        # (use non-persistent mode to help preserve flash)
        bulb.setRgb(r, g, b, persist=False)

#MAIN     
bulb = WifiLedBulb('192.168.0.240')

color_time = 5  # seconds on each color

red = (255, 0, 0)
orange = (255, 125, 0)
yellow = (255, 255, 0)
springgreen = (125, 255, 0)
green = (0, 255, 0)
turquoise = (0, 255, 125)
cyan = (0, 255, 255)
ocean = (0, 125, 255)
blue = (0, 0, 255)
violet = (125, 0, 255)
magenta = (255, 0, 255)
raspberry = (255, 0, 125)
colorwheel = [
  red,
  orange,
  yellow,
  springgreen,
  green,
  turquoise,
  cyan,
  ocean,
  blue,
  violet,
  magenta,
  raspberry,
]

# use cycle() to treat the list in a circular fashion
colorpool = cycle(colorwheel)

# get the first color before the loop
color = next(colorpool)

while True:
  bulb.refreshState()

  # set to color and wait
  # (use non-persistent mode to help preserve flash)
  bulb.setRgb(*color, persist=False)
  time.sleep(color_time)

  # fade from color to next color
  next_color = next(colorpool)
  crossFade(bulb, color, next_color)

  # ready for next loop
  color = next_color