# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 19:18:13 2022

@author: User
"""

from tkinter import*
import random

root=Tk()
root.title("Picnic Bag List")
root.geometry("600x650")

list_items = Label(root)
random_numbers = Label(root)
items_for_picnic =["water_bottle", "Lunch_box", "Money", "Hankerchief", "Pen", "Diary", "Chips"]

list_items["text"] = "Listed Items : "+ str(items_for_picnic)

def random_item():
    random.sample(range(0,7),1)
    random_numbers ["text"] = "Put Item Number " + str(items_for_picnic)+ " In Bag"; 

btn=Button(root,text="Which Item To Take? ", command=randomlist)
btn.place(relx=0.5, rely=0.5, anchor = CENTER)

list_items.place(relx=0.5, rely=0.4, anchor = CENTER)
random_numbers.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainl
    