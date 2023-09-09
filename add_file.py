from tkinter.messagebox import showinfo
from tkinter import filedialog as fd 
from tkinter import Tk
from tkinter import ttk
from tkinter import Label

class add_file():
    def __init__(self) -> None:
        pass

    def add(self):
        fileTypes = (("PDF files", '*.pdf'), ("EPUB files", '*.epub'))
        fileName = fd.askopenfilename(title = "Open a file", initialdir = '~', filetypes = fileTypes)
        showinfo(title = "Selected files", message=fileName)
        self.displayFileTitle(fileName)

def main(self):
    add_file.add(self)

if __name__ == "__main__":
    main()