# Code from https://p5.readthedocs.io/en/latest/examples/input/clock.html

from p5 import *

cx , cy = (0, 0)
secondsRadius = 0
minutesRadius = 0
hoursRadius = 0
clockDiameter = 0

def setup():
        global cx, cy, secondsRadius, minutesRadius, hoursRadius, clockDiameter

        size(640, 360)
        stroke(255)

        radius = min(width, height) / 2

        secondsRadius = radius * 0.72
        minutesRadius = radius * 0.60
        hoursRadius = radius * 0.50
        clockDiameter = radius * 1.8

        cx = width / 2
        cy = height / 2

def draw():
        global cx, cy, secondsRadius, minutesRadius, hoursRadius, clockDiameter
        background(102)

        # Draw the clock background
        fill(80)
        no_stroke()
        ellipse((cx, cy), clockDiameter, clockDiameter)

        # Angles for sin() and cos() start at 3 o'clock
        # subtract HALF_PI to make them start at the top
        s = remap(second(), [0, 60], [0, TWO_PI]) - HALF_PI
        m = remap(minute() + normalize(second(), 0, 60), [0, 60], [0, TWO_PI]) - HALF_PI
        h = remap(hour() + normalize(minute(), 0, 60), [0, 24], [0, TWO_PI * 2]) - HALF_PI

        # Draw the hands of the clock
        stroke(255)
        stroke_weight(1)
        line([cx, cy], [cx + cos(s) * secondsRadius, cy + sin(s) * secondsRadius])
        stroke_weight(2)
        line([cx, cy], [cx + cos(m) * minutesRadius, cy + sin(m) * minutesRadius])
        stroke_weight(4)
        line([cx, cy], [cx + cos(h) * hoursRadius, cy + sin(h) * hoursRadius])

        # Draw the minute ticks
        stroke_weight(2)
        begin_shape(POINTS)
        for a in range(0, 360, 6):
                angle = radians(a)
                x = cx + cos(angle) * secondsRadius
                y = cy + sin(angle) * secondsRadius
                vertex(x, y)
        end_shape()


if __name__ == '__main__':
        run(renderer="skia")