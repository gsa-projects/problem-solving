from .units import *
from .utils import *
from tkinter import *
from time import sleep
from typing import Tuple
from abc import *

__all__ = ['Space', 'Object']

class Object(metaclass=ABCMeta):
	def __init__(self, pos: Quantity, mass: Quantity = 1 * kg, acc: Quantity = (0, 0) * m/s**2):
		if pos.unit != m or pos.is_scalar():
			raise UnitError("Position must be vector in m.")
		elif mass.unit != kg:
			raise UnitError("Mass must be in kg.")
		elif acc.unit != m/s**2:
			raise UnitError("Acceleration must be vector in m/s^2.")
		
		self.pos = pos
		self.last_pos = pos
		self.acc = acc
		self.mass = mass
		self.render_object = None
	
	@abstractmethod
	def attr(self, **kw):
		return self
	
	@abstractmethod
	def update(self, space: "Space"):
		return NotImplemented
	
	@abstractmethod
	def render(self, space: "Space"):
		return NotImplemented
	
	@abstractmethod
	def __repr__(self) -> str:
		return f"Object(pos={self.pos}, mass={self.mass})"
	
	def __str__(self):
		return self.__repr__()

# todo: x-y 축 방향 재설정
class Space:
	def __init__(self, size: Quantity, gravity: Quantity = (0, -0.1) * m / s ** 2, tps: int = 60, name: str = "Newtonian Space"):
		if size.unit != m or size.is_scalar():
			raise UnitError("Size must be vector in m.")
		elif gravity.unit != m/s**2 or gravity.is_scalar():
			raise UnitError("Gravity must be vector in m/s^2.")
		
		self.master = Tk(screenName=name)
		self.canvas = Canvas(master=self.master, width=size.x.value, height=size.y.value)
		self.size = size
		self.gravity = gravity
		self.tps = tps
		self.__layers = Arrays()
		
		self.master.geometry(f"{size.x.value}x{size.y.value}")
		self.canvas.pack()
	
	@property
	def width(self):
		return self.size.x
	
	@property
	def height(self):
		return self.size.y
	
	def tick(self):
		self.master.update()
		sleep(1 / self.tps)
	
	def is_destroyed(self):
		try:
			return not self.master.winfo_exists()
		except TclError:
			return True
		
	def create_line(self, pos_0: Quantity, pos_1: Quantity, *args, **kw) -> int:
		if not (pos_0.unit != m and pos_0.is_vector() and pos_1.unit == m and pos_1.is_vector()):
			raise UnitError("Position must be vector in m.")
		
		return self.canvas.create_line(pos_0.x.value, (self.height - pos_0.y).value, pos_1.x.value, (self.height - pos_1.y).value, *args, **kw)
	
	def create_rectangle(self, pos_0: Quantity, pos_1: Quantity, *args, **kw) -> int:
		if not (pos_0.unit == m and pos_0.is_vector() and pos_1.unit == m and pos_1.is_vector()):
			raise UnitError("Position must be vector in m.")
		
		return self.canvas.create_rectangle(pos_0.x.value, (self.height - pos_0.y).value, pos_1.x.value, (self.height - pos_1.y).value, *args, **kw)
	
	def create_oval(self, pos_0: Quantity, pos_1: Quantity, *args, **kw) -> int:
		if not (pos_0.unit == m and pos_0.is_vector() and pos_1.unit == m and pos_1.is_vector()):
			raise UnitError("Position must be vector in m.")
		
		return self.canvas.create_oval(pos_0.x.value, (self.height - pos_0.y).value, pos_1.x.value, (self.height - pos_1.y).value, *args, **kw)
	
	def create_text(self, pos: Quantity, *args, **kw) -> int:
		if not (pos.unit == m and pos.is_vector()):
			raise UnitError("Position must be vector in m.")
		
		return self.canvas.create_text(pos.x.value, (self.height - pos.y).value, *args, **kw)
	
	def create_polygon(self, pos_list: list[Quantity], *args, **kw) -> int:
		if not all((pos.unit == m and pos.is_vector()) for pos in pos_list):
			raise UnitError("Position must be vector in m.")
		
		return self.canvas.create_polygon(*((pos.x.value, (self.height - pos.y).value) for pos in pos_list), *args, **kw)
	
	def move(self, obj: Object, d_pos: Quantity):
		if not (d_pos.unit == m and d_pos.is_vector()):
			raise UnitError("Position must be vector in m.")
		
		self.canvas.move(obj.render_object, d_pos.x.value, -d_pos.y.value)
	
	def __enter__(self):
		return self.__layers
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		pass
	
	def __iadd__(self, objects: Object | Tuple):
		if isinstance(objects, Object):
			objects = (objects,)
		else:
			objects = tuple(objects)
		
		layer_idx = 0
		for i, obj in enumerate(objects):
			if isinstance(obj, Object):
				self.__layers[layer_idx] += obj
			else:
				if i > 0:
					layer_idx += 1
				self.__layers[layer_idx] += obj
				layer_idx += 1
		
		return self
	
	def __bool__(self):
		return not self.is_destroyed()

	def __iter__(self):
		for arr in self.__layers:
			for obj in arr:
				yield obj
	