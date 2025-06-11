import random
import sys
import time
from sys import stdout
from datetime import datetime

# Generic Utils
def printSlow(string, typing_speed=300): # A horrific crime, which I am only putting here since I seem to use it in every project. Stolen off stackoverflow and bent to my whims shamelessly
  string = str(string)
  string += "\n"
  for letter in string:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(random.random() * 10.0 / typing_speed)

def currentTime(): # Kinda handy, use it sometimes
  now = datetime.now()
  return now.strftime("%H:%M:%S")

# Maths Utils
def isEven(num): # You'd be surprised how much I use this
  if num % 2:
      return False
  else:
      return True

def isOdd(num): # :)
  return not(iseven(num))

def average(list): # Commonly used, very handy
    return sum(list) / len(list) 

# File Utils
def readLine(path, line): # self explanatory
  file = open(path) 
  content = file.readlines() 
  return content[line-1]

def readLines(path, lines): # self explanatory
  content = ""
  if len(lines) > 0:
    line = lines.pop()
    content += readline(path, line)
    content += "\n"
  return content

# Validation Utils
def rangeCheck(lower, upper, value): # Check if an integer is inbetween two other integers
  try:
    return float(lower) <= float(value) <= float(upper)
  except:
    return False

def clamp(num, lowest=0): # Basically just another input validation thing
  if num < lowest:
    num = lowest
  return num
