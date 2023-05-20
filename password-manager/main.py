from tkinter import *

#WINDOW
window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

#CANVAS
canvas = Canvas(width=210, height=210, highlightthickness=0)
#Add image to canvas
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()

#TEXT LABELS

#Website
website_text = Label()
website_text.config(text="Website:", font=("Arial", 10))
website_text.pack()

#Email/username
email_username_text = Label()
email_username_text.config(text="Email/Username:", font=("Arial", 10))
email_username_text.pack()

#Password
password_text = Label()
password_text.config(text="Password:", font=("Arial", 10))
password_text.pack()

#INPUT FIELDS

#Website input
website_input = Entry(width=35)
website_input.pack()

#Email/username input
email_username_input = Entry(width=35)
email_username_input.pack()

#Password input
password_input = Entry(width=21)
password_input.pack()

#BUTTON

#Generate Password
gen_pass_button= Button(text="Generate Password", font=("Arial", 10))
gen_pass_button.pack()

#Add Password
add_pass_button= Button(text="Add Password", font=("Arial", 10), width=36)
add_pass_button.pack()

window.mainloop()