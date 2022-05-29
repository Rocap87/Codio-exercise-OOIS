#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 12:37:31 2022

@author: robertocappiello
"""

class Person:
  def __init__(self, name, age):
    self._name = name
    self._age = age
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, new_name):
    self._name = new_name
    
  @property
  def age(self):
    return self._age
  
  @age.setter
  def age(self, new_age):
    self._age = new_age
  
c = Person("Calvin", "6")
print(c.name)
print(c.age)
c.age = -17
c.name = False
print(c.name)
print(c.age)