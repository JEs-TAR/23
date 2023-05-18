import tkinter as tk
from main_2 import *

def on_play():
    global root_game
    root_game.destroy()
    game_window()

root_game = tk.Tk()

root_game.title("Gender Guesser!")
icon = tk.PhotoImage(file="Resources\icon_image.png")
root_game.iconphoto(True,icon)
root_game.geometry("700x700")
root_game.config(bg="#886b92")

Banner = tk.PhotoImage(file="Resources\\banner(1).png")
L1 = tk.Label(root_game,image=Banner)
L1.place(x=100,y=180)

b1 = tk.Button(root_game,text="Play",command=on_play,font=("Times",12,"bold"))
b1.place(x=320,y=450)

root_game.mainloop()

