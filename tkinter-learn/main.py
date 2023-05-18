from tkinter import *

#Create a window
window = Tk()
#Set title of window
window.title("First GUI")
#Set window dimensions
window.minsize(width=500, height=300)
#Add padding to window
window.config(padx=20, pady=20)

#Create Label
label_1= Label(text="New Text", font=("Arial", 24))
#Make label appear on the window using 'grid'
label_1.grid(column=0, row=0)
label_1.config(padx=20, pady=20)

#Function to listen for button click
def button_click():
    new_text = input.get()
    label_1.config(text=new_text)


#Create button
button = Button(text="Don't click", command=button_click)
button.grid(column=1, row=1)

#New Button
button_2 = Button(text="This is the new button")
button_2.grid(column=2, row=0)


#Create Input Field
input = Entry(width=10)
input.grid(column=3, row=3)


#This line will make the window appear indefinitely
window.mainloop()