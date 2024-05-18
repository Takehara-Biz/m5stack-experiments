import os, sys, io
import M5
from M5 import *



title0 = None
label0 = None


def setup():
  global title0, label0

  M5.begin()
  Widgets.fillScreen(0xe1c3c3)
  title0 = Widgets.Title("Takehara", 3, 0xffffff, 0x0000FF, Widgets.FONTS.DejaVu18)
  label0 = Widgets.Label("Hello World!!!!", 90, 170, 1.0, 0xffffff, 0x222222, Widgets.FONTS.DejaVu18)



def loop():
  global title0, label0
  M5.update()


if __name__ == '__main__':
  try:
    setup()
    while True:
      loop()
  except (Exception, KeyboardInterrupt) as e:
    try:
      from utility import print_error_msg
      print_error_msg(e)
    except ImportError:
      print("please update to latest firmware")
