from abc import ABCMeta, abstractmethod

from kivy.graphics import Canvas, Color, Line, Rectangle, Ellipse, Triangle


class CommandResolver():

    @staticmethod
    def resolve(command_as_string: str):
        if command_as_string.strip().lower() == "draw line":
            return DrawLineCommand()
        if command_as_string.strip().lower() == "draw rectangle":
            return DrawRectangleCommand()
        if command_as_string.strip().lower() == "draw circle":
            return DrawCircleCommand()
        if command_as_string.strip().lower() == "draw triangle":
            return DrawTriangleCommand()

        else:
            return UnknownCommand()


class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self, canvas: Canvas):
        ...


class DrawLineCommand(Command):

    def execute(self, canvas: Canvas):
        with canvas:
            Color(0., 1., 0.5)
            Line(points=[100, 100, 200, 200], width=2)


class DrawRectangleCommand(Command):

    def execute(self, canvas: Canvas):
        with canvas:
            Color(0., 0.5, 0.8)
            Rectangle(pos=(400, 150), size=(20, 20))


class DrawCircleCommand(Command):

    def execute(self, canvas: Canvas):
        with canvas:
            Color(0.5, 0.2, 0.3)
            Ellipse(pos=(500, 500), size=(50, 50))

class DrawTriangleCommand(Command):

    def execute(self, canvas: Canvas):
        with canvas:
            Color(1, 0., 0., 0.5)
            Triangle(points=[100, 100, 300, 300, 500, 100])


class UnknownCommand(Command):
    def execute(self, canvas):
        ...
