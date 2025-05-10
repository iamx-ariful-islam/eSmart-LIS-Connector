from tkinter import *


# helper class
class Helper:
    __width_size  = 480
    __height_size = 220
    
    __font_size   = ('Arial', 9, 'bold')
    __note_text   = '''eSmart LIS Connector is an all in one application with multiple device, instrument, analyzer connection at a time.'''
    __app_information   = ['eSmart LIS Connector', '15 04 vM15', '15.04.2025 (Tuesday)']
    __developer_profile = ['Md. Ar!ful Islam', 'ariful.cse08@gmail.com', '01794899422 | 01714732878']
    
    
    def __init__(self, parent, color_scheme, is_page=None):
        self.color_scheme = color_scheme
        self.top_window   = Toplevel(parent, bg=color_scheme)
        self.top_window.title(is_page)
        self.top_window.resizable(False, False)
        
        # ensure the window stays on top and make it modal
        self.top_window.transient(parent)
        self.top_window.grab_set()
        self.top_window.focus_set()
        self.top_window.wm_attributes("-topmost", 1)

        x_axis = (self.top_window.winfo_screenwidth() / 2)  - (self.__width_size / 2)
        y_axis = (self.top_window.winfo_screenheight() / 2) - (self.__height_size / 2)
        self.top_window.geometry('%dx%d+%d+%d' % (self.__width_size, self.__height_size, x_axis, y_axis-50))
        
        
    # welcome page
    def welcome_page(self):
        title = Label(self.top_window, text=self.__app_information[0], font=('Arial', 12, 'bold'), bg=self.color_scheme, fg=('black' if self.color_scheme=='lightgray' else 'white'))
        label = Label(self.top_window, text=f'{self.__app_information[1]} | Last updated: {self.__app_information[2]}', font=self.__font_size, bg=self.color_scheme, fg='gray')
        note  = Label(self.top_window, text=self.__note_text, wraplength=400, font=self.__font_size, bg=self.color_scheme, fg='red',justify=LEFT)
        title.grid(row=1, column=3, columnspan=5, padx=30, pady=(40, 0), sticky='w')
        label.grid(row=2, column=3, columnspan=5, padx=30, pady=0, sticky='w')
        note.grid(row=3, column=3, columnspan=5, padx=30, pady=0, sticky='w')
        
        label2 = Label(self.top_window, text='More Info: Help > About', font=self.__font_size, bg=self.color_scheme, fg=('blue' if self.color_scheme=='lightgray' else 'orange'))
        label2.grid(row=5, column=3, columnspan=5, padx=30, pady=(30, 5), sticky='w')


    # get documents content
    def documents_page(self):
        text_widget = Text(self.top_window, wrap='word', height=12, width=57)
        text_widget.grid(row=1, column=0, columnspan=4, rowspan=5, padx=10, pady=(12, 10))

        text_widget.delete(1.0, END)
        text_widget.insert(END, self.__note_text+'\n\n\n'+'\n'.join(self.__developer_profile))
        text_widget.config(state=DISABLED)
        

    # about page
    def about_page(self):
        # developer information
        label1 = Label(self.top_window, text='Developed by', font=('Arial', 12, 'bold'), bg=self.color_scheme, fg='gray')
        label2 = Label(self.top_window, text=self.__developer_profile[0], font=self.__font_size, bg=self.color_scheme, fg='gray')
        label3 = Label(self.top_window, text=self.__developer_profile[1], font=self.__font_size, bg=self.color_scheme, fg='gray')
        label4 = Label(self.top_window, text=self.__developer_profile[2], font=self.__font_size, bg=self.color_scheme, fg='gray')
        label1.grid(row=1, column=0, columnspan=2, padx=30, pady=(60, 0), sticky='w')
        label2.grid(row=2, column=0, columnspan=2, padx=30, pady=0, sticky='w')
        label3.grid(row=3, column=0, columnspan=2, padx=30, pady=0, sticky='w')
        label4.grid(row=4, column=0, columnspan=2, padx=30, pady=0, sticky='w')
        
        line_frame = Frame(self.top_window, bg='gray')
        line_frame.grid(row=0, column=2, rowspan=5, pady=(60, 0), sticky='ns')

        # maintenance company information
        label5 = Label(self.top_window, text='Maintenance by', font=('Arial', 12, 'bold'), bg=self.color_scheme, fg='gray')
        label6 = Label(self.top_window, text=self.__developer_profile[0],    font=self.__font_size, bg=self.color_scheme, fg='gray')
        label7 = Label(self.top_window, text=self.__developer_profile[1], font=self.__font_size, bg=self.color_scheme, fg='gray')
        label8 = Label(self.top_window, text=self.__developer_profile[2],  font=self.__font_size, bg=self.color_scheme, fg='gray')
        label5.grid(row=1, column=3, columnspan=2, padx=30, pady=(60, 0), sticky='w')
        label6.grid(row=2, column=3, columnspan=2, padx=30, pady=0, sticky='w')
        label7.grid(row=3, column=3, columnspan=2, padx=30, pady=0, sticky='w')
        label8.grid(row=4, column=3, columnspan=2, padx=30, pady=0, sticky='w')
        

# # debugging
# if __name__ == '__main__':
#     window = Tk()
#     cls_obj = Helper(window, 'lightgray', 'Welcome')
#     cls_obj.welcome_page()
#     window.mainloop()