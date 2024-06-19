import time
import tkinter as tk
import threading

class Display:
    def __init__(self):
        self.window = tk.Tk()

    def show(self, d):
        for key, value in d.items():
            tk.Label(self.window, text=f"{key}: {value}").pack()
        self.window.update()

    def close(self):
        self.window.destroy()

# 测试

obj = Display()

for i in range(10):
    time.sleep(10)
    d = {"name": "John", "age": 30+i, "city": "New York"}
    obj.show(d)
    print(i)
