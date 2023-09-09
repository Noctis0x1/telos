from tkinter.messagebox import showinfo
from tkinter import filedialog as fd 
from tkinter import Tk
from tkinter import ttk
from tkinter import Label

class telos():
    def __init__(self, mainBody) -> None:
        self.mainBody = mainBody

        self.mainBody.title("Telos: File Reader")
        self.mainBody.geometry("900x700")
        self.mainBody.configure(background = "#b6b6b6")

        self.files = []

        addButton = ttk.Button(mainBody, text = "Add a file", command=self.addFile)
        addButton.grid(row=1)


    def addFile(self):
        fileTypes = (("PDF files", '*.pdf'), ("EPUB files", '*.epub'))
        fileName = fd.askopenfilename(title = "Open a file", initialdir = '~', filetypes = fileTypes)
        showinfo(title = "Selected files", message=fileName)
        self.displayFileTitle(fileName)
 

    def displayFileTitle(self, name):
        self.files.append(name)
        print(self.files)
        for i in self.files:
            j = len(self.files)
            label = Label(self.mainBody, text=i, anchor="w", justify="left", width=100)
            label.grid(column=1, row=1+j)
    

def main():
    mainBody = Tk()
    telos(mainBody)
    mainBody.mainloop()

if __name__ == "__main__":
    main()


