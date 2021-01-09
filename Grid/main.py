from turtle import *


def draw_grid(x, y, grid_w, grid_h, x_step, y_step, stroke_color):

	# Set color
	color(stroke_color)

	# Horizonrtal lines
	for row in range(0, grid_w + 1, y_step):
		penup()
		goto(x + 0, y + row)
		pendown()
		goto(x + grid_w, y + row)

	# Vertical lines
	for col in range(0, grid_h + 1, x_step):
		penup()
		goto(x + col, y + 0)
		pendown()
		goto(x + col, y + grid_h)s


draw_grid(100, 0, 100, 100, 50, 10, "lime")

exitonclick()