from turtle import * 

# Inital settings
window_width  = 2000
window_height = 1000
grid_x_step   = 100
grid_y_step   = 100
screensize(window_width, window_height)


# This function draws a line between the two given points
def draw_line(x1, y1, x2, y2, stroke_color, stroke_width):
    color(stroke_color)
    pensize(stroke_width )
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)

# This function draws the grid (cootdinate system)
def draw_grid():

    # Set the speed of the turtle
    speed(0)

    # Draw vertical lines 
    for x in range(-window_width // 2, window_width // 2 + 1, grid_x_step):
        draw_line(x, window_height // 2, x, -window_height // 2, "#d3d3d3", 1)

    # Draw horizontal lines
    for y in range(-window_height // 2, window_height // 2 + 1, grid_y_step):
        draw_line(-window_width // 2, y, window_width // 2, y, "#d3d3d3", 1)

    # Draw the X and Y axies
    draw_line(-window_width // 2, 0, window_width // 2, 0, "silver", 3)
    draw_line(0, window_height // 2, 0, -window_height // 2, "silver", 3)

# This function graphs functions 
def draw_function(fn, start_x, stop_x, step_x, graph_color):

    # Set the size and speed of the pencile
    pensize(7)
    speed(0)
    color(graph_color)


    # Go to the fist point to start drawing
    penup()
    goto(start_x, fn(start_x))
    pendown()

    # Loop through every single point and draw it 
    scale = 2
    for x in range(start_x, stop_x, step_x):
        goto(scale * x, scale * fn(x))



# --------------- FUNCTINOS -----------------
def func1(x):
    return .0001 * ((x + 300) ** 3) - 150

def func2(x):
    return .01 * (x ** 2)

def func3(x):
    return (.4 * (x - 200) ** 2) ** .5 - 200
# --------------------------------------------



# Draw the grid
draw_grid()

# Graph the functions
draw_function(func2, -300, 300, 2, "indianred")
draw_function(func1, -800, 300, 2, "palegreen")
draw_function(func3, -1000, 800, 10, "plum")

# Close the window on a click
exitonclick()