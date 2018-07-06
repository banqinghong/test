# _*_ coding:utf-8 _*_
from myClass import Rectangle
import re
from ConfigParser import ConfigParser

#CONFIGFILE = 'config.properties'
config = ConfigParser()
config.read('config.properties')


c = Rectangle()
c.hight = int(config.get('size','thehight'))
c.width = int(config.get('size','thewidth'))
print c.getSize()

my_text = 'alpha,beta,,,,gamma delta'
print re.split('[, ]+', my_text)