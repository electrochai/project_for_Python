# windows_draw.py

# библиотека которая создает рабочию поверхность для рисования 
# используя класс кисть и класс окна

# а также присутствует функция которая рисует следуя за мышкой

import tkinter as tk

from tools.brush import brush # добавление объекта класса кисть
from tools import windows # подключение класса окна

# объявление глобальной переменойф окна рисования как объекта класса окно
window_draw = windows.Canvas_for_drawing()

def echo(window_main):
    # функция рисует с помощью кругов \ аналог кисти
    def paint(event):
        x1 = event.x - brush.size
        x2 = event.x + brush.size
        y1 = event.y - brush.size
        y2 = event.y + brush.size
        window_draw.draw.create_oval(x1, y1, x2, y2, fill=brush.color_fill, outline=brush.color_outline)

    # создание окна для рисования
    window_draw.draw = tk.Canvas(window_main, 
                     width=window_draw.width-5, 
                     height=window_draw.height-5, 
                     bg=window_draw.bg_color, 
                     borderwidth=2)
    
    # прорисовка окна для рисования
    window_draw.draw.place(x=5,y=45)
    
    # использование мыши для рисование
    window_draw.draw.bind("<B1-Motion>", paint)