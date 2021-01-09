from turtle import *      

from tools import *       # Settings
from smile import *       # Drawing


def main():
  # Set turtle speed and hide it
  setup_turtle()

  # Draw smile 
  draw_smile()

  # Close window when user clicks on it
  close_window_on_click()


main()