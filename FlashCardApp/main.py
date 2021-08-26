import pandas as pd
import tkinter as tk
from app import Application


try:
    
    data = pd.read_csv('data/words_to_learn.csv')

except FileNotFoundError:

    #If first time using app (need to learn all the words in the dict)
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient = "records")

else:
    to_learn = data.to_dict(orient = "records")



root = tk.Tk()
app = Application(to_learn,master=root)
app.next_card()
app.mainloop()