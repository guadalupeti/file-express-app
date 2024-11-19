import os
from pathlib import Path
from datetime import datetime
from tkinter import *
from tkinter import filedialog
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".ogg", ".flac"],
    "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Others": [] 
}

def open_file():
    file_path = filedialog.askdirectory(title = 'Select a file: ')
    select_file_button.grid_forget()
    return file_path

def rename_all_files(folder: str, define_for: str):

    match define_for:
        case 'date':
            for file in os.listdir(folder):
                complete_path = os.path.join(folder,file)
                if os.path.isfile(complete_path):
                    timestamp = os.path.getctime(complete_path)
                    date = datetime.fromtimestamp(timestamp)
                    formated_date = date.strftime("%d-%m-%y")
                    extension = os.path.splitext(file)[1]
                    new_path = os.path.join(folder, f'{formated_date}{extension}')
                    os.rename(complete_path, new_path)
            return True
        
        case 'enumerate_by_date':
            files_to_enumerate = []
            for file in os.listdir(folder):
                complete_path = os.path.join(folder,file)
                if os.path.isfile(complete_path):
                    timestamp = os.path.getctime(complete_path)
                    date = datetime.fromtimestamp(timestamp)
                    files_to_enumerate.append((complete_path, date))

            files_to_enumerate.sort(key = lambda x: x[1])
            
            for i, file in enumerate(files_to_enumerate, start = 1):
                extension = os.path.splitext(file[0])[1]
                new_path = os.path.join(folder, f'{i}{extension}')
                os.rename(file[0], new_path)

            return True

def organize_file_in_folders(folder: str, define_for: str):

    match define_for:
        case 'by_type':
            for file in os.listdir(folder):
                complete_path = os.path.join(folder,file)

                if not os.path.isfile(complete_path):
                    continue


                _, extension = os.path.splitext(file)
                extension = extension.lower()

                categorie = 'Others'

                for cat, ext_list in FILE_CATEGORIES.items():
                    if extension in ext_list:
                        categorie = cat
                        break
                
                destiny_folder = os.path.join(folder, categorie)
                os.makedirs(destiny_folder, exist_ok=True)

                new_path = os.path.join(destiny_folder, file)
                shutil.move(complete_path, new_path)

                

        
def open_window():
    global select_file_button 

    def set_option_date():
        nonlocal option
        option = 'date'
        rename_all_files(open_file, option)
        return option
    
    def set_option_enumerate_date():
        nonlocal option
        option = 'enumerate_by_date'
        rename_all_files(open_file, option)
        return option

    window = Tk()
    select_file_button = Button(window, text = 'Select file', command = open_file)
    window.columnconfigure(0, weight=1)
    window.rowconfigure(0, weight=1)
    select_file_button = select_file_button.grid(column=0, row = 0, sticky='')
    if not select_file_button.winfo_ismapped():
        option = None
        date_button = Button(window, text = 'Rename with creation date', command = set_option_date)
        enumerate_by_date_button = Button(window, text = 'Enumerate by creation date', command = set_option_enumerate_date)
        date_button.grid(column=0, row = 0, sticky='', padx=10, pady = 10)
        enumerate_by_date_button.grid(column=1, row = 0, sticky='', padx=10, pady = 10)

    window.mainloop()



