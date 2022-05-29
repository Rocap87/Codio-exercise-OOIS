#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 13:43:05 2022

@author: robertocappiello
"""

class FinancialAccount:
  def __init__(self, amount):
    self.account = amount
    
  def __add__(self, other):
    return self.account + other.account
    
class BankAccount(FinancialAccount):
  pass

class InvestmentAccount(FinancialAccount):
  pass

my_banking = BankAccount(500)
my_investments = InvestmentAccount(750)
print(my_investments + my_banking)