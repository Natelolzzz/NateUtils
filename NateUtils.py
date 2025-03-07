import random
import sys
import time
import os
from sys import stdout
from datetime import datetime

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

def eraseLast():
  for i in range(1,20):
      stdout.write("\r%d" % i)
      stdout.flush()
      time.sleep(1)
  stdout.write("\n")

def readline(path, line):
  file = open(path) 
  content = file.readlines() 
  return content[line-1]

def readlines(path, lines):
  content = ""
  if len(lines) > 0:
    line = lines.pop()
    content += readline(path, line)
    content += "\n"
  return content

def readlinestripped(path):
  with open(path, 'r') as file:
      content = file.readlines()
  return [line.strip() for line in content if line.strip().isdigit()]

def multilinetolist():
  return [y for y in (x.strip() for x in list.splitlines()) if y]

def clear_screen():
  if os.name == 'nt':
    _ = os.system('cls')
  else:
    _ = os.system('clear')

def current_time():
  now = datetime.now()
  return now.strftime("%H:%M:%S")
