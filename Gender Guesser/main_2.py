import tkinter as tk
import requests


def male():
    global x,score_,name_display,root
    if x == "male":
        score_+=1
    x = gender_guesser()
    name_display.config(text=f"Name: {name}")
    score.config(text=f"Current Score:{score_}")

def female():
    global x,score_,name_display
    if x == "female":
        score_+=1
    x = gender_guesser()
    name_display.config(text=f"Name: {name}")
    score.config(text=f"Current Score:{score_}")



def gender_guesser():
    global name,x
    name = name_file.readline()
    name = name[0:len(name)-1]

    x = requests.get(f"https://api.genderize.io?name={name}",)
    data = x.json()
    # print(f'Name is  {name}')
    return data["gender"]

def game_window():
    global name_file,score_,name_display,score

    name_file = open("Resources\\Names.txt")
    root = tk.Tk()
    root.title("Gender Guesser!")
    root.config(bg="#55AE95")
    root.geometry("500x500")
    score_ = 0
    x = gender_guesser()

    name_display = tk.Label(root,text=f"Name: {name}",font=("ArcadeClassic",16,"bold"),bg="#55AE95")
    name_display.place(x=170,y=100)

    b1 = tk.Button(text="Male",command=male)
    b1.place(x=100, y=250, width=100, height=50)

    b2 = tk.Button(text="Female",command=female)
    b2.place(x=300, y=250, width=100, height=50)

    score = tk.Label(root,text=f"Current Score:{score_}",font=("ArcadeClassic",12,"bold"),bg="#55AE95")
    score.place(x=350,y=470)

    root.mainloop()

    print(f"You scored - {score_}")
