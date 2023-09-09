from tkinter.messagebox import showinfo
from tkinter import filedialog as fd 
import display_file_title

class file():
    def __init__(self) -> None:
        pass

    def add(self):
        fileTypes = (("PDF files", '*.pdf'), ("EPUB files", '*.epub'))
        fileName = fd.askopenfilename(title = "Open a file", initialdir = '~', filetypes = fileTypes)
        showinfo(title = "Selected files", message=fileName)
        display_file_title.file_title.display(self, fileName)

def main(self):
    file.add(self)

if __name__ == "__main__":
    main()