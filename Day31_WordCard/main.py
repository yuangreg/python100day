import tkinter as tk

import pandas
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pd.read_csv("data/my_words.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")
word_pairs = df.to_dict(orient="Records")
print(word_pairs)
current_pair = None
flip_item = None

def next_word():
    global current_pair, flip_item
    canvas.itemconfig(image_item, image=card_front_img)
    current_pair = random.choice(word_pairs)
    canvas.itemconfig(title_item, text="French")
    canvas.itemconfig(word_item, text=current_pair["French"])
    if flip_item:
        window.after_cancel(flip_item)
    flip_item = window.after(3000, func=flip_card)

def known_word():
    word_pairs.remove(current_pair)
    next_word()
    # Save the word list
    df = pandas.DataFrame(word_pairs)
    df.to_csv("data/my_words.csv", index=False)

def flip_card():
    canvas.itemconfig(title_item, text="English")
    canvas.itemconfig(word_item, text=current_pair["English"])
    canvas.itemconfig(image_item, image=card_back_img)

window = tk.Tk()
window.title("Word Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


canvas= tk.Canvas(width=800, height=526)
card_front_img = tk.PhotoImage(file="images/card_front.png")
card_back_img = tk.PhotoImage(file="images/card_back.png")
image_item = canvas.create_image(400, 263, image=card_front_img)
title_item = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_item = canvas.create_text(400, 263, text="Word", font=("Ariel", 40, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


wrong_image = tk.PhotoImage(file="images/wrong.png")
right_image = tk.PhotoImage(file="images/right.png")
wrong_button = tk.Button(image=wrong_image, command=next_word)
right_button = tk.Button(image=right_image, command=known_word)
wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=1)

next_word()

window.mainloop()