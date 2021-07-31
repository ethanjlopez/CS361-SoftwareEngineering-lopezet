from tkinter import * 
from tkinter import ttk

root = Tk()
root.title("Encryption Program")

canvas = Canvas(root, width=800, height=800)
canvas.grid(columnspan=4, rowspan=4)


upperContent = Frame(root)
upperContent.grid(column=0, row=0)

upperSideContent = Frame(root)
upperSideContent.grid(column=1, row=0)

#instructions
instructions = Label(upperContent, text="Please enter text to encryp/decrypt: ")
instructions.grid(column=0, row=0)

#text
textfield = Text(upperContent, height = 10, width = 60)
textfield.grid(column=0, row=1)

#button
clrBttn = Button(upperSideContent, text='Clear')
clrBttn.grid(column=1, row=1)

cpyBttn = Button(upperSideContent, text='Copy')
cpyBttn.grid(column=1, row=2)







root.mainloop()

