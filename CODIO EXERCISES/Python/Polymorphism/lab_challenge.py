#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 14:03:21 2022

@author: robertocappiello
"""

class Chef:
  def __init__(self, name, cuisine, stars):
    self.name = name
    self.cuisine = cuisine
    self.michelin_stars = stars
    
  def __gt__(self, other_chef):
    return self.michelin_stars > other_chef.michelin_stars
    
  def compare(self, other_chef):
    if self > other_chef:
      return f'{self.name} has more Michelin stars than {other_chef.name}'
    else:
      return f'{other_chef.name} has more Michelin stars than {self.name}'

marco = Chef('Marco Pierre White', 'French, British', 3)
rene = Chef('Rene Redzepi', 'Nordic', 2)

marco.compare(rene)