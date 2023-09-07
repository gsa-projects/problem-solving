def get_weekday(current_weekday: int, days_ahead: int) -> int:
	"""current_weekday에서 부터 days_ahead만큼 지났을 때의 요일을 반환합니다.
	>>> get_weekday(7, 1)
	1
	>>> get_weekday(3, 1)
	4
	"""
	
	return (current_weekday - 1 + days_ahead) % 7 + 1


def days_difference(day1: int, day2: int) -> int:
	"""day1과 day2 사이의 일수 반환

	>>> days_difference(2000, 2000)
	0
	>>> days_difference(2000, 2001)
	1
	>>> days_difference(2000, 1999)
	-1
	"""
	
	return day2 - day1


def get_birthday_weekday(current_weekday: int, current_day: int, birthday_day: int) -> int:
	"""
	>>> get_birthday_weekday(5, 3, 4)
	6
	>>> get_birthday_weekday(5, 3, 116)
	6
	>>> get_birthday_weekday(6, 116, 3)
	5
	"""
	
	diff = days_difference(current_day, birthday_day)
	return get_weekday(current_weekday, diff)


print(get_birthday_weekday(5, 3, 117))
