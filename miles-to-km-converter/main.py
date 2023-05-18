from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
#Set window size
window.minsize(width=300, height=150)
window.config(padx=30,pady=30)

#Miles to km convert function
def convert():
    miles = float(miles_input.get())
    km =  round(miles * 1.609, 2)
    km_calc.config(text = f"{km}")

#Add entry field for miles
miles_input = Entry(width=20)
miles_input.grid(column=1, row=0)


#Label for "Miles"
miles_label= Label(text="Miles", font=("Arial", 14))
miles_label.grid(column=2, row=0)
miles_label.config(padx=10)

#Label for "is equal to"
is_equal_to= Label(text="is equal to", font=("Arial", 14))
is_equal_to.grid(column=0, row=1)
is_equal_to.config(padx=10)

#Label for km_calc
km_calc= Label(text="0", font=("Arial", 14))
km_calc.grid(column=1, row=1)
km_calc.config(padx=10)

#Label for "Kilometers"
km= Label(text="Kilometers", font=("Arial", 14))
km.grid(column=2, row=1)
km.config(padx=10)

#Button
convert_button= Button(text="Convert", font=("Arial", 14), command=(convert))
convert_button.grid(column=1, row=2)


window.mainloop()