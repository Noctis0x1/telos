from tkinter import Label
from tkinter import Frame
import tkinter as tk

class file_title():
    def __init__(self) -> None:
        pass

    # def open_url(self, url):
    #     self.webbrowser.open_new_tab(url)

    def display(self, name):
        self.files.insert(0, name)
        print(self.files)
        for j, i in enumerate(self.files):
            print("j=", j)
            label_frame = tk.Frame(self.mainBody, borderwidth=2, relief="solid", bg="#575757")
            label_frame.grid(column=0, row=j+10, sticky="w", padx=25, pady=(2,2))
            label = Label(label_frame, text=i, anchor="w", justify="left", width=50, background="#cccccc")
            label.grid(column=0, row=10+j)
            # row = label.grid_info()["row"]
        # label.grid_configure(row=row)
            # label.bind("<Button-1>", lambda e:self.open_url(self, ""))



def main(self):
    file_title.display(self)

if __name__ == "__main__":
    main()