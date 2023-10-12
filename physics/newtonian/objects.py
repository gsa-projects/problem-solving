from .base import Object, Space
from .utils import VecLike
from .units import *

__all__ = ['Circle']

class Circle(Object):
	def __init__(self, pos: Quantity, vel: Quantity = (0, 0) * m/s, acc: Quantity = (0, 0) * m/s**2, mass: Quantity = 1 * kg, radius: Quantity = 10 * m):
		super().__init__(pos, vel, acc, mass)
		
		if mass.unit != kg or mass.is_vector():
			raise UnitError("Mass must be scalar in kg.")
		elif radius.unit != m or radius.is_vector():
			raise UnitError("Radius must be scalar in m.")
		
		self.radius = radius
		
		self.width = 1
		self.outline_color = 'black'
		self.fill_color = 'white'

	def config(self, width=None, outline_color=None, fill_color=None):
		if width is not None:
			self.width = width
		if outline_color is not None:
			self.outline_color = outline_color
		if fill_color is not None:
			self.fill_color = fill_color
		
		return self
	
	def update(self, space: "Space"):
		self.render(space)
		
		v_0 = self.vel
		x_0 = self.pos
		a = self.acc
		dt = 1 / (space.tps / 10)
		
		self.vel = v_0 + a*dt
		self.pos_0 = self.pos
		self.pos = x_0 + v_0*dt + a*dt**2/2
	
	def render(self, space: "Space"):
		if self.render_object is None:
			p0, p1 = self.pos - self.radius, self.pos + self.radius
			self.render_object = space.create_oval(p0, p1, fill=self.fill_color, outline=self.outline_color, width=self.width)
		
		space.move(self, self.pos - self.pos_0)
	
	def __repr__(self):
		return f"Circle(pos={self.pos}, radius={self.radius}, mass={self.mass})"
