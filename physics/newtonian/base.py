from .units import *
from .utils import *
from tkinter import *
from time import sleep
from typing import Tuple
from abc import *

__all__ = ['Space', 'Object']

class Object(metaclass=ABCMeta):
	def __init__(self, pos: Quantity, vel: Quantity = (0, 0)*m/s**2, acc: Quantity = (0, 0)*m/s**2, mass: Quantity = 1*kg):
		if pos.unit != m or pos.is_scalar():
			raise UnitError("Position must be vector in m.")
		elif vel.unit != m/s or vel.is_scalar():
			raise UnitError("Velocity must be vector in m/s.")
		elif acc.unit != m/s**2:
			raise UnitError("Acceleration must be vector in m/s^2.")
		elif mass.unit != kg:
			raise UnitError("Mass must be in kg.")
		
		self.pos = pos
		self.pos_0 = pos
		self.vel = vel
		self.acc = acc
		self.mass = mass
		self.render_object = None
	
	@abstractmethod
	def config(self):
		return self
	
	@abstractmethod
	def update(self, space: "Space"):
		self.render(space)
	
	@abstractmethod
	def render(self, space: "Space"):
		pass
	
	@abstractmethod
	def __repr__(self) -> str:
		return f"Object(pos={self.pos}, mass={self.mass})"
	
	def __str__(self):
		return self.__repr__()

px = 1 * m

class Space:
	def __init__(self, size: Tuple[int, int],
	             zoom: float = 1,
	             gravity: Quantity = (0, -9.80665)*m/s**2,
	             tps: Quantity = 60/s):
		if gravity.unit != m/s**2 or gravity.is_scalar():
			raise UnitError("Gravity must be vector in m/s^2.")
		
		"""
		zoom이 1이면 1m가 1px인 상황임
		zoom이 2면 1m가 2px인 상황임
		"""
		global px
		px = m / zoom
		
		self.size = size
		self.zoom = zoom
		self.gravity = gravity
		self.tps = tps
		
		self.__master = Tk()
		self.__canvas = Canvas(master=self.__master, width=self.size[0], height=self.size[1])
		self.__layers = Arrays()
		
		self.__master.geometry(f"{self.size[0]}x{self.size[1]}")
		self.__canvas.pack()
	
	def config(self, screen_name: str = 'Newtonian Space', screen_icon: str = None, bg_color: str = None):
		if screen_name is not None:
			self.__master.title(screen_name)
		if screen_icon is not None:
			self.__master.iconbitmap(screen_icon)
		if bg_color is not None:
			self.__canvas.config(bg=bg_color)
		
		return self
	
	@property
	def width(self) -> float:
		return self.size[0]
	
	@property
	def height(self) -> float:
		return self.size[1]
	
	def tick(self):
		self.__master.update()
		sleep((1 / self.tps) / s)
	
	def is_destroyed(self):
		try:
			return not self.__master.winfo_exists()
		except TclError:
			return True
		
	def create_line(self, pos_0: Quantity, pos_1: Quantity, *args, **kw) -> int:
		if not (pos_0.unit != m and pos_0.is_vector() and pos_1.unit == m and pos_1.is_vector()):
			raise UnitError("Position must be vector in m.")
		
		pos_0 /= px
		pos_1 /= px
		
		return self.__canvas.create_line(pos_0.x, self.height - pos_0.y, pos_1.x, self.height - pos_1.y.value, *args, **kw)
	
	def create_rectangle(self, pos_0: Quantity, pos_1: Quantity, *args, **kw) -> int:
		if not (pos_0.unit == m and pos_0.is_vector() and pos_1.unit == m and pos_1.is_vector()):
			raise UnitError("Position must be vector in m.")
		
		pos_0 /= px
		pos_1 /= px
		
		return self.__canvas.create_rectangle(pos_0.x, self.height - pos_0.y, pos_1.x, self.height - pos_1.y, *args, **kw)
	
	def create_oval(self, pos_0: Quantity, pos_1: Quantity, *args, **kw) -> int:
		if not (pos_0.unit == m and pos_0.is_vector() and pos_1.unit == m and pos_1.is_vector()):
			raise UnitError("Position must be vector in m.")
		
		pos_0 /= px
		pos_1 /= px
		
		return self.__canvas.create_oval(pos_0.x, self.height - pos_0.y, pos_1.x, self.height - pos_1.y, *args, **kw)
	
	def create_text(self, pos: Quantity, *args, **kw) -> int:
		if not (pos.unit == m and pos.is_vector()):
			raise UnitError("Position must be vector in m.")
		
		pos /= px
		
		return self.__canvas.create_text(pos.x, self.height - pos.y, *args, **kw)
	
	def create_polygon(self, pos_list: list[Quantity], *args, **kw) -> int:
		if not all((pos.unit == m and pos.is_vector()) for pos in pos_list):
			raise UnitError("Position must be vector in m.")
		
		pos_list = [pos / px for pos in pos_list]
		
		return self.__canvas.create_polygon(*((pos.x, self.height - pos.y) for pos in pos_list), *args, **kw)
	
	def move(self, obj: Object, d_pos: Quantity):
		if not (d_pos.unit == m and d_pos.is_vector()):
			raise UnitError("Position must be vector in m.")
		
		d_pos /= px
		
		self.__canvas.move(obj.render_object, d_pos.x, -d_pos.y)
	
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
