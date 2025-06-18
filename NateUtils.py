import random
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
  if toIntSafe(num) % 2:
      return False
  else:
      return True

def isOdd(num): # :)
  return not(iseven(num))

def average(list): # Commonly used, very handy
  toRemove = []
  for i in range(0,len(list)): 
      list[i] = toFloatSafe(list[i],"False")
  try:
    list.remove("False")
    return sum(list) / len(list) 
  except:
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
    return toFloatSafe(lower) <= toFloatSafe(value) <= toFloatSafe(upper)
  except:
    return False

def clamp(num, lowest=0): # Basically just another input validation thing
  if toIntSafe(num) < toIntSafe(lowest):
    num = toIntSafe(lowest)
  return num

def toIntSafe(num,returnval=0): # Duo of automatic safety converts, so shouldnt throw errors on incorrect input. Just check if = to 0, ask for new input or handle otherwise
  try:
    return int(num)
  except:
    return returnval

def toFloatSafe(num,returnval=0):
  try:
    return float(num)
  except:
    return returnval
