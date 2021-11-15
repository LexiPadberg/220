"""
Name: Lexi Padberg
button.py

Problem: this problem creates a user-defined class

Certification of Authenticity: I certify that this assignment is entirely my own work
"""

from graphics import Text
class Button:
    def __init__ (self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def color_button(self, color):
        self.shape.setFill(color)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, click):

        if click.getX() >= self.shape.getP1().getX() and click.getX() <= self.shape.getP2().getX() \
                and click.getY() >= self.shape.getP1().getY() \
                and click.getY() <= self.shape.getP2().getY():
            return True
        return False
