#!/usr/bin/python3

import argparse
import subprocess

def get_max_brightness():
   with open('/sys/class/backlight/intel_backlight/max_brightness', "r") as infile:
      return int(infile.readline().strip())

def get_current_brightness():
   with open('/sys/class/backlight/intel_backlight/actual_brightness', "r") as infile:
      return int(infile.readline().strip())

""" Preferably use set_relative_brightness"""
def set_brightness(i):
   with open('/sys/class/backlight/intel_backlight/brightness', "w") as outfile:
      subprocess.call(["echo",str(i)], stdout=outfile)

def get_current_relative_brightness():
   curr_b = get_current_brightness()
   max_b  = get_max_brightness()
   return int(100 * curr_b/max_b)

def set_relative_brightness(i):
   b = int(get_max_brightness() * i / 100)
   with open('/sys/class/backlight/intel_backlight/brightness', "w") as outfile:
      subprocess.call(["echo",str(b)], stdout=outfile)

def main():
   parser = argparse.ArgumentParser()
   parser.add_argument("-get", action="store_true")
   parser.add_argument("-set", type=int)
   parser.add_argument("-inc", type=int)
   parser.add_argument("-dec", type=int)
   args = parser.parse_args()
   if args.get:
      print(get_current_relative_brightness())
      exit()
   elif args.set:
      val=args.set
      set_relative_brightness(val)
      exit()
   elif args.inc:
      db = args.inc
      new_b = get_current_relative_brightness() + db
   elif args.dec:
      db = args.dec
      new_b = get_current_relative_brightness() - db
   if (new_b<=0):
      new_b=1
   elif new_b>100:
      new_b=100
   elif (new_b==11):
      new_b=10
   set_relative_brightness(new_b)

if __name__ == "__main__":
   main()

