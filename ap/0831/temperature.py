def to_celsius(fahrenheit: float) -> float:
	return (fahrenheit - 32.0) * 5 / 9

def above_freezing(celsius: float) -> bool:
	return celsius > 0
