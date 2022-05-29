#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 13:37:26 2022

@author: robertocappiello
"""

class Alpha:
  def show(self):
    print("I am from class Alpha")
  
  def hello(self):
    print("Hello from Alpha")
    
class Bravo(Alpha):
  def show(self):
    print("I am from class Bravo")
  
  def hello(self):
    print("Hello from Bravo")
    
test_object = Alpha()
test_object.hello()
test_object = Bravo()
test_object.hello()