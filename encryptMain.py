from encryptEngine import *
from tkinter import * 
from tkinter import ttk
import requests
from tkinter import messagebox
from tkinter import filedialog
from PIL import ImageTk, Image, UnidentifiedImageError
import urllib

root = Tk()
root.title("Encryption Program")


style = ttk.Style(root)
style.configure('lefttab.TNotebook', tabposition='ne')
tabs = ttk.Notebook(root, style='lefttab.TNotebook')
tabs.grid()

canvas = Frame(tabs)
canvas2 = Frame(tabs)


canvas.grid(columnspan = 2, rowspan = 3)

tabs.add(canvas, text="Text")
tabs.add(canvas2, text="Image")


#frames

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
titleLabel = Label(canvas2, text= "Choose an Image that you wish to encrypt: ")
titleLabel.grid(column=0, row=0)

imageContent = Frame(canvas2, width=350, height=350)
imageContent.grid(column=0,row=1)

imageSide = Frame(canvas2)
imageSide.grid(column=2, row=1)

newFrame = Frame(canvas2)
newFrame.grid(column=0, row=1)

imagePanel = Label(newFrame, text="Please Upload an Image")
imagePanel.grid()

imageEtryLbl = Label(canvas2, text="Password:")
imageEtryLbl.grid(column=1, row=2)
imageEntry = ttk.Entry(canvas2)
imageEntry.grid(column=2, row=2)

upldButton = Button(imageSide, text='Browse', command= lambda: open_img(), width=10)
upldButton.grid(column=0, row=0)

rndmPicButton = Button(imageSide, text='Random', width=10, command=lambda: randomPicture())
rndmPicButton.grid(column=1, row=0)

encryptImgButton = Button(imageSide, text='Encrypt', width=10, command= lambda: encrypt_decrypt_image(encryptImage))
encryptImgButton.grid(column=0, row=2)

decryptImgButton = Button(imageSide, text='Decrypt', width=10, command= lambda: encrypt_decrypt_image(decryptImage))
decryptImgButton.grid(column=1, row=2)

saveImageButton = Button(imageSide, text='Save As...', width=20, command= lambda: save_img(save_img()))
saveImageButton.grid(column=0, row=1, columnspan=2)

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
    """Makes a GET Request to an image scraper and populates the image field with a random image."""
    rndmImage = requests.get('https://imagescraperapi.herokuapp.com/?url=https://en.wikipedia.org/wiki/Beaver')
    inputValue = rndmImage.json()
    img = inputValue['image-url']
   
    with urllib.request.urlopen('https://' + img[2:]) as url:
        with open('temp.jpg', 'wb') as f:
            f.write(url.read())
    
    randomImg = Image.open('temp.jpg')
    global randomB
    randomB = randomImg
    randomImg = img.resize((300,300), Image.ANTIALIAS)
    randomImg = ImageTk.PhotoImage(randomImg)
    imagePanel.configure(image=randomImg)
    imagePanel.image = randomImg
    return  

def encrypt_decrypt_image(service):
    if service == encryptImage:
        if encryptImage(filename, imageEntry.get()) == True:
            imagePanel.configure(image='')
            imagePanel.configure(text="Encryption of Image was Successful!")
    elif service == decryptImage:
        if decryptImage(filename, imageEntry.get()) == True:
            img = Image.open(filename)
            img = img.resize((300, 300), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            imagePanel.configure(image=img)
            imagePanel.image = img
            
def open_img():
    """Upload's an image from the user's local files then populates that image into the GUI."""
    x = UploadAction()
    try:
        uploadedImage = Image.open(x)
        uploadedImage = uploadedImage.resize((300, 300), Image.ANTIALIAS)
        uploadedImage = ImageTk.PhotoImage(uploadedImage)
        imagePanel.configure(image=uploadedImage)
        imagePanel.image = uploadedImage
    except UnidentifiedImageError:
        imagePanel.configure(image='')
        imagePanel.configure(text='Upload of Encrypted File was Successful!')

def save_img():
    image = Image.open("temp.jpg")
    photo = ImageTk.PhotoImage(image)
    filedialog.asksaveasfilename(initialdir="/", title="Select file", filetypes=(
        ('JPEG', ('*.jpg', '*.jpeg', '*.jpe')), ('PNG', '*.png'), ('BMP', ('*.bmp', '*.jdib')), ('GIF', '*.gif')))
    photo.save()

root.mainloop()

