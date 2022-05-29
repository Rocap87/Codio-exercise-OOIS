#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 12:39:18 2022

@author: robertocappiello
"""

class Person:
  def __init__(self, name):
    self._name = name
  
  def get_name(self):
    return self._name
  
  def set_name(self, new_name):
    self._name = new_name
  
  name = property(get_name, set_name)
  
c = Person("Calvin")
print(c.name)
c.name = "Hobbes"
print(c.name)