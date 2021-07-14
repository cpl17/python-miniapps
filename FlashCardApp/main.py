from tkinter import * 
import pandas as pd 
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    
    data = pd.read_csv('data/words_to_learn.csv')

except FileNotFoundError:

    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient = "records")

else:
    to_learn = data.to_dict(orient = "records")
    

def next_card():

    global current_card,flip_timer

    root.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text = "French", fill = "black")
    canvas.itemconfig(card_text, text = current_card["French"],fill = "black")
    canvas.itemconfigure(bg, image = card_front)

    countdown(3)

    flip_timer = root.after(3000,flip_card)

    
def flip_card():

    
    canvas.itemconfig(card_title, text = "English", fill = "white")
    canvas.itemconfig(card_text, text = current_card["English"], fill = "white")
    canvas.itemconfig(bg,image = card_back)
    canvas.itemconfig(timer_text,text="")

def is_known():

    to_learn.remove(current_card)

    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv")
    next_card()

def countdown(count):

    if count > 0:
        canvas.itemconfig(timer_text,text=count)   
        root.after(1000,countdown, count - 1)



    
#---------Create UI----------#

# Create root 

root = Tk()
root.title("Flashy")
root.configure(padx = 50, pady = 50, bg = BACKGROUND_COLOR)
root.minsize(900,1000)

flip_timer = root.after(3000, func = flip_card)


# Images 

card_back = PhotoImage(file = "./images/card_back.png")
card_front = PhotoImage(file = "./images/card_front.png")
right_img = PhotoImage(file = "./images/right.png")
wrong_img = PhotoImage(file = "./images/wrong.png")

# Create canvas 

canvas = Canvas(width = 800,height = 526, highlightthickness = 0, bg = BACKGROUND_COLOR)

bg = canvas.create_image(400,263,image = card_front)
card_title = canvas.create_text(400,150, text = "Language", font = ("Arial", 40, "italic"))
card_text = canvas.create_text(400,263, text = "Word", font = ("Arial", 60, "bold"))
timer_text = canvas.create_text(700,450, text = "3", fill = 'black', font = ("Arial", 35, "bold"))

canvas.grid(row = 0, column = 0, columnspan = 2)


# Create button

right_but = Button(image = right_img,command = is_known, highlightthickness = 0)
right_but.grid(row = 1, column = 0)

wrong_but = Button(image = wrong_img,command = next_card, highlightthickness = 0)
wrong_but.grid(row = 1, column = 1)



# Run code 


next_card()


root.mainloop()