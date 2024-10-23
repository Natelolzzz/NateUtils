import random
import sys
import time
from sys import stdout

def print_slow(string, typing_speed=300):
  string = str(string)
  string += "\n"
  for letter in string:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(random.random() * 10.0 / typing_speed)

def iseven(num):
  if num % 2:
      return False
  else:
      return True

def isodd(num):
  return not iseven(num)

def correct(num):
  if num < 0:
    num = 0
  return num

def EraseLast():
  for i in range(1,20):
      stdout.write("\r%d" % i)
      stdout.flush()
      time.sleep(1)
  stdout.write("\n")
