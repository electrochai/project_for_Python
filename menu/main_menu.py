# main_menu.py

# библиотека содержит функции меню

import tkinter as tk

import function.new

def echo(window_main):
    window_main.option_add("*tearOff", False)
    
    main_menu = tk.Menu(window_main)

    def about_program():
        window_about_program = tk.Tk()
        window_about_program.title("About NAJV")
        window_about_program.geometry("400x250")
    
        label_name_program = tk.Label(
            window_about_program, 
            text="NAJV - Simple Graphic Editor", 
            font=("Arial", 20)
            )
        label_authors = tk.Label(
            window_about_program,
            text="Authors: Nikolay, Alexsandra, Julia, Vladislav.", 
            font=("Arial", 14)
            )
        label_info = tk.Label(
            window_about_program,
            text=("They are students of MK-202. Together,\n"\
                  "they developed this project as a credit\n"\
                  "assignment in the subject of the Python\n"\
                  "programming language"), 
            font=("Arial", 14)
            )
        
        label_name_program.pack()
        label_authors.pack()
        label_info.pack()

        window_about_program.mainloop()

    def edit_click():
        tk.messagebox.showinfo("GUI Python", "Нажата опция Edit")
 
    #----File-----#
    file_menu = tk.Menu(main_menu)
    file_menu.add_command(label="New", command=lambda: (window_main.destroy(), function.new.echo()))
    file_menu.add_command(label="Save")
    file_menu.add_command(label="Open")
    file_menu.add_separator()
    file_menu.add_command(
        label="Exit", 
        command=window_main.destroy
        )

    #----main_menu-----#
    main_menu.add_cascade(
        label="File", 
        menu=file_menu
        )
    main_menu.add_command(
        label="Edit", 
        command=edit_click
        )
    main_menu.add_command(
        label="About", 
        command=about_program
        )

    window_main.config(menu=main_menu)
    