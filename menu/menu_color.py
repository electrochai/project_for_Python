# menu_color.py

# библиотека которая содержит в себе настройку окна инструментов 
# для смены цвета кисти и фона

# В этой библиотеке прописана логика для кнопок которые меняют свой цвет 
# в зависимости от цвета кисти фона и обводки кисти

import tkinter as tk
from tkinter.colorchooser import askcolor

from tools.brush import brush
from windows.windows_draw import window_draw

def echo(window_main):
    # создание окна настроек цвета
    window_color = tk.Canvas(
        window_main, 
        width=window_draw.width+10, 
        height=40, 
        bg="blue"
        )
    
    # кнопка которая меняет цвет кисти
    brush_color_now = tk.Button(
        window_color,
        bg=brush.color_fill,
        command=lambda: (
            brush.color_change(askcolor()[1]),
            brush_color_now.configure(bg=brush.color_fill),
            window_color.update(),
            )
        )
    # кнопка меняющая цвет обводки кисти
    brush_color_outline_now = tk.Button(
        window_color,
        bg=brush.color_outline,
        command=lambda: (
            brush.color_outline_change((askcolor()[1])),
            brush_color_outline_now.configure(bg=brush.color_outline),
            window_color.update(),
            )
        )
    # кнопка меняет цвет фона на рабочей поверхности
    bg_color_now = tk.Button(
        window_color,
        bg=window_draw.bg_color,
        command=lambda: (
            window_draw.bg_color_change(askcolor()[1]),
            bg_color_now.configure(bg=window_draw.bg_color),
            window_draw.draw.configure(bg=window_draw.bg_color),
            window_color.update(),
            window_draw.draw.update()
            )
        )
    
    # кнопка которая меняет цвет кисти на красный
    red_btn = tk.Button(
        window_color, 
        bg="red", 
        command=lambda: (
            brush.color_change("red"), 
            brush_color_now.configure(bg=brush.color_fill),
            window_color.update()
            )
        )
    # кнопка которая меняет цвет кисти на синий
    blue_btn = tk.Button(
        window_color,
        bg="blue",
        command=lambda: (
            brush.color_change("blue"),
            brush_color_now.configure(bg=brush.color_fill),
            window_color.update()
            )
        )
    # кнопка которая меняет цвет кисти на черный
    black_btn = tk.Button(
        window_color,
        bg="black",
        command=lambda: (
            brush.color_change("black"),
            brush_color_now.configure(bg=brush.color_fill),
            window_color.update()
            )
        )
    # кнопка которая меняет цвет кисти на белый
    white_btn = tk.Button(
        window_color,
        bg="white",
        command=lambda: (
            brush.color_change("white"),
            brush_color_now.configure(bg=brush.color_fill),
            window_color.update()
            )
        )
    
    # прорисовка окна с кнопками для смены цвета
    window_color.place(y=0)
    
    # прорисовка кнопок смены цвета
    red_btn.place(x=5,y=5,height=15,width=15)
    blue_btn.place(x=20,y=5,height=15,width=15)
    black_btn.place(x=5,y=20,height=15,width=15)
    white_btn.place(x=20,y=20,height=15,width=15)

    brush_color_now.place(x=40,y=5,height=20,width=20)
    brush_color_outline_now.place(x=50,y=15,height=20,width=20)
    bg_color_now.place(x=75,y=10,height=20,width=20)    