import random
import sys
import time
from sys import stdout
from datetime import datetime

def printSlow(string, typing_speed=300):
  string = str(string)
  string += "\n"
  for letter in string:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(random.random() * 10.0 / typing_speed)

def isEven(num):
  if num % 2:
      return False
  else:
      return True

def isOdd(num):
  return not iseven(num)

def clamp(num, lowest=0):
  if num < lowest:
    num = 0
  return num

def readLine(path, line):
  file = open(path) 
  content = file.readlines() 
  return content[line-1]

def readLines(path, lines):
  content = ""
  if len(lines) > 0:
    line = lines.pop()
    content += readline(path, line)
    content += "\n"
  return content

def currentTime():
  now = datetime.now()
  return now.strftime("%H:%M:%S")

def rangeCheck(lower, upper, value):
  try:
    return float(lower) <= float(value) <= float(upper)
  except:
    return False
