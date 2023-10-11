from .units import Unit, Vec, kg, DimError
from .utils import Arrays

from typing import Tuple, List, TypeAlias
from tkinter import *
from numpy import ndarray
from time import sleep

VecLike: TypeAlias = Vec | Tuple[int, int] | List[int, int] | ndarray

class Object:
	def __init__(self, pos: VecLike, mass: Unit, render: bool = True):
		if mass.dimension != kg:
			raise DimError("Mass must be in kg.")
		
		self.pos = Vec(pos)
		self.mass = mass
		self.render = render
	
	def attr(self, **kw):
		return self
	
	def __call__(self):
		return NotImplemented

class Circle(Object):
	def __init__(self, pos: VecLike, mass: Unit, radius: int, render: bool = True):
		super().__init__(pos, mass, render)
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

# todo: x-y 축 방향 재설정
class Space:
	def __init__(self, size: VecLike,
	             tps: int = 60,
	             gravity: VecLike = Vec(0, 0.03),
	             name: str = "Newtonian Space"):
		self.master = Tk(screenName=name)
		self.canvas = Canvas(master=self.master, width=size[0], height=size[1])
		self.size = size
		self.tps = tps
		self.gravity = Vec(gravity)
		self.layers = Arrays()
		
		self.master.geometry(f"{size[0]}x{size[1]}")
		self.canvas.pack()
	
	@property
	def width(self):
		return self.size[0]
	
	@property
	def height(self):
		return self.size[1]
	
	def tick(self):
		self.master.update()
		sleep(1 / self.tps)
	
	def __enter__(self):
		...
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		...
	
	def __add__(self, other: Object | tuple[Object, ...] | list[Object, ...]):
		if isinstance(other, Object):
			self.shapes.append(other)
		else:
			self.shapes.extend(other)

	def __bool__(self):
		return self.master.winfo_exists()
	