'''
Homework 5 - Problem 3:
See HW5 PDF for specifics
'''

# Checked with Matt Pozsgai

from abc import ABCMeta, abstractmethod
from math import sqrt
import tkinter as tk


class Drawable(metaclass=ABCMeta):
    @abstractmethod
    def __contains__():
        pass

    # overloading
    def __and__(self, other):
        return Intersection(self, other)
    def __or__(self, other):
        return Union(self, other)
    def __sub__(self, other):
        return Difference(self, other)
    
    def draw(self, canvas):
        for x in range(int(canvas['width'])+1):
            for y in range(int(canvas['height'])+1):
                if (x - (int(canvas['width'])/2), (int(canvas['height'])/2) - y) in self:
                    draw_pixel(canvas, x, y)

class Circle(Drawable):
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        if r>0:
            self.r = r
    def __contains__(self, point): # check with prof if contains should be inclusive of border
        return True if sqrt((point[0]-self.x)**2 + (point[1]-self.y)**2) <= self.r else False
    def __repr__(self):
        return "Circle:center = ({},{}), radius = {}".format(self.x, self.y, self.r)

class Rectangle(Drawable):
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
    def __contains__(self, point):
        return True if (point[0] >= self.x0 and point[0] <= self.x1 and point[1] >= self.y0 and point[1] <= self.y1) else False
    def __repr__(self):
        return "Rectangle:left bottom = ({},{}), top right = ({},{})".format(self.x0, self.y0, self.x1, self.y1)

class Intersection(Drawable):
    def __init__(self, shape1, shape2):
        self.shape1 = shape1
        self.shape2 = shape2
    def __contains__(self, point):
        return point in self.shape1 and point in self.shape2
    def __repr__(self):
        return "Intersection of {} and {}".format(self.shape1, self.shape2)

class Union(Drawable):
    def __init__(self, shape1, shape2):
        self.shape1 = shape1
        self.shape2 = shape2
    def __contains__(self, point):
        return point in self.shape1 or point in self.shape2
    def __repr__(self):
        return "Union of {} and {}".format(self.shape1, self.shape2)

class Difference(Drawable):
    def __init__(self, shape1, shape2):
        self.shape1 = shape1
        self.shape2 = shape2
    def __contains__(self, point):
        return point in self.shape1 and point not in self.shape2
    def __repr__(self):
        return "Difference between {} and {}".format(self.shape1, self.shape2)        

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 500

def draw_pixel(canvas, x, y, color='#000000'):
    '''Draw a pixel at (x,y) on the given canvas'''
    x1, y1 = x - 1, y - 1
    x2, y2 = x + 1, y + 1
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)

def main(shape):
    '''Create a main window with a canvas to draw on'''
    master = tk.Tk()
    master.title("Drawing")
    canvas = tk.Canvas(master, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack(expand=tk.YES, fill=tk.BOTH)

    shape.draw(canvas)
    
    # Starts the Tk event loop (in this case, it doesn't do anything other than
    # show the window, but we could have defined "event handlers" that intercept
    # mouse clicks, keyboard presses, etc.)
    tk.mainloop()

        
if __name__ == '__main__':
    head = Circle(0, 0, 200)
    left_eye = Circle(-70, 100, 20)
    right_eye = Circle(70, 100, 20)
    mouth1 = Circle(0, -50, 80)
    mouth2 = Rectangle(-80, -130, 80, -50)
    mouth_total = mouth1 & mouth2
    
    # Add to smiley by giving him a hat
    hat_bottom = Rectangle(-200, 125, 200, 200)
    hat_top = Rectangle(-100, 175, 100, 350)
    
    happy_face = head - left_eye - right_eye - mouth_total
    
    # Draw the happy face
    main(happy_face | hat_bottom | hat_top)



