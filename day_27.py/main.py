from tkinter import *

windows = Tk()

windows.title("My First GUI Program")
windows.minsize(width=500, height=300)
windows.config(padx=100, pady=200)

#Label

my_label = Label(text="I am a Label", font=("Arial", 24, "italic"))
# my_label.pack()
#sau
# my_label.pack(side="left")
#sau
# my_label.pack()
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#Buttons

def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())
    my_label.grid(column=0, row=0)

button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

#Entry

input = Entry(width=30)
# input.pack()
print(input.get())
# input.pack()
input.grid(column=3, row=2)













windows.mainloop()