#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 29 13:56:34 2022

@author: robertocappiello
"""

class Contacts:
  def __init__(self):
    self.view = 'list'
    self.contact_list = []
    self.choice = None
    self.index = None

  def display(self):
    while True:
      if self.view == 'list':
        self.show_list()
      elif self.view == 'info':
        self.show_info()
      elif self.view == 'add':
        print()
        self.add_contact()
      elif self.view == 'quit':
        print('\nClosing the contact list...\n')
        break
    
  def show_list(self):
    print()
    if len(self.contact_list) == 0:
        self.choice = input('(A)dd a new contact \n(Q)uit \n> ').lower()
    else:
        self.view = 'quit'
    self.handle_choice()

  def show_info(self):
    pass

  def __add__(self, new_contact):
    self.contact_list.append(new_contact)

  def add_contact(self):
    self + Information()
    self.view = 'list'

  def handle_choice(self):
      if self.choice == 'q':
          self.view = 'quit'
      elif self.choice == 'a' and self.view == 'list':
          self.view = 'add'  
  
class Information:
    def __init__(self):
        self.first_name = input('Enter first name: ')
        self.last_name = input('Enter last name: ')
        self.personal_phone = input('Enter personal phone number: ')
        self.personal_email = input('Enter personal email address: ')
        self.work_phone = input('Enter work phone number: ')
        self.work_email = input('Enter work email address: ')
        self.title = input('Enter work title: ')

contacts = Contacts()
contacts.display()
print(len(contacts.contact_list))