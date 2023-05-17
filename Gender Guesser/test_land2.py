import tkinter as tk
from test_land import *
def on_play():
    global root
    root.destroy()
    game_window()

root = tk.Tk()
b1 = tk.Button(text="click me",command=on_play)
b1.place(x=10,y=20)
root.mainloop()