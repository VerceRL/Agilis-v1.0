from tkinter import filedialog
from tkinter import *

def custom_directory():
    root = Tk()
    root.withdraw()
    folder_selected = filedialog.askdirectory()
    print(folder_selected)

custom_directory()
