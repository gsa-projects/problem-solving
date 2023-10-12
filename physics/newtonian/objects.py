from .base import Object, Space
from .utils import VecLike
from .units import *

__all__ = ['Circle']

class Circle(Object):
	def __init__(self, pos: Quantity, radius: Quantity = 10 * m, mass: Quantity = 1 * kg, acc: Quantity = (0, 0) * m/s**2):
		super().__init__(pos, mass, acc)
		self.radius = radius
		
		self.width = 1
		self.outline_color = 'black'
		self.fill_color = 'white'

	def attr(self, **kw):
		if 'width' in kw:
			self.width = kw['width']
		if 'outline_color' in kw:
			self.outline_color = kw['outline_color']
		if 'fill_color' in kw:
			self.fill_color = kw['fill_color']
		
		return self
	
	def update(self, space: "Space"):
		"""
		Verlet Integration

		x_(i+2) = 2x_(i+1) - x_i + a_i * dt^2
		"""
		# self.acc = space.gravity
		
		x = [self.last_pos, self.pos]
		a = self.acc
		dt = 1 * s
		
		self.pos = 2 * x[1] - x[0] + a * dt**2
		self.last_pos = x[1]
		
		return self
	
	def render(self, space: "Space"):
		if self.render_object is None:
			p0, p1 = self.pos - self.radius, self.pos + self.radius
			self.render_object = space.create_oval(p0, p1, fill=self.fill_color, outline=self.outline_color, width=self.width)
		
		space.move(self, self.pos - self.last_pos)
	
	def __repr__(self):
		return f"Circle(pos={self.pos}, radius={self.radius}, mass={self.mass})"
