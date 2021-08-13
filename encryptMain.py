from encryptEngine import *
from tkinter import * 
from tkinter import ttk
import requests
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image
import urllib
import base64
root = Tk()
root.title("Encryption Program")


style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='ne')
tabs = ttk.Notebook(root, style='lefttab.TNotebook')
tabs.grid(row=0, column=3)

canvas = Frame(tabs)
canvas2 = Frame(tabs)
canvas3 = Frame(tabs)

canvas.grid(columnspan=2, rowspan=3)

tabs.add(canvas, text="Text")
tabs.add(canvas2, text="Image")
tabs.add(canvas3, text='Advanced')

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
instructions = Label(upperContent, text="1. Please enter text to encryp/decrypt: ")
instructions.grid(column=0, row=0, sticky= W)

secondInstructions = Label(lowerContent, text="2. This is your Encrypted / Decrypted Text: ")
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

encryptBttn = Button(middleContent, text='Encrypt', command= lambda: encrypt_decrypt_Textfield(encryptText))
encryptBttn.grid(column=2, row=0)

decryptBttn = Button(middleContent, text='Decrypt', command= lambda: encrypt_decrypt_Textfield(decryptText))
decryptBttn.grid(column=3, row=0)

cpyBttn2 = Button(lowerSideContent, text='Copy', command= lambda: copyField(secondField) )
cpyBttn2.grid(column=1, row=1)

clrBttn2 = Button(lowerSideContent, text='Clear', command= lambda: clearField(secondField))
clrBttn2.grid(column=2, row=1)



#notebook

imageContent = Frame(canvas2)
imageContent.grid(column=0,row=0)

label = Label(imageContent)
label.grid(column=0, row=0)

panelU = Label(imageContent)
panelU.grid(column=0, row=0)

upldButton = Button(imageContent, text='upload', command= lambda: open_img())
upldButton.grid(column=1, row=0)

rndmPicButton = Button(imageContent, text='random', command=lambda: randomPicture())
rndmPicButton.grid(column=2, row=0)

encryptImgButton = Button(imageContent, text='Encrypt', command= lambda: encryptImage(filename))
encryptImgButton.grid(column=3, row=0)

decryptImgButton = Button(imageContent, text='Decrypt', command= lambda: decryptImage(filename))
decryptImgButton.grid(column=4, row=0)

#commands

def randomTextCall():
    textfield.delete('1.0', 'end-1c')
    rndmText = requests.get('https://randomtextgenerator20210726144542.azurewebsites.net/TextGenerator')
    inputValue = rndmText.json()
    textfield.insert("1.0", inputValue['content'])

def encrypt_decrypt_Textfield(mode):
    
    inputValue = textfield.get("1.0", "end-1c")
    passValue = passEntry.get()

    if len(inputValue) == 0 or len(passValue) == 0:
        messagebox.showerror("Input Error", "The Password and Input Text Fields cannot be empty.")

    secondField.delete('1.0', 'end-1c')
    secondField.insert('1.0', mode(inputValue, passValue))


def clearField(field):
    field.delete("1.0", "end-1c")

def copyField(field):
    data = field.get("1.0", "end-1c")
    root.clipboard_clear()
    root.clipboard_append(data)

def UploadAction():
    global filename
    filename = filedialog.askopenfilename()
    return filename

def randomPicture():
    rndmImage = requests.get('https://imagescraperapi.herokuapp.com/?url=https://en.wikipedia.org/wiki/Bluebird')
    inputValue = rndmImage.json()
    img = inputValue['image-url']
    bin_img = urllib.request.urlopen('https://en.wikipedia.org/wiki/Bluebird')
    raw_data = bin_img.read()
    bin_img.close()
    b64_data = base64.encodestring(raw_data)
    image = PhotoImage(data=b64_data)
    panel = Label(imageContent, image=image)
    panel.image = image
    panel.grid(column=0, row=0)


def open_img():
    x = UploadAction()
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panelU.configure(image=img)
    panelU.image = img

root.mainloop()

