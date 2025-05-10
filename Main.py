import os
import psutil
import webbrowser

import tkinter as tk
from tkinter import scrolledtext

from HelperPage import Helper


# welcome page
def show_welcome_page(): Helper(window, window['bg'], 'Welcome').welcome_page()
# documents page
def show_documents_page(): Helper(window, window["bg"], 'Documents').documents_page()
# about page
def show_about_page(): Helper(window, window['bg'], 'About').about_page()


# close/exit event
def on_close():
    global work
    work = True
    window.destroy()
    my_id = os.getpid()
    for proc in psutil.process_iter():
        try:
            if proc.pid == my_id: proc.kill()
        except: pass
        
        
# create gui window
window = tk.Tk()
window.title('eSmart LIS Connector')
window.configure(bg="lightgray")

menubar   = tk.Menu(window)
file_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Exit", font=('Arial', 8), command=on_close)

edit_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit_menu)
        
help_menu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="Welcome", font=('Arial', 8), command=show_welcome_page)
help_menu.add_command(label="Documents", font=('Arial', 8), command=show_documents_page)
help_menu.add_separator()
help_menu.add_command(label="About", font=('Arial', 8), command=show_about_page)

menubar.add_command(label='Install Packages')
menubar.add_command(label="Select All")

try: window.config(menu=menubar)
except AttributeError: window.tk.call(window, "config", "-menu", menubar)

byte_text_box = scrolledtext.ScrolledText(window, width=106, height=21)
byte_text_box.grid(row=0, column=0, columnspan=5, rowspan=50, padx=(15, 0), pady=(5, 0), sticky='ew')
byte_text_box.insert(tk.END, '\n\n\n\n'+'\n'.join(Helper._Helper__developer_profile)+'\n\n\n'+' | '.join(Helper._Helper__app_information))


link = tk.Label(window, text='J O N A K I  |  N E T W O R K', cursor='hand2', font=('Arial', 8, 'bold'), bg='lightgray', fg='gray')
link.grid(row=50, column=0, columnspan=5, padx=0, pady=0, sticky='ew')
link.bind('<Button-1>', lambda _: webbrowser.open_new("https://www.facebook.com/jonakisoft.net/"))
    

__widthSize   = 900
__heightSize  = 367

x = (window.winfo_screenwidth() / 2) - (__widthSize / 2)
y = (window.winfo_screenheight() / 2) - (__heightSize / 2)
window.geometry('%dx%d+%d+%d' % (__widthSize, __heightSize, x, y-50))
window.protocol('WM_DELETE_WINDOW', on_close)
window.resizable(0, 0)
window.mainloop()