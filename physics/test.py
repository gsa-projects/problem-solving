import newtonian as nt
from newtonian.units import *
from os import *

px = 1 * m

class A:
	def __init__(self):
		global px
		px = m / 2

def p():
	global px
	px = m / 2

A()
print(px)
