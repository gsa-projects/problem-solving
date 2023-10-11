from typing import List

class Array:
	def __init__(self, items: List = None):
		if items is None:
			self.__data: List = []
		elif isinstance(items, Array):
			self.__data = items.__data
		else:
			self.__data = items
	
	def __len__(self):
		return len(self.__data)
	
	def __del__(self):
		del self.__data
	
	def __add__(self, items) -> "Array":
		if isinstance(items, tuple | list):
			return Array(self.__data + list(items))
		else:
			return Array(self.__data + [items])
	
	def __sub__(self, items) -> "Array":
		if isinstance(items, tuple | list):
			items = list(items)
		else:
			items = [items]
		
		copied = self.__data.copy()
		for _e in items:
			copied.remove(_e)
		return Array(copied)
	
	def __repr__(self) -> str:
		return str(self.__data)
	
	__str__ = __repr__

class Arrays:
	def __init__(self):
		self.__data = []
	
	def __len__(self):
		return len(self.__data)
	
	def __del__(self):
		del self.__data
		
	def __delitem__(self, key):
		del self.__data[key]
	
	def __getitem__(self, idx):
		if idx == len(self):
			self.__data.append(Array())
		elif idx > len(self):
			raise IndexError("Index out of range.")
		
		return self.__data[idx]
	
	def __setitem__(self, key, value):
		if key == len(self):
			self.__data.append(Array())
		elif key > len(self):
			raise IndexError("Index out of range.")

		self.__data[key] = value
	
	def __repr__(self):
		if len(self) == 0:
			return '[]'
		
		__rs = '[\n'
		for _i in range(len(self)):
			__rs += f"\t{_i}: {self.__data[_i]}\n"
		__rs += ']'
		
		return __rs
	
	__str__ = __repr__

a = Arrays()
a[0] += 1, 2, 3, 4, 4, 4, 4, 4
a[1] += 4, 5, 6
a[2] += 7, 8, 9
print(a)

a[0] -= 4, 4, 4
print(a)

del a[1]
print(a)
