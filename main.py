from tkinter import Tk
from tkinter import ttk
import add_file
import display_file_title

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
        add_file.main(self)
 

    def displayFileTitle(self):
        display_file_title.main(self)

        
def main():
    mainBody = Tk()
    telos(mainBody)
    mainBody.mainloop()

if __name__ == "__main__":
    main()


