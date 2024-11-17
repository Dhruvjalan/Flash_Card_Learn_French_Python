from tkinter import *
import pandas
import csv
import random
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
print(to_learn)

window = Tk()
window.title("Flash Card Game")
window.config(padx=50, pady=50)


def disp_english(random_word):

    global back_card_img
    canvas1.itemconfig(card_img, image=back_card_img)
    canvas1.itemconfig(title, text="English")
    canvas1.itemconfig(word, text=random_word["English"])


def button_clicked():
    global front_card_img, flip_timer
    window.after_cancel(flip_timer)
    canvas1.itemconfig(card_img, image=front_card_img)
    random_word = random.choice(to_learn)
    canvas1.itemconfig(title, text="French")
    canvas1.itemconfig(word, text=random_word["French"])
    print("Button clicked")
    flip_timer = window.after(3000, disp_english,random_word)
    return random_word


def yes_clicked():
    correct_word = button_clicked()
    to_learn.remove(correct_word)


def no_clicked():
    wrong_word = button_clicked()
    to_learn.remove(wrong_word)


canvas1 = Canvas(height=526, width=800)
back_card_img = PhotoImage(file="images/card_back.png")
front_card_img = PhotoImage(file="images/card_front.png")
card_img = canvas1.create_image(400, 263, image=front_card_img)
title = canvas1.create_text(400,150, text="", font=('Aerial', 20,'bold'))
word = canvas1.create_text(400,200, text="", font=('Aerial', 20,'normal'))
canvas1.grid(row=0, column=1)

tick_img = PhotoImage(file="images/right.png")
tick_button = Button(image=tick_img, highlightthickness=0, command=yes_clicked)
tick_button.grid(row=1, column=2)


wrong_img = PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_img, highlightthickness=0, command=no_clicked)
wrong_button.grid(row=1, column=0)
flip_timer = window.after(3000,func=disp_english)

button_clicked()

window.mainloop()