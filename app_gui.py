from tkinter import *
from funcs import *

window = Tk()

select_file_button = Button(window, text = 'Select file', command = open_file)
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
select_file_button = select_file_button.grid(column=0, row = 0, sticky='')

window.mainloop()