# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 17:37:30 2019

@author: ValentinePit
"""
import kivy

from kivy.app import App
from kivy.uix.lable import Lable

class MyApp(App):
    
    
    def build(self):
        return Label(text = "Hello, World")

if __name__ == '__main__':
    MyApp().run()
   
