from p5 import *

f = None

def setup():
        global f
        size(640, 360)
        background(0)

        # Create the font
        f = create_font("Arial.ttf", 16)
        text_font(f)
        text_align("CENTER")

def draw():
        background(0)

        # Set the left and top margin
        margin = 10
        translate(margin*4, margin*4)

        gap = 46
        counter = 35

        for y in range(0, height - gap, gap):
                for x in range(0, width - gap, gap):

                        letter = chr(counter)

                        if (letter == "A" or letter == "E" or letter == "I" or letter == "0" or letter == "U"):
                                fill(255, 204, 0)
                        else:
                                fill(255)

                        # Draw the letter to the screen
                        text(letter, (x, y))

                        # Increment the counter
                        counter += 1

if __name__ == '__main__':
        run()