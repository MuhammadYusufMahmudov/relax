# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 21:06:42 2021

@author: MuhammadYusuf
"""
import turtle
turtle.bgcolor("black")
s=turtle.Turtle()


s.pensize(2)
s.speed(0)

c_list=('green','yellow','blue','violet','red','blue',
        'yellow','green','blue','red','violet','green','blue','red')
turtle.bgcolor('black')

a=0

while a<150:
    for i in c_list:
        s.color(i)
        s.forward(100+a*3)
        s.left(-90)
        a+=1




