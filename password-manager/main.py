from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

#------------- PASSWORD GENERATOR -------------#

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(letters) for _ in range(nr_symbols)]
    password_numbers = [choice(letters) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


#------------- SAVE PASSWORD -------------#

def save():
    """
    Save user input into a text file.
    """
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password
        }
                }
    if website == "" or email_username == "" or password == "":
        messagebox.showerror(title="Empty Field", message="Please fill out all the fields.")

    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                #Reading old data
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent= 4)
        else:
                #Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as f:
                    json.dump(new_data, f, indent= 4)   

        finally:
            website_input.delete(0, 'end')          
            password_input.delete(0, 'end')
            website_input.insert(0, "")  

def find_password():
    """
    Search for existing username & password in database
    """       
    website = website_input.get()

    if website == "":
        messagebox.showerror(title="Empty Field", message="Please fill out website.")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                messagebox.showinfo(title="Password", message=f"Email/Username: {data[website]['email']} \nPassword: {data[website]['password']}")
        except:
            messagebox.showerror(title="No Data", message="You don't have a saved password for this website.")
            
#------------- GUI -------------#

#WINDOW
window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

#CANVAS
canvas = Canvas(width=210, height=210, highlightthickness=0)
#Add image to canvas
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#TEXT LABELS

#Website
website_text = Label()
website_text.config(text="Website:", font=("Arial", 10))
website_text.grid(column=0, row=1)

#Email/username
email_username_text = Label()
email_username_text.config(text="Email/Username:", font=("Arial", 10))
email_username_text.grid(column=0, row=2)

#Password
password_text = Label()
password_text.config(text="Password:", font=("Arial", 10))
password_text.grid(column=0, row=3)

#INPUT FIELDS

#Website input
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
website_input.focus()

#Email/username input
email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2, sticky="EW")
email_username_input.insert(0, "rnnbalongapro@gmail.com")

#Password input
password_input = Entry()
password_input.grid(column=1, row=3, sticky="EW")

#BUTTON

#Search Website
search_website_button= Button(text="Search", font=("Arial", 10), command=find_password)
search_website_button.grid(column=2, row=1, sticky="EW")
search_website_button.config(padx=10)


#Generate Password
gen_pass_button= Button(text="Generate Password", font=("Arial", 10), command=generate_password)
gen_pass_button.grid(column=2, row=3, sticky="EW")
gen_pass_button.config(padx=10)

#Add Password
add_pass_button= Button(text="Add", font=("Arial", 10), width=35, command=save)
add_pass_button.grid(column=1, row=5, columnspan=2, sticky="EW")


window.mainloop()