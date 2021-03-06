# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 17:55:28 2022

@author: steve
"""

import random


class Character():
    def __init__(self):
        self.__LEVEL=1
        self.__HP=10
        self.__MP=5
        self.__ATK=3
        self.__DEF=2
        self.__NAME=""
        self.__EXP=0
    
    def show_status(self):
        print(f"Your name is {self.__NAME}\nLV:{self.__LEVEL}\nHP:{self.__HP}\nMP:{self.__MP}")
        print(f"ATK:{self.__ATK}\nDEF:{self.__DEF}\nEXP:{self.__EXP}")

    def get_EXP(self,gain):
        self.__EXP+=gain
        self.check_Level()
    
    def check_Level(self):
        if(self.__EXP>self.__LEVEL**2):
            self.__EXP=0
            self.__LEVEL+=1
            self.Level_up()
            
    def Level_up(self):
        self.__HP+=self.__LEVEL
        self.__MP+=3
        self.__ATK+=2
        self.__DEF+=self.__LEVEL%2
    
    def change_name(self,name):
        self.__NAME=name
        
class Player(Character):
    def set_name(self,name):
        self.change_name(name)

class monster(Character):
    def set_name(self,name):
        self.change_name(name)
        
    def set_monster(self,key=None):
        self.set_name("test")
        if key:
            print("still work")
        