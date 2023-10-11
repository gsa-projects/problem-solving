import tkinter as tk
import numpy as np
from dataclasses import dataclass
import time

fps = 60.0

# space = nt.Space(size=(1000, 600), gravity=nt.Vec(0., 0.05))

window = tk.Tk()
window.geometry('700x500')
canvas = tk.Canvas(width=700, height=500, master=window)
canvas.pack()

# circle = nt.Circle((100, 50), 30, fill_color='skyblue', outline_color='yellow', width=3)
# circle2 = nt.Circle((110, 60), 20, fill_color='green', outline_color='lime', width=2)
circle = canvas.create_oval(70, 20, 130, 80, fill='skyblue', outline='yellow', width=3)

# with space.into() as objects:
# 	objects += circle, circle2

def do():
	x1, y1, x2, y2 = canvas.coords(circle)
	canvas.coords(circle, x1, y1 + 3, x2, y2 + 3)
	print(canvas.coords(circle))
	
	# canvas.after(10, do)

try:
	while True:
		# if not window.winfo_exists():
		# 	break

		do()
		window.update()
		time.sleep(1 / fps)
except tk.TclError:
	print('Closed')

# while not space.destroy():
# 	space.update()
# 	space.step(sub=4)
