"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Justin Heinz.
"""
########################################################################
# Done: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()
justin = rg.SimpleTurtle('turtle')
justin.pen = rg.Pen('blue', 30)
justin.speed = 8
ashley = rg.SimpleTurtle()
ashley.pen = rg.Pen('red', 30)
ashley.speed = 5

justin.forward(200)
ashley.backward(200)
size = 200

for k in range(3):
    justin.draw_circle(size)
    ashley.draw_square(size)
    size = size - 50
justin.pen_up()
justin.right(90)
justin.forward(250)
justin.left(50)
justin.pen_down()
window.tracer(200)
for k in range(300):
    justin.left(85)
    justin.forward(k)

window.close_on_mouse_click()
