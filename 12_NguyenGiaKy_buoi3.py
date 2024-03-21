# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.

#vd 1 S
class Rectangle: 
    def _init_(self , width , height):
        self.width = width 
        self.height = height 
    def getWidth(self) :
        return self.width
    def getHeigh(self): 
        return self.height
    def getArea(self): 
        return self.width *self.height

r1 = Rectangle(10 , 5)
r2 = Rectangle(20,11)
print("r1.width=" , r1.width)

#vd 2

class Car:
loaixe = "Ô tô"
def __init__(self, tenxe, mausac, nguyenlieu):
self.tenxe = tenxe
self.mausac = mausac
self.nguyenlieu = nguyenlieu
toyota = Car("Toyota", "Đỏ", "Điện")
lamborghini = Car("Lamborghini", "Vàng", "Deisel")
porsche = Car("Porsche", "Xanh", "Gas")
print("Porsche là {}.".format(porsche.__class__.loaixe))
print("Toyota là {}.".format(toyota.__class__.loaixe))
print("Lamborghini cũng là {}.".format(lamborghini.__class__.loaixe))

print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format( toyota.tenxe, toyota.mausac,
toyota.nguyenlieu))
print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format( lamborghini.tenxe,
lamborghini.mausac,lamborghini.nguyenlieu))
print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format( porsche.tenxe, porsche.mausac,
porsche.nguyenlieu))
""" 
#baitaptrenlop1 
import math import pi 
class hinhtron: 
    def init(self , banKinh ):
        self.banKinh = banKinh
       
    def chuVi(self):
        return 2*pi*self.banKinh 
    def dienTich(self): 
        pi*self.bankinh*self.banKinh
            












