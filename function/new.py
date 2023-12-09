import tkinter as tk

import function.create_new_windows
import windows.windows_draw as windows_draw

def echo():
    def show_message():
        windows_draw.window_draw.name_project = entry_name_file.get() 
        windows_draw.window_draw.width = int(entry_width.get())
        windows_draw.window_draw.height = int(entry_height.get())
        window.destroy()
        function.create_new_windows.echo()
    
    window = tk.Tk()
    window.title('Draw NAJV')

    window.geometry("300x250")

    label_name_file = tk.Label(text="Name file: ")
    entry_name_file = tk.Entry()

    label_width = tk.Label(text="Size: ")
    entry_width = tk.Entry()
    label_height = tk.Label(text=" x ")
    entry_height = tk.Entry()

    btn_create = tk.Button(text="Create", command=show_message)

    label_name_file.place(x=5, y=5,height=30,width=100)
    entry_name_file.place(x=105, y=5,height=30,width=150)

    label_width.place(x=5, y=35,height=30,width=50)
    entry_width.place(x=55, y=35,height=30,width=70)
    label_height.place(x=125, y=35,height=30,width=20)
    entry_height.place(x=145, y=35,height=30,width=70)

    btn_create.place(x=5, y=70,height=30,width=270)

    window.mainloop()