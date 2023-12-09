import tkinter as tk

import menu.main_menu as main_menu
import menu.menu_tools as menu_tools
import windows.windows_draw as windows_draw

def echo():
    window = tk.Tk()
    window.title('Draw NAJV' + ' - ' + windows_draw.window_draw.name_project)

    icon = tk.PhotoImage(file = "./pictures/icon.png")
    window.iconphoto(True, icon)

    main_frame = tk.Frame(window, 
                      width=windows_draw.window_draw.width+10, 
                      height=windows_draw.window_draw.height+50)

    # main_menu
    main_menu.echo(window)

    # menu_instruments
    menu_tools.echo(main_frame)

    # drawing
    windows_draw.echo(main_frame)

    main_frame.pack()

    window.mainloop()