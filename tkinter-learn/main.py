from tkinter import *

#Create a window
window = Tk()
#Set title of window
window.title("First GUI")
#Set window dimensions
window.minsize(width=500, height=300)

#Create Label
label_1= Label(text="This is my first label", font=("Arial", 24))
#Make label appear on the window
label_1.pack()

#Function to listen for button click
def button_click():
    new_text = input.get()
    label_1.config(text=new_text)


#Create button
button = Button(text="Don't click", command=button_click)
button.pack()

#Create Input Field
input = Entry(width=10)
input.pack()
#Get the input 



#This line will make the window appear indefinitely
window.mainloop()