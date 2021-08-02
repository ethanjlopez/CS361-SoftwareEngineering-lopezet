from encryptEngine import *
from tkinter import * 
from tkinter import ttk
import requests

root = Tk()
root.title("Encryption Program")


canvas = Frame(root, width=800, height=800)
canvas.grid(columnspan=2, rowspan=3)

#frames
tabSection = Frame(canvas)
tabSection.grid(column=1, row=0, sticky=NW)

upperContent = Frame(canvas)
upperContent.grid(column=0, row=0)

middleContent = Frame(canvas)
middleContent.grid(column=0, row=1)

lowerContent = Frame(canvas)
lowerContent.grid(column=0, row=2)

upperSideContent = Frame(canvas)
upperSideContent.grid(column=1, row=0)

lowerSideContent = Frame(canvas)
lowerSideContent.grid(column=1, row=2)

#instructions
instructions = Label(upperContent, text="Please enter text to encryp/decrypt: ")
instructions.grid(column=0, row=0, sticky= W)

secondInstructions = Label(lowerContent, text="This is your Encrypted / Decrypted Text: ")
secondInstructions.grid(column=0, row=0, sticky= W)

#text
textfield = Text(upperContent, height = 10, width = 60)
textfield.grid(column=0, row=1)

secondField = Text(lowerContent, height= 10, width = 60)
secondField.grid(column=0, row=1)

passEntry = ttk.Entry(middleContent)
passEntry.grid(column=0, row=0)

#button
cpyBttn = Button(upperSideContent, text='Copy' , command= lambda: copyField(textfield))
cpyBttn.grid(column=1, row=1)

clrBttn = Button(upperSideContent, text='Clear', command= lambda: clearField(textfield))
clrBttn.grid(column=2, row=1)

randomTxtBttn = Button(upperSideContent, text='Random Text', command= lambda: randomTextCall())
randomTxtBttn.grid(column=1, row=0, columnspan=2)

encryptBttn = Button(middleContent, text='Encrypt', command= lambda: encryptTextfield())
encryptBttn.grid(column=2, row=0)

decryptBttn = Button(middleContent, text='Decrypt', command= lambda: decryptTextField())
decryptBttn.grid(column=3, row=0)

cpyBttn2 = Button(lowerSideContent, text='Copy', command= lambda: copyField(secondField) )
cpyBttn2.grid(column=1, row=1)

clrBttn2 = Button(lowerSideContent, text='Clear', command= lambda: clearField(secondField))
clrBttn2.grid(column=2, row=1)



#notebook

# tabs = ttk.Notebook(canvas)
# tabs.add(upperContent, text='One')





#commands

def randomTextCall():
    textfield.delete('1.0', 'end-1c')
    rndmText = requests.get('https://randomtextgenerator20210726144542.azurewebsites.net/TextGenerator')
    inputValue = rndmText.json()
    textfield.insert("1.0", inputValue['content'])

def encryptTextfield():
    inputValue = textfield.get("1.0", "end-1c")
    passValue = passEntry.get()
    secondField.delete('1.0', 'end-1c')
    secondField.insert('1.0', encryptText(inputValue, passValue))


def decryptTextField():
    inputValue = textfield.get("1.0", "end-1c")
    passValue = passEntry.get()
    secondField.delete('1.0', 'end-1c')
    secondField.insert('1.0', decryptText(inputValue, passValue))


def clearField(field):
    field.delete("1.0", "end-1c")

def copyField(field):
    data = field.get("1.0", "end-1c")
    root.clipboard_clear()
    root.clipboard_append(data)


root.mainloop()

