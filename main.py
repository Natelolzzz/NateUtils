import random
import sys
import time


def print_slow(string, typing_speed=300):
  string = str(string)
  string += "\n"
  for letter in string:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(random.random() * 10.0 / typing_speed)

def iseven(num):
  if num % 2:
      return false
  else:
      return true

def isodd(num):
  return not iseven(num)
