import base64
from PIL import Image
import math

def encryptText(text, password):
    randomtext = text
    randompass = password
    hex_str = ''
    bin_str = ''
    lengthText = len(randomtext)
    lengthKey = len(randompass)

    for i in range (0, lengthText):
        j = i % lengthKey

        letterB = ord(randomtext[i])
        passB = ord(randompass[j])

        test = passB ^ letterB
        bin_str += format(test, '08b') + ' '
        hex_str += '{:02x}'.format(test)        
    

    textBinary = ' '.join(format(ord(x), 'b') for x in randomtext)
    passBinary = ' '.join(format(ord(x), 'b') for x in randompass)
    hex_byte = bytes.fromhex(hex_str)
    encoded_data = base64.b64encode(hex_byte)
    return encoded_data

    
def decryptText(data, password):    
    hex_str = ''
    decoded_data_bin = ''
    final_text = ''
    decoded_data = base64.b64decode(data)
    # num = bin(int.from_bytes(decoded_data, byteorder='big'))
    # print(num)
    lengthxor = len(decoded_data)

    for my_byte in range(0, lengthxor):
        j = my_byte % len(password)
        new = decoded_data[my_byte] ^ ord(password[j])
        final_text += chr(new) 
    return final_text
        

def encryptImage(path):
     # take path of image as a input
  
     
    # taking encryption key as input

    # print path of image file and encryption key that
    # we are using
    print('The path of file : ', path)
    print('Key for encryption : ', 22)
     
    # open file for reading purpose
    fin = open(path, 'rb')
     
    # storing image data in variable "image"
    image = fin.read()
    fin.close()
     
    # converting image into byte array to
    # perform encryption easily on numeric data
    image = bytearray(image)
    
    # performing XOR operation on each value of bytearray
    for index, values in enumerate(image):
        image[index] = values ^ 22
 
    # opening file for writing purpose
    fin = open(path, 'wb')
     
    # writing encrypted data in image
    fin.write(image)

    fin.close()
    print('Encryption Done...')
 
def decryptImage(path):
     # take path of image as a input
     
    # taking decryption key as input
    key = int(input('Enter Key for encryption of Image : '))
     
    # print path of image file and decryption key that we are using
    print('The path of file : ', path)
    print('Note : Encryption key and Decryption key must be same.')
    print('Key for Decryption : ', key)
     
    # open file for reading purpose
    fin = open(path, 'rb')
     
    # storing image data in variable "image"
    image = fin.read()
    fin.close()
     
    # converting image into byte array to perform decryption easily on numeric data
    image = bytearray(image)
 
    # performing XOR operation on each value of bytearray
    for index, values in enumerate(image):
        image[index] = values ^ key
 
    # opening file for writing purpose
    fin = open(path, 'wb')
     
    # writing decryption data in image
    fin.write(image)
    fin.close()
    print('Decryption Done...')

def main():
    encryptImage(22)



if __name__ == "__main__":
    main()