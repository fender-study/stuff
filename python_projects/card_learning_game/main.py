from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FRENCH_TITLE = "French"
TITLE_FONT = ("Arial", 40, "italic")
WORD_FONT = ("Arial", 60, "bold")

word_list = ""
data_dict = {}
random_dict = {}
words_to_learn = []


def load_file():
    global word_list, data_dict
    try:
        word_list = pandas.read_csv("Data/words_to_learn.csv")
    except FileNotFoundError:
        word_list = pandas.read_csv("Data/french_words.csv")
    finally:
        data_dict = word_list.to_dict(orient="records")


def remove_word():
    global words_to_learn
    data_dict.remove(random_dict)
    words_to_learn = data_dict
    df = pandas.DataFrame(words_to_learn)
    df.to_csv("Data/words_to_learn.csv", index=False)
    pick_word()


def pick_word():
    global random_dict, flip_timer
    window.after_cancel(flip_timer)
    random_dict = random.choice(data_dict)
    canvas.itemconfig(image_item, image=card_front)
    canvas.itemconfig(top_text, text="French", fill="black")
    canvas.itemconfig(bottom_text, text=random_dict['French'], fill="black")
    flip_timer = window.after(3000, func=delayed_flip)


def delayed_flip():
    canvas.itemconfig(top_text, text="English", fill="white")
    canvas.itemconfig(image_item, image=card_back)
    canvas.itemconfig(bottom_text, text=random_dict['English'], fill="white")


load_file()

window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Flashy")

flip_timer = window.after(3000, func=delayed_flip)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.grid(column=0, row=0, columnspan=2)
image_item = canvas.create_image(400, 263, image=card_front)
top_text = canvas.create_text(400, 150, text="", font=TITLE_FONT)
bottom_text = canvas.create_text(400, 263, text="", font=WORD_FONT)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

right_button = Button(image=right_image, highlightthickness=0, command=remove_word)
right_button.grid(column=1, row=1)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=pick_word)
wrong_button.grid(column=0, row=1)

pick_word()

window.mainloop()
