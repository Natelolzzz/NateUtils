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

def readLineStripped(path):
  with open(path, 'r') as file:
      content = file.readlines()
  return [line.strip() for line in content if line.strip().isdigit()]

def currentTime():
  now = datetime.now()
  return now.strftime("%H:%M:%S")

def rangeCheck(lower, upper, value):
  return int(lower) <= int(value) <= int(upper)
