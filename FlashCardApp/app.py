import tkinter as tk
import random 

class Application(tk.Frame):

    _BACKGROUND_COLOR = "#B1DDC6"
  

    def __init__(self, to_learn, master=None,):
        
        super().__init__(master)
        self.master = master
        self.to_learn = to_learn
        
        
        self.create_window(self._BACKGROUND_COLOR)
        self.create_canvas()
        self.create_button()
        
        



    # The Main Window #
    def create_window(self,bgcolor):

        self.master.title("Flashy")
        self.master.configure(padx = 50, pady = 50, bg = bgcolor)
        self.master.minsize(900,1000) 

        self.flip_timer_id = self.master.after(1000, func = self.flip_card)
        


    # Canvas # 
    def create_canvas(self):

        #Image
        self.card_front = tk.PhotoImage(file = "./images/card_front.png")

        #Canvas Object
        self.canvas = tk.Canvas(width = 800,height = 526, highlightthickness = 0, bg = self._BACKGROUND_COLOR)

        #Canvas Attributes
        self.bg = self.canvas.create_image(400,263,image = self.card_front)
        self.card_title = self.canvas.create_text(400,150, text = "Language", font = ("Arial", 40, "italic"))
        self.card_text = self.canvas.create_text(400,263, text = "Word", font = ("Arial", 60, "bold"))
        self.timer_text = self.canvas.create_text(700,450, text = "3", fill = 'black', font = ("Arial", 35, "bold"))

        #Canvas Geometry
        self.canvas.grid(row = 0, column = 0, columnspan = 2)



    # Buttons # 
    def create_button(self):

        #Images
        self.right_img = tk.PhotoImage(file = "./images/right.png")
        self.wrong_img = tk.PhotoImage(file = "./images/wrong.png")

        #Right Button
        self.right_but = tk.Button(image = self.right_img,command = self.is_known, highlightthickness = 0)
        self.right_but.grid(row = 1, column = 0)

        #Wrong Button
        self.wrong_but = tk.Button(image = self.wrong_img,command = self.is_not_known, highlightthickness = 0)
        self.wrong_but.grid(row = 1, column = 1)







    # Class Methods # 

    def next_card(self):

        

        self.master.after_cancel(self.flip_timer_id)      

        self.current_card = random.choice(self.to_learn)
        self.canvas.itemconfig(self.card_title, text = "French", fill = "black")
        self.canvas.itemconfig(self.card_text, text = self.current_card["French"],fill = "black")
        self.canvas.itemconfigure(self.bg, image = self.card_front)

        self.countdown(3)

        #Create new timer id
        self.flip_timer_id = self.master.after(3000,self.flip_card)

    
    def flip_card(self):

        #Image
        self.card_back = tk.PhotoImage(file = "./images/card_back.png")

        # Display English Side
        self.canvas.itemconfig(self.card_title, text = "English", fill = "white")
        self.canvas.itemconfig(self.card_text, text = self.current_card["English"], fill = "white")
        self.canvas.itemconfig(self.bg,image = self.card_back)
        self.canvas.itemconfig(self.timer_text,text="")


    def is_known(self):

        # Remove known word
        self.to_learn.remove(self.current_card)

        #Update words to learn
        data = pd.DataFrame(self.to_learn)
        data.to_csv("data/words_to_learn.csv")

        self.next_card()


    def is_not_known(self):

        self.master.after_cancel(self.job)
        self.master.after_cancel(self.flip_timer_id) 
        self.flip_card()
        self.master.after(2000,self.next_card)
        


    def countdown(self,count):
        
        #Countdown from count and display count
        if count > 0:
            self.canvas.itemconfig(self.timer_text,text=count)   
            self.job = self.master.after(1000,self.countdown, count - 1)