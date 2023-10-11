from dataclasses import dataclass
from numpy import ndarray

class Vec[T]:
	x: T
	y: T
	
	def __init__(self, *args):
		if len(args) == 1 and isinstance(args[0], tuple | list | ndarray | Vec):
			self.x, self.y = args[0]
		else:
			self.x, self.y = args
	
	def __pos__(self):
		return self
	
	def __neg__(self):
		return Vec(-self.x, -self.y)
	
	def __add__(self, other: ndarray):
		if isinstance(other, Vec):
			return Vec(self.x + other.x, self.y + other.y)
		elif isinstance(other, ndarray):
			if not (other.ndim == 1 and len(other) == 2 and other.dtype == T):
				raise TypeError
			return Vec(self.x + other[0], self.y + other[1])
		elif isinstance(other, int | float):
			return Vec(self.x + other, self.y + other)
		else:
			return NotImplemented
	
	def __radd__(self, other):
		return self.__add__(other)
	
	def __sub__(self, other):
		return self.__add__(-other)
	
	def __rsub__(self, other):
		return -(self.__add__(-other))
	
	def __mul__(self, other):
		if isinstance(other, int | float):
			return Vec(self.x * other, self.y * other)
		else:
			return NotImplemented
	
	def __rmul__(self, other):
		return self.__mul__(other)
	
	def __truediv__(self, other):   # self / other
		return self.__mul__(1 / other)
	
	def __rtruediv__(self, other):  # other / self
		# return Vec(other / self.x, other / self.y)
		return 1 / self.__truediv__(other)
	
	def __iter__(self):
		yield self.x
		yield self.y
	
	def __repr__(self):
		return f"({self.x}, {self.y})"
	
	def __abs__(self):
		return (self.x ** 2 + self.y ** 2) ** 0.5
	
	__str__ = __repr__

@dataclass
class Dim:
	kg: float = 0.
	m: float = 0.
	s: float = 0.
	A: float = 0.
	K: float = 0.
	mol: float = 0.
	cd: float = 0.
	
	def __iter__(self):
		yield 'kg', self.kg
		yield 'm', self.m
		yield 's', self.s
		yield 'A', self.A
		yield 'K', self.K
		yield 'mol', self.mol
		yield 'cd', self.cd
		
	def __pos__(self):
		return self
	
	def __neg__(self):
		return Dim(
			-self.kg,
			-self.m,
			-self.s,
			-self.A,
			-self.K,
			-self.mol,
			-self.cd
		)
		
	def __add__(self, other):
		if isinstance(other, Dim):
			return Dim(
				self.kg + other.kg,
				self.m + other.m,
				self.s + other.s,
				self.A + other.A,
				self.K + other.K,
				self.mol + other.mol,
				self.cd + other.cd
			)
		else:
			return NotImplemented
		
	def __sub__(self, other):
		return self.__add__(-other)
	
	def __mul__(self, other):
		if isinstance(other, int | float):
			return Dim(
				self.kg * other,
				self.m * other,
				self.s * other,
				self.A * other,
				self.K * other,
				self.mol * other,
				self.cd * other
			)
		else:
			return NotImplemented
		
	def __eq__(self, other):
		if isinstance(other, Dim):
			return all(_s == _o for _s, _o in zip(self, other))
		else:
			return NotImplemented
	
class DimError(Exception):
	pass

class Unit:
	def __init__(self, value: float | Vec, dimension: Dim):
		self.value = value
		self.dimension = dimension
	
	def __repr__(self):
		return f"Unit(value={self.value}, dim={self.dimension})"
	
	def __str__(self):
		dot = '⋅'
		dimension_string = ["", ""]
		for name, power in self.dimension:
			if power == 0:
				continue
			elif abs(power) == 1:
				dimension_string[power < 0] += name + dot
			else:
				__str = str(int(abs(power)) if power.is_integer() else abs(power))
				dimension_string[power < 0] += name + '^' + __str + dot
		
		front, back = dimension_string
		front = front.strip(dot)
		back = back.strip(dot)
		
		return f"{self.value} {front}{"/" if back else ""}{back}".strip()
	
	def __pos__(self):
		return self
	
	def __neg__(self):
		return Unit(-self.value, self.dimension)
	
	def __add__(self, other):
		if isinstance(other, Unit):
			if self.dimension == other.dimension:
				return Unit(self.value + other.value, self.dimension)
			else:
				raise DimError
		else:
			return Unit(self.value + other, self.dimension)
	
	def __radd__(self, other):
		return self.__add__(other)
	
	def __sub__(self, other):
		return self.__add__(-other)
	
	def __rsub__(self, other):
		return -(self.__add__(-other))
	
	def __mul__(self, other):
		if isinstance(other, Unit):
			return Unit(self.value * other.value, self.dimension + other.dimension)
		elif isinstance(other, tuple):
			return Unit(self.value * Vec(other), self.dimension)
		else:
			return Unit(self.value * other, self.dimension)
	
	def __rmul__(self, other):
		return self.__mul__(other)
	
	def __truediv__(self, other):
		return self.__mul__(1 / other)
		
	def __rtruediv__(self, other):
		if isinstance(other, tuple):
			return Unit(Vec(other) / self.value, -self.dimension)
		else:
			return Unit(other / self.value, -self.dimension)
		
	def __pow__(self, other: int):
		if isinstance(other, int | float):
			return Unit(self.value ** other, self.dimension * other)
		else:
			return NotImplemented
		
	def __abs__(self):
		return Unit(abs(self.value), self.dimension)
	
	@property
	def unit(self):
		return Unit(1, self.dimension)

kg = Unit(1, Dim(kg=1))
m = Unit(1, Dim(m=1))
s = Unit(1, Dim(s=1))
A = Unit(1, Dim(A=1))
K = Unit(1, Dim(K=1))
mol = Unit(1, Dim(mol=1))
cd = Unit(1, Dim(cd=1))
rad = Unit(1, Dim())
