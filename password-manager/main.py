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
email_username = Label()
email_username.config(text="Email/Username:", font=("Arial", 10))
email_username.pack()

#Password
password = Label()
password.config(text="Password:", font=("Arial", 10))
password.pack()


window.mainloop()