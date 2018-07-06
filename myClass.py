# _*_ coding:utf-8 _*_

class Rectangle:
    def __init__(self):
        self.width = 0
        self.hight = 0

    def setSize(self, size):
        self.hight, self.width = size

    def getSize(self):
        return self.width, self.hight