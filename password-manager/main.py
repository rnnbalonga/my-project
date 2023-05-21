from tkinter import *


#------------- SAVE PASSWORD -------------#

def save():
    """
    Save user input into a text file.
    """
    website = website_input.get()
    email_username = email_username_input.get()
    password = password_input.get()
    
    with open("data.txt", "a") as f:
        f.write(f"\n{website} | {email_username} | {password}")
        f.close()

    website_input.delete(0, 'end')          
    password_input.delete(0, 'end')
    website_input.insert(0, "")         

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

#Generate Password
gen_pass_button= Button(text="Generate Password", font=("Arial", 10))
gen_pass_button.grid(column=2, row=3, sticky="EW")
gen_pass_button.config(padx=10)

#Add Password
add_pass_button= Button(text="Add", font=("Arial", 10), width=35, command=save)
add_pass_button.grid(column=1, row=5, columnspan=2, sticky="EW")


window.mainloop()