from shapes import *


def draw_smile():

  # Draw head
  draw_circle(0, 0, 210, "black", "lime", 5)

  # Draw mouth
  draw_circle(0, 0, 120, "black", "lime", 5)
  draw_rectangle(-150, -30, 300, 170, "lime", "lime", 5)
  draw_triangle(-60, 140, 60, 140, 0, 180, "lime", "lime", 1)

  # Draw right eye
  draw_circle(100, 80, 40, "black", "white", 5)
  draw_circle(120, 80, 15, "black", "black", 5)

  # Draw left eye
  draw_circle(-100, 80, 40, "black", "white", 5)
  draw_circle(-80, 80, 15, "black", "black", 5)


