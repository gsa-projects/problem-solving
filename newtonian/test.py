import newtonian as nt
from newtonian.units import *

space = nt.Space((1000, 600)*m)

c1 = nt.Circle((50, 50)*m, 30*kg, 10*m)
c2 = nt.Circle((110, 60)*m, 20*kg, 20*m)
c3 = nt.Circle((130, 90)*m, 10*kg, 30*m)

with space.set_object() as layers:
	layers[0] += circle, circle2
	layers[1] += circle3
	layers[2] += circle4, circle5

space.layers[0] += c1, c2
space.layers[1] += c

# space += (circle, circle2), circle3, (circle4, circle5)

space += c1, c2, c3

while space:
	for shape in space:
		shape.update()
		
	space.tick()
