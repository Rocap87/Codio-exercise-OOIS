#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 12:31:51 2022

@author: robertocappiello
"""

class PrivateClass:
  def __init__(self):
    self.__private_attribute = "I am a private attribute"
    
  def __private_method(self):
    return "I am a private method"
  
  def helper_method(self):
    return self.__private_method()
    
obj = PrivateClass()
print(obj.helper_method())