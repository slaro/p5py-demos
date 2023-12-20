from p5 import *

width = 600
height = 600

def setup():
    size(width, height)
    background(100)

def draw_circle(v):
    if v > 0:
        ellipse(spiral_x(v), spiral_y(v), spiral_r(v), spiral_r(v))
        draw_circle(v - 0.7)

def draw():
    background(0)
    noFill()
    circle_color = Color(r=114, g=222, b=194, a=25)
    stroke(circle_color)
    strokeWeight(1)
    draw_circle(300)

def spiral_x(v):
    center_x = width / 2
    inner = (v / 25.0) + (millis() * 0.001)
    outer = cos(inner) * (v / 2.0)
    return (center_x + outer)

def spiral_y(v):
    center_y = height / 2
    inner = (v / 11.0) # + (millis() * 0.001)
    outer = sin(inner) * (v / 2.0)
    return (center_y + outer)

def spiral_r(v):
    return (v / 2.0)

run(renderer="skia")