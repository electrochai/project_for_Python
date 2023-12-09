# windows.py

# класс инструмента окна для рисования
class Canvas_for_drawing:
    def __init__(self):
        self.bg_color = "white"
        self.width = 800
        self.height = 600
        self.draw = "Null"
        self.name_project = "test"
    
    def bg_color_change(self, new_bg_color):
        self.bg_color = new_bg_color

    def width_change(self, new_width):
        self.width = new_width

    def width_change(self, new_height):
        self.height = new_height
    
    def delete(self):
        del self.draw
        del self