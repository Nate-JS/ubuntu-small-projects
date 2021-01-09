from turtle import *


def draw_circle(x, y, radius, stroke_color, fill_color, stroke_width):
    color(stroke_color, fill_color)
    pensize(stroke_width)
    begin_fill()
    penup()
    goto(x, y - radius)
    pendown()
    circle(radius)
    end_fill()


def draw_triangle(x1, y1, x2, y2, x3, y3, stroke_color, fill_color, stroke_width):
    color(stroke_color, fill_color)
    pensize(stroke_width)
    begin_fill()
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)
    goto(x3, y3)
    goto(x1, y1)
    end_fill()


def draw_rectangle(x, y, width, height, stroke_color, fill_color, stroke_width):
    color(stroke_color, fill_color)
    pensize(stroke_width)
    begin_fill()
    penup()
    goto(x, y)
    pendown()
    goto(x + width, y)
    goto(x + width, y + height)
    goto(x, y + height)
    goto(x, y)
    end_fill()


def draw_line(x1, y1, x2, y2, stroke_color, stroke_width):
    color(stroke_color)
    pensize(stroke_width )
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)

