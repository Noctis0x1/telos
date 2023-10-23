import tkinter as tk

root = tk.Tk()

# Create a parent frame using the grid manager
parent_frame = tk.Frame(root)
parent_frame.grid(row=2, column=10)

# Create labels within the parent frame
label1 = tk.Label(parent_frame, text="Label 1")
label2 = tk.Label(parent_frame, text="Label 2")

# Create a child frame within the parent frame
child_frame = tk.Frame(parent_frame)
child_frame.grid(row=3, column=0, columnspan=2)

# Create labels within the child frame
label3 = tk.Label(child_frame, text="Label 3")
label4 = tk.Label(child_frame, text="Label 4")

# Arrange labels within the parent frame
label1.grid(row=0, column=0)
label2.grid(row=0, column=1)

# Arrange labels within the child frame
label3.grid(row=0, column=0)
label4.grid(row=0, column=1)

root.mainloop()
