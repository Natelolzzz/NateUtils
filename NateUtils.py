from os import read
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

def multilinetolist(list):
  list = [y for y in (x.strip() for x in list.splitlines()) if y]
