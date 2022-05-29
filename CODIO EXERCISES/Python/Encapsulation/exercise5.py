#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 13:26:03 2022

@author: robertocappiello
"""

class Cyclist:
  def __init__(self, name, nationality, nickname):
    self._name = name
    self._nationality = nationality
    self._nickname = nickname
    
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, new_value):
    self._name = new_value
    
  @property
  def nationality(self):
    return self._nationality
  
  @nationality.setter
  def nationality(self, new_value):
    self._nationality = new_value
    
  @property
  def nickname(self):
    return self._nickname
  
  @nickname.setter
  def nickname(self, new_value):
    self._nickname = new_value

my_cyclist = Cyclist("Greg LeMond", "American", "Le Montstre")

print(my_cyclist.name)
print(my_cyclist.nationality)
print(my_cyclist.nickname)
my_cyclist.name = "Eddy Merckx"
my_cyclist.nationality = "Belgian"
my_cyclist.nickname = "The Cannibal"
print(my_cyclist.name)
print(my_cyclist.nationality)
print(my_cyclist.nickname)