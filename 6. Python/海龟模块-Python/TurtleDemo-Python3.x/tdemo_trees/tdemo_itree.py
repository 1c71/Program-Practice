"""      turtle-example-suite:

            tdemo_itree.py

Displays a 'breadth-first-tree' - in contrast
to the classical Logo tree drawing programs,
which use a depth-first-algorithm.

Uses turtle-cloning: At each branching point
the current turtle is cloned.

Branching depth is visualized by colors.

As the recursive breadth first tree scripts
are tail recursive they can easily be
transformed into iterative versions.
This is an example.
"""

from turtle import Screen, Turtle

screen = Screen()

def itree(t, l, f, colors):
    t.color(colors[0])
    t.forward(l)
    turtles = [t]
    colors.pop(0)
    while colors:
        l *= f
        newturtles = []
        for t in turtles:
            t.color(colors[0])
            t1 = t.clone()
            t.left(45)
            t.forward(l)
            t1.right(45)
            t1.forward(l)
            newturtles.extend([t, t1])
        turtles = newturtles
        colors.pop(0)
    for t in turtles:
        t.color("green")
            
def main():
    screen.mode("logo")
    t = Turtle(shape="triangle")
    t.penup(); t.back(280); t.pendown()
    t.pensize(3)
    itree(t, 250, 0.63,
          ["black", "brown", "red", "orange", "violet", "lightblue"])

if __name__ == '__main__':
    main()
    screen.mainloop()
