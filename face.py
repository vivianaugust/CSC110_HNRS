from graphics import graphics

def main():
    gui = graphics(500, 500, 'Face')
    gui.ellipse(250, 250, 400, 400, 'dodger blue')
    gui.ellipse(150, 200, 50, 50, 'green')
    gui.ellipse(350, 200, 50, 50, 'green')
    gui.rectangle(150, 325, 200, 50, 'pale green')
    gui.triangle(250, 175, 200, 300, 300, 300, 'wheat3')
    i = 100
    while i < 400:
        gui.line(i, 25, i, 125, 'orange')
        i += 10
    gui.text(320, 445, 'ROBOT', 'blue', 50)
    gui.draw()

main()