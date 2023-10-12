import newtonian as nt
import newtonian.units as _

space = nt.Space((1000, 600)*_.m, tps=1000, gravity=(0, -0.01)*_.m/_.s**2)

c1 = nt.Circle((50, 50)*_.m, 10*_.m, 30*_.kg, acc=space.gravity).attr(fill_color='red', width=5)
c2 = nt.Circle((250, 260)*_.m, 20*_.m, 20*_.kg, acc=space.gravity).attr(fill_color='blue', width=3)
c3 = nt.Circle((450, 390)*_.m, 30*_.m, 10*_.kg, acc=space.gravity).attr(fill_color='green', width=7)
c4 = nt.Circle((650, 520)*_.m, 40*_.m, 10*_.kg, acc=space.gravity).attr(fill_color='yellow', width=10)
c5 = nt.Circle((850, 750)*_.m, 50*_.m, 10*_.kg, acc=space.gravity).attr(fill_color='purple', width=15)

with space as layers:
	layers[0] += c1, c2
	layers[1] += c3
	layers[2] += c4, c5

while space:
	for obj in space:
		obj.render(space)
		obj.update(space)

	space.tick()
