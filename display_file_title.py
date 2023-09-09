from tkinter import Label

class file_title():
    def __init__(self) -> None:
        pass

    def display(self, name):
        self.files.append(name)
        print(self.files)
        for i in self.files:
            j = len(self.files)
            label = Label(self.mainBody, text=i, anchor="w", justify="left", width=100)
            label.grid(column=1, row=1+j)

def main(self):
    file_title.display(self)

if __name__ == "__main__":
    main()