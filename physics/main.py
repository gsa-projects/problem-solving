import newtonian as nt
from newtonian.units import *

space = nt.Space((1000, 700), gravity=(0, -9.8)*m/s**2).config(screen_icon='physics/icon.ico')

c1 = nt.Circle(pos=(100, 400)*m, vel=(20, 30)*m/s, acc=space.gravity).config(fill_color="YELLOW")
c2 = nt.Circle(pos=(200, 400)*m, vel=(0, 0)*m/s, acc=space.gravity).config(fill_color="RED")
c3 = nt.Circle(pos=(300, 400)*m, vel=(40, 20)*m/s, acc=space.gravity).config(fill_color="BLUE")
c4 = nt.Circle(pos=(400, 400)*m, vel=(10, 50)*m/s, acc=space.gravity).config(fill_color="GREEN")
c5 = nt.Circle(pos=(500, 400)*m, vel=(30, 10)*m/s, acc=space.gravity).config(fill_color="PURPLE")

space += c1, c2, c3, c4, c5

while space:
	for obj in space:
		obj.update(space)
	
	space.tick()
