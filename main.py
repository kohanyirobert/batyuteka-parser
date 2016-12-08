#!/usr/bin/env python3

import json
import os
import random
import signal
import string
import urllib.request
import batyu

from gi.repository import Gtk
from gi.repository import AppIndicator3
from gi.repository import Notify


APPINDICATOR_ID = 'batyuteka-appindicator'


def main():
  indicator = AppIndicator3.Indicator.new(
      APPINDICATOR_ID,
      os.path.abspath('batyuteka.svg'),
      AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
  indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)
  indicator.set_menu(menu_build())
  Notify.init(APPINDICATOR_ID)

  Gtk.main()


def menu_build():
  menu = Gtk.Menu()

  item_food = Gtk.MenuItem('Food')
  item_food.connect('activate', food_get)
  menu.append(item_food)

  item_quit = Gtk.MenuItem('Quit')
  item_quit.connect('activate', quit)
  menu.append(item_quit)

  menu.show_all()
  
  return menu


def food_get(source):
  foods = '\n'.join(batyu.get_menu(batyu.get_day_index()))
  
  Notify.Notification.new('<b>A wild Pokemon appeared</b>', 
              foods,
              None).show()


def quit(source):
  Notify.uninit()
  Gtk.main_quit()


if __name__ == '__main__':
  signal.signal(signal.SIGINT, signal.SIG_DFL)
  main()
