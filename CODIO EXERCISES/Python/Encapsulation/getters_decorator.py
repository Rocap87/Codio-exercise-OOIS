#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 12:35:21 2022

@author: robertocappiello
"""

class Person:
  def __init__(self, name):
    self._name = name
  
  @property
  def name(self):
    return self._name
  
c = Person("Calvin")
print(c.name)