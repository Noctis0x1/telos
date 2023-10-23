from tkinter import Tk
from tkinter import ttk
import tkinter as tk
import add_file
import display_file_title

class telos():
    def __init__(self, mainBody) -> None:
        self.mainBody = mainBody

        mainBody.title("Telos: File Reader")
        mainBody.geometry("900x700")
        mainBody.configure(background = "#b6b6b6")

        mainBody.columnconfigure(0, weight=0)
        mainBody.columnconfigure(1, weight=3)
        mainBody.rowconfigure(0, weight = 0)
        mainBody.columnconfigure(3, weight=3)

        ghostLabel = ttk.Label(mainBody, text='', anchor="w", justify="left", width=115, background="#cccccc")
        ghostLabel.grid(row=0, column=0)

        for i in range(1,10):
            mainBody.rowconfigure(i, weight = 0)
            empty = ttk.Label(mainBody, text='', background="#b6b6b6")
            empty.grid(row= i, column= 1)

        self.files = []

        addButton = ttk.Button(mainBody, text = "Add a file", command=self.addFile)
        addButton.grid(row=0, column=0, sticky='N')

    def addFile(self):
        add_file.main(self)
 

    def displayFileTitle(self):
        display_file_title.main(self)

def main():
    mainBody = Tk()
    telos(mainBody)
    # body(mainBody)
    mainBody.mainloop()

if __name__ == "__main__":
    main()


