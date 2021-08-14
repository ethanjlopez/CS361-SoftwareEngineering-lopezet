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
        

def encryptImage(path, key):
    
    fin = open(path, 'rb')
     

    image = fin.read()
    fin.close()
     
    # converting image into byte array to
    # perform encryption easily on numeric data
    image = bytearray(image)
    
    # performing XOR operation on each value of bytearray
    for index, values in enumerate(image):
        j = index % len(key)
        image[index] = values ^ ord(key[j])
 
    # opening file for writing purpose
    fin = open(path, 'wb')
     
    # writing encrypted data in image
    fin.write(image)

    fin.close()
    return True
 
def decryptImage(path, key):

    fin = open(path, 'rb')

    image = fin.read()
    fin.close()
     
    # converting image into byte array to perform decryption easily on numeric data
    image = bytearray(image)
 
    # performing XOR operation on each value of bytearray
    for index, values in enumerate(image):
        j = index % len(key)
        image[index] = values ^ ord(key[j])
 
    # opening file for writing purpose
    fin = open(path, 'wb')
     
    # writing decryption data in image
    fin.write(image)
    fin.close()
    return True

def main():
    decryptImage('G:\Files\Pictures\\13_02_sadies\\3535_10200126919230253_1664104074_n_10200126919230253.jpg', 22)



if __name__ == "__main__":
    main()