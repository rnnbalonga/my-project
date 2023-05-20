from tkinter import *

#Window
window = Tk()
window.config(padx=20, pady=20)
window.title("Password Manager")

#Canvas
canvas = Canvas(width=210, height=210, highlightthickness=0)
#Add image to canvas
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.pack()

window.mainloop()