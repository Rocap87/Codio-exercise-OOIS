#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 13:39:23 2022

@author: robertocappiello
"""

class TestClass:
  def sum(self, a = 0, b = 0, c = 0):
    if a != 0 and b != 0 and c != 0:
      return a + b + c
    elif a != 0 and b != 0:
      return a + b
    elif a != 0:
      return a
    else:
      return 0
    
obj = TestClass()
print(obj.sum(0, 2))