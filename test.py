import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import filedialog as fd


class FileReaderApp:
    def __init__(self, root):
        self.root = root
        root.title("Telos: File Reader")
        root.geometry("900x700")
        root.configure(background="#b6b6b6")

        self.files = []
        
        self.add_button = tk.Button(root, text="Add a file", command=self.add_file)
        self.add_button.grid(row=1)

        #hover

        # label = tk.Label(root, text="change it")
        # label.grid()

        # def on_enter(event):
        #     label.config(bg='lightblue', fg='red')

        # def on_leave(event):
        #     label.config(bg='white', fg='black')

        # label.bind("<Enter>", on_enter)
        # label.bind("<Leave>", on_leave)

        #hover




    def add_file(self):
        file_types = (("PDF files", '*.pdf'), ("EPUB files", '*.epub'))
        file_name = fd.askopenfilename(title="Open a file", initialdir='~', filetypes=file_types)
        if file_name:
            showinfo(title="Selected files", message=file_name)
            self.display_file_title(file_name)

    def display_file_title(self, name):
        self.files.append(name)
        print(self.files)
        label = tk.Label(self.root, text=name, anchor="w", justify="left", width=100)
        label.grid(column=1, row=len(self.files) + 1)

        column = label.grid_info()["column"]
        row = label.grid_info()["row"]

        def on_enter(event):
            # label.place_configure(z)
            button = tk.Button(self.root, text="But")
            button.grid(column=column, row=row)
            print(column,row)
            label.grid_forget()


        def on_leave(event):
            label.config(bg='white', fg='black')
            label.grid_forget()

        label.bind("<Enter>", on_enter)
        label.bind("<Leave>", on_leave)
 
    


def main():
    root = tk.Tk()
    app = FileReaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
