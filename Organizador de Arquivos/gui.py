from elevate import elevate
import ctypes
import customtkinter as tk
import tkinter.filedialog
import os
import functions
from time import sleep


# Confere se o progrma está sendo executado como administrador para ter as permissçoes necessárias
#is_admin = ctypes.windll.shell32.IsUserAnAdmin() == 1

# Se não estiver, pede para tal
#if not is_admin:
    #elevate()


# Classe para as funções de execução da organização de arquivos
class Action:
    def __init__(self):
        self.dir = ''

    def organize_files(self):
        self.dir = tkinter.filedialog.askdirectory(title="Choose a directory!")
        functions.create_dir_by_file_format(self.dir)

    def undoo(self):
        try:
            functions.undoo_dir_organization(self.dir)
        except FileNotFoundError:
            warning_label.configure(text='Choose a dir first!')
            warning_label.pack()
            warning_label.after(3000, lambda: warning_label.configure(text=''))


# Classe para as funções de execução da mudança de cor dos diretórios
class Color:
    def __init__(self):
        self.choice = None

    def choose(self, choice):
        self.choice = os.path.join(os.path.dirname(
            __file__), 'colors', f'{choice.lower()}.ico')

    def change_color_(self):
        dir = tkinter.filedialog.askdirectory(
            title="Choose a directory to change color")
        if self.choice:
            functions.change_dir_color(dir, self.choice)

class Rename:
    def __init__(self):
        self.choice = None

    def choose(self, choice):
        if not choice:
            return
        if choice == 'Date':
            self.choice = 'date'
            return
        self.choice = 'enumerate_by_date'

    def rename_files(self):
        self.dir = tkinter.filedialog.askdirectory(title='Choose a directory to rename all the files:')
        if not self.choice:
            return
        functions.rename_all_files(self.dir, self.choice)
        

def open_file():
    file_path = tkinter.filedialog.askdirectory(title='Select a file: ')
    # select_file_button.grid_forget()
    return file_path


# Função para a digitação de um texto quando o arquivo é aberto
def type_text(label, text, index=0):
    if index < len(text):
        current_text = f'{text[:index+1]}'
        label.configure(text=current_text)
        label.after(100, type_text, label, text, index+1)


# Janela principal
def main():
    tk.set_appearance_mode('dark')
    tk.set_default_color_theme('blue')

    window = tk.CTk()
    window.title('File Manager')
    window.geometry('1920x1080+0+0')
    commands = Action()

    label = tk.CTkLabel(window, text="", font=("Jetbrains Mono", 40))
    label.pack(pady=90)
    label.place(relx=0.25, rely=0.1, anchor='center')

    type_text(label, "Create subdirs by file Type:")

    dir_button = tk.CTkButton(window, text='Choose directory',
                              command=commands.organize_files, corner_radius=1000)
    dir_button.pack()
    dir_button.configure(font=("Jetbrains Mono", 26))
    dir_button.place(relx=0.25, rely=0.2, anchor='center')

    label2 = tk.CTkLabel(window, text='')
    label2.pack(pady=5)

    undoo_button = tk.CTkButton(window, text='Undoo',
                                command=commands.undoo, corner_radius=40)
    undoo_button.pack(padx=10)
    undoo_button.configure(font=("Jetbrains Mono", 26))
    undoo_button.place(relx=0.25, rely=0.27, anchor='center')

    global warning_label
    warning_label = tk.CTkLabel(window, text="", font=("Jetbrains Mono", 18))
    warning_label.pack(pady=20)

    color_ = Color()

    color_change = tk.CTkLabel(window, text="", font=('Jetbrains Mono', 40))
    color_change.pack(pady=50)
    color_change.place(relx=0.25, rely=0.5, anchor='center')
    type_text(color_change, "Change Dir Color:")

    values = []
    directory = os.listdir(os.path.join(os.path.dirname(__file__), 'colors'))
    for color in directory:
        values.append(color.replace('.ico', '').title())

    choose_icon = tk.CTkOptionMenu(window, values=values,
                                   font=("Jetbrains Mono", 30), corner_radius=15,
                                   command=color_.choose)
    choose_icon.pack(pady=20)
    choose_icon.set("Choice: ")
    choose_icon.place(relx=0.25, rely=0.6, anchor='center')

    choose_dir = tk.CTkButton(window, text='Choose dir', corner_radius=20,
                              font=('Jetbrains Mono', 26), command=color_.change_color_)
    choose_dir.pack(pady=20)
    choose_dir.place(relx=0.25, rely=0.67, anchor='center')

    rename_files_label = tk.CTkLabel(window, text='', font=('Jetbrains Mono', 40))
    rename_files_label.pack(pady=5)
    rename_files_label.place(relx=0.75, rely=0.1, anchor='center')
    type_text(rename_files_label, 'Rename all files by:')

    rename = Rename()

    choose_rename = tk.CTkOptionMenu(window, values=['Date', 'Enumerate by date'],
                                   font=("Jetbrains Mono", 30), corner_radius=15,
                                   command=rename.choose)
    choose_rename.pack(pady=20)
    choose_rename.set("Choice: ")
    choose_rename.place(relx=0.75, rely=0.2, anchor='center')

    choose_dir = tk.CTkButton(window, text='Choose dir', corner_radius=20,
                              font=('Jetbrains Mono', 26), command=rename.rename_files)
    choose_dir.pack(pady=20)
    choose_dir.place(relx=0.75, rely=0.27, anchor='center')

    window.mainloop()


if __name__ == '__main__':

    main()
