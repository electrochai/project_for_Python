# menu_size_brush.py

# библиотека которая содержит в себе настройку размера кисти

import tkinter as tk

from tools.brush import brush

def echo(window_main):
    # создание области в которой будут находиться размеры кисти
    size_brush_frame = tk.Frame(
        window_main, 
        width=100, 
        height=40,
        # bg="red"
        )
    # кнопки быстрого изменения размера кисти
    five_btn = tk.Button(size_brush_frame, text="5", width=5, command=lambda: brush.size_change(5))
    ten_btn = tk.Button(size_brush_frame, text="10", width=5, command=lambda: brush.size_change(10))
    fiveteen_btn = tk.Button(size_brush_frame, text="15", width=5, command=lambda: brush.size_change(15))
    twenty_btn = tk.Button(size_brush_frame, text="20", width=5, command=lambda: brush.size_change(20))

    # размещение кнопок бысмтрого изменения размера кисти
    five_btn.place(x=2,y=0,height=20,width=20)
    ten_btn.place(x=27,y=0,height=20,width=20)
    fiveteen_btn.place(x=52,y=0,height=20,width=20)
    twenty_btn.place(x=77,y=0,height=20,width=20)

    # создание и размещение инструмента для считывания размера кисти введенного пользователем
    spinbox = tk.Spinbox(size_brush_frame, from_=1.0, to=100.0, command=lambda: brush.size_change(int(spinbox.get())))
    spinbox.place(x=2,y=25,height=20,width=80)
    
    # размещение области с инструментами выбора размера кисти
    size_brush_frame.place(x=160)