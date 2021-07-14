from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
import json

WHITE = "#FFFFFF"





# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pwd():
    options_list = list(string.ascii_lowercase + string.digits + string.punctuation)
    lop = random.randint(8,15)
    pwd_list = [random.choice(options_list) for _ in range(lop)]
    pwd = ''.join(pwd_list)
    pwd_entry.insert(0,pwd)
    pyperclip.copy(pwd)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():

    website = web_entry.get()
    email = eu_entry.get()
    password = pwd_entry.get()
    new_data = {
        website: {
            "email":email,
            "password":password,
        }
    }

    if (len(website) == 0) | (len(password) == 0):
        messagebox.showinfo(title = "oops", message = "Empty fields bro")
    
    else:

        try:
            with open('data.json','r') as data_file:
                data  = json.load(data_file)
        
        except FileNotFoundError:

            with open('data.json','w') as data_file:
                json.dump(new_data,data_file, indent = 4)
        
        else:

            data.update(new_data)

            with open('data.json','w') as data_file:
                json.dump(data,data_file, indent = 4)
        
        finally:
        
            web_entry.delete(0,END)
            pwd_entry.delete(0,END)

# ---------------------------- Search PASSWORD ------------------------------- #

def find_password():
    
    website = web_entry.get()

    if len(website) == 0:
        messagebox.showinfo(title = "oops", message = "Empty fields bro")
    
    else:

        try:
            with open('data.json','r') as data_file:
                data  = json.load(data_file)
        
        except FileNotFoundError:

            messagebox.showinfo(title = "Oops", message = "File not found, you have not entered any passwords yet")

        else:

            websites = data.keys()

            if website in websites:
                
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title = "Found", message = f"Email: {email}\nPassword: {password}")
            
            else: 
                messagebox.showinfo(title = "Not Found", message = f"You dont not have a password for {website}")

      
        finally:
        
            web_entry.delete(0,END)
            pwd_entry.delete(0,END)


    
    

# ---------------------------- UI SETUP ------------------------------- #

# Window 

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50, bg = WHITE)
window.grid_columnconfigure(1,weight = 1)

# Canvas 

canvas = Canvas(width = 200, height = 200, bg = WHITE, highlightthickness = 0)

img = PhotoImage(file = "logo.png")
canvas.create_image(100,100, image = img)
canvas.grid(row = 0, column = 1)

# Create Labels 

web_label = Label(text = "Website: ",anchor="e", bg = WHITE)
web_label.grid(row=1, column = 0,sticky="w")

em_un_label = Label(text = "Email/Username: ", bg = WHITE)
em_un_label.grid(row=2, column = 0)

password_label = Label(text = "Password: ",anchor="e", bg = WHITE)
password_label.grid(row=3, column = 0,sticky="w")

# Create Text Entries 

web_entry = Entry(width = 35)
web_entry.grid(row = 1,column = 1,sticky="nsew")
web_entry.focus()

eu_entry = Entry(width = 35)
eu_entry.grid(row = 2,column = 1, columnspan = 2,sticky="nsew")
eu_entry.insert(0, 'charlesleahan@gmail.com')

pwd_entry = Entry(width = 21)
pwd_entry.grid(row = 3,column = 1,sticky="nsew")


# Add buttons 

gen_pwd = Button(text = "Generate Password",command = generate_pwd, highlightthickness = 0, bg = WHITE)
gen_pwd.grid(row = 3, column = 2)

add_pwd = Button(text = "Add",command = save, highlightthickness = 0,bg = WHITE, width = 36)
add_pwd.grid(row = 4, column = 1, columnspan = 2,sticky="nsew")

search_but = Button(text = "Search",command = find_password, highlightthickness = 0, width = 15, bg = WHITE)
search_but.grid(row = 1, column = 2)























window.mainloop()