# brush.py

# класс инструмента кисть
class Brush:
    def __init__(self):
        self.color_fill = "Black"
        self.color_outline = "Black"
        self.size = 5
    
    def color_change(self, new_color):
        self.color_fill = new_color
        self.color_outline = new_color

    def color_fill_change(self, new_color):
        self.color_fill = new_color

    def color_outline_change(self, new_color):
        self.color_outline = new_color

    def size_change(self, new_size):
        self.size = new_size

# создание оюъекта класса кисть
brush = Brush()