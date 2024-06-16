import time
import tkinter as tk

def update_label(label, text):
    label.config(text=str(text))
    # label.update_idletasks()
    root.update()

root = tk.Tk()
label_i = tk.Label(root, text="")
label_i.pack()
label_j = tk.Label(root, text="")
label_j.pack()

for i in range(10):
    update_label(label_i, f"i: {i}")
    time.sleep(0.5)
    for j in range(2):
        update_label(label_j, f"j: {j}")
        time.sleep(0.5)

root.destroy()
