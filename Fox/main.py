
from turtle import *

# Position
x = -150
y = -100

# Scale factor
scale = 5

# Hide turtle
ht()

# This function draws triangles with given 3 points
def draw_polygon_3(x1, y1, x2, y2, x3, y3, stroke_color, fill_color, stroke_width):
  color(stroke_color, fill_color)
  pensize(stroke_width)
  begin_fill()
  penup()
  goto(scale * (x1 + x), -1 * scale * (y1 + y))
  pendown()
  goto(scale * (x2 + x), -1 * scale * (y2 + y))
  goto(scale * (x3 + x), -1 * scale * (y3 + y))
  goto(scale * (x1 + x), -1 * scale * (y1 + y))
  end_fill()    

# This function draws a polygon with given 4 points
def draw_polygon_4(x1, y1, x2, y2, x3, y3, x4, y4, stroke_color, fill_color, stroke_width):
  color(stroke_color, fill_color)
  pensize(stroke_width)
  begin_fill()
  penup()
  goto(scale * (x1 + x), -1 * scale * (y1 + y))
  pendown()
  goto(scale * (x2 + x), -1 * scale * (y2 + y))
  goto(scale * (x3 + x), -1 * scale * (y3 + y))
  goto(scale * (x4 + x), -1 * scale * (y4 + y))
  goto(scale * (x1 + x), -1 * scale * (y1 + y))
  end_fill()    

# This function draws a polygon with given 8 points
def draw_polygon_7(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, stroke_color, fill_color, stroke_width):
  color(stroke_color, fill_color)
  pensize(stroke_width)
  begin_fill()
  penup()
  goto(scale * (x1 + x), -1 * scale * (y1 + y))
  pendown()
  goto(scale * (x2 + x), -1 * scale * (y2 + y))
  goto(scale * (x3 + x), -1 * scale * (y3 + y))
  goto(scale * (x4 + x), -1 * scale * (y4 + y))
  goto(scale * (x5 + x), -1 * scale * (y5 + y))
  goto(scale * (x6 + x), -1 * scale * (y6 + y))
  goto(scale * (x7 + x), -1 * scale * (y7 + y))
  goto(scale * (x1 + x), -1 * scale * (y1 + y))
  end_fill() 


# Head
draw_polygon_3(128,142,172,135,134,134, "orange", "orange", 1)
draw_polygon_3(81,141,128,142,107,148, "#E7E7E7", "#E7E7E7", 1) 
draw_polygon_3(106,148,131,170,128,142, "#E7E7E7", "#E7E7E7", 1) 
draw_polygon_7(82,142,128,142,134,135,118,122,99,116,104,124,93,135, "orange", "orange", 1) 

# Back
draw_polygon_3(131,170,172,135,128,142, "orange", "orange", 1) 
draw_polygon_3(173,134,196,155,131,170, "orange", "orange", 1) 
draw_polygon_3(196,155,221,125,173,134, "orange", "orange", 1)
draw_polygon_3(196,155,218,163,221,125, "orange", "orange", 1) 
draw_polygon_3(221,125,239,155,218,163, "orange", "orange", 1)

# Tail
draw_polygon_3(221,125,260,152,256,125, "orange", "orange", 1)
draw_polygon_4(256,125,298,139,300,156,260,152, "orange", "orange", 1) 
draw_polygon_3(298,139,299,156,317,135, "orange", "orange", 1) 
draw_polygon_4(298,139,282,108,311,119,317,136, "orange", "orange", 1)
draw_polygon_3(304,116,313,101,282,107, "#E7E7E7", "#E7E7E7", 1) 

# First Leg
draw_polygon_3(131,170,111,183,196,155, "orange", "orange", 1) 
draw_polygon_3(112,183,118,186,144,172, "orange", "orange", 1) 
draw_polygon_3(111,183,99,196,118,186, "black", "black", 1) 

# Second Leg
draw_polygon_3(155,169,174,186,171,163, "orange", "orange", 1) 
draw_polygon_3(164,177,169,198,174,187, "black", "black", 1) 

# Third Leg
draw_polygon_3(196,155,211,188,214,162, "orange", "orange", 1) 
draw_polygon_3(207,180,199,197,211,189, "black", "black", 1) 

# Fourth Leg
draw_polygon_3(218,163,252,176,239,155, "orange", "orange", 1) 
draw_polygon_3(252,176,258,169,239,155, "orange", "orange", 1) 
draw_polygon_3(252,176,259,196,258,170, "black", "black", 1) 

# Close window when user clicks on it
exitonclick()
