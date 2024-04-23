from abc import ABCMeta, abstractmethod

from kivy.graphics import Canvas, Color, Line, Rectangle, Ellipse, Triangle

DELTA_UP = 50


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
        if command_as_string.strip().lower() == "delete line":
            return DeleteLineCommand()
        if command_as_string.strip().lower() == 'delete circle':
            return DeleteCircleCommand()
        if command_as_string.strip().lower() == "delete rectangle":
            return DeleteRectangleCommand()
        if command_as_string.strip().lower() == 'delete triangle':
            return DeleteTriangleCommand()
        if command_as_string.strip().lower() == 'delete all':
            return DeleteAllCommand()
        if command_as_string.strip().lower() == 'move line':
            return MoveLineCommand()
        if command_as_string.strip().lower() == 'move circle':
            return MoveCircleCommand()
        if command_as_string.strip().lower() == 'move rectangle':
            return MoveRectangleCommand()
        if command_as_string.strip().lower() == 'move triangle':
            return MoveTriangleCommand()
        if command_as_string.strip().lower() == 'move all':
            return MoveAllCommand()

        else:
            return UnknownCommand()


class Command(metaclass=ABCMeta):

    @abstractmethod
    def execute(self, canvas: Canvas):
        ...


#region Draw Commands
class DrawLineCommand(Command):

    def execute(self, canvas: Canvas):
        with canvas:
            #TODO: add group name
            Color(0., 1., 0.5, group='line')
            Line(points=[100, 100, 200, 200], width=2, group='line')


class DrawRectangleCommand(Command):

    def execute(self, canvas: Canvas):
        with canvas:
            Color(0., 0.5, 0.8, group='rectangle')
            Rectangle(pos=(400, 150), size=(20, 20), group='rectangle')


class DrawCircleCommand(Command):

    def execute(self, canvas: Canvas):
        with canvas:
            Color(0.5, 0.2, 0.3, group='circle')
            Ellipse(pos=(500, 500), size=(50, 50), group='circle')


class DrawTriangleCommand(Command):

    def execute(self, canvas: Canvas):
        with canvas:
            Color(1, 0., 0., 0.5, group='triangle')
            Triangle(points=[100, 100, 300, 300, 500, 100], group='triangle')


#endregion

#region Delete Commands
class DeleteLineCommand(Command):

    def execute(self, canvas: Canvas):
        # find children instructions in children with group 'line'
        for i in canvas.children:
            if i.group == 'line':
                canvas.remove(i)


class DeleteRectangleCommand(Command):

    def execute(self, canvas: Canvas):
        # find children instructions in children with group 'rectangle'
        for i in canvas.children:
            if i.group == 'rectangle':
                canvas.remove(i)


class DeleteCircleCommand(Command):

    def execute(self, canvas: Canvas):
        # find children instructions in children with group 'circle'
        for i in canvas.children:
            if i.group == 'circle':
                canvas.remove(i)


class DeleteTriangleCommand(Command):

    def execute(self, canvas: Canvas):
        # find children instructions in children with group 'triangle'
        for i in canvas.children:
            if i.group == 'triangle':
                canvas.remove(i)


class DeleteAllCommand(Command):

    def execute(self, canvas: Canvas):
        # delete all primitives with filled group property
        for i in canvas.children:
            if i.group:
                canvas.remove(i)


#endregion

#region Move Commands
class MoveLineCommand(Command):

    def execute(self, canvas: Canvas):
        for i in canvas.children:
            if i.group == 'line' and isinstance(i, Line):
                i.points = [p + DELTA_UP for p in i.points]


class MoveCircleCommand(Command):

    def execute(self, canvas: Canvas):
        for i in canvas.children:
            if i.group == 'circle' and isinstance(i, Ellipse):
                i.pos = (i.pos[0] + DELTA_UP, i.pos[1] + DELTA_UP)


class MoveRectangleCommand(Command):

    def execute(self, canvas: Canvas):
        for i in canvas.children:
            if i.group == 'rectangle' and isinstance(i, Rectangle):
                i.pos = (i.pos[0] + DELTA_UP, i.pos[1] + DELTA_UP)


class MoveTriangleCommand(Command):

    def execute(self, canvas: Canvas):
        for i in canvas.children:
            if i.group == 'triangle' and isinstance(i, Triangle):
                i.points = [p + DELTA_UP for p in i.points]


class MoveAllCommand(Command):

    def execute(self, canvas: Canvas):
        for i in canvas.children:
            if i.group == 'line' and isinstance(i, Line):
                i.points = [p + DELTA_UP for p in i.points]
            elif i.group == 'circle' and isinstance(i, Ellipse):
                i.pos = (i.pos[0] + DELTA_UP, i.pos[1] + DELTA_UP)
            elif i.group == 'rectangle' and isinstance(i, Rectangle):
                i.pos = (i.pos[0] + DELTA_UP, i.pos[1] + DELTA_UP)
            elif i.group == 'triangle' and isinstance(i, Triangle):
                i.points = [p + DELTA_UP for p in i.points]
#endregion

class UnknownCommand(Command):
    def execute(self, canvas):
        ...
