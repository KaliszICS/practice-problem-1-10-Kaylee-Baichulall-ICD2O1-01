'''
    Lesson: Math Library
    Author: Kaylee Baichulall
    Date Created: October 2, 2024
    Date Last Modified: October 2, 2024
'''
import math

def q1(): 
  num = input("Input a number: ")
  num = float(num)
  print(math.sqrt(num))

def q2(): 
  num = input("Input a number: ")
  num = int(num)
  print(math.isqrt(num))

def q3(): 
  num = input("Input a number: ")
  num = float(num)
  print(math.floor(num))

def q4(): 
  num = input("Input a number: ")
  num = float(num)
  print(math.ceil(num))

def q5(): 
  num = input("Input a number: ")
  num = float(num)
  num2 = input("Input another number: ")
  num2 = float(num2)
  num3 = num * num2
  num3 = num3 / 2
  print(math.trunc(num3))

#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
q3()
q4()
q5()
