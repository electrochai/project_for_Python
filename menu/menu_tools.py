# menu_tools.py

# библиотека которая содержит в себе настройку окно инструментов 

import tkinter as tk

import menu.menu_color as menu_color
import menu.menu_size_brush as menu_size_brush
from tools.brush import brush
from windows.windows_draw import window_draw

def echo(window_main):
    # color_brush_menu
    menu_color.echo(window_main) # 2 * 20 = 40

    # size_brush_menu
    menu_size_brush.echo(window_main)

    # создание области в которой будут находиться инструменты
    tools_frame = tk.Frame(
        window_main, 
        width=50, 
        height=40,
        # bg="blue"
        )
    
    # инструмент ластик который в зависимости от фона меняет  свои свойства
    lastik_btn = tk.Button(tools_frame, text="lastik", width=20, command=lambda: (brush.color_change(window_draw.bg_color), brush.color_outline_change(window_draw.bg_color)))
    # кнопка которая очищает холст
    clear_btn = tk.Button(tools_frame, text="clear", width=20, command=lambda: window_draw.draw.delete("all"))

    # размещение кнопки ластика
    lastik_btn.place(x=0,y=5,height=15,width=50)
    # размещение кнопки очистка
    clear_btn.place(x=0,y=20,height=15,width=50)
    # размещение области с инструментами
    tools_frame.place(x=100)