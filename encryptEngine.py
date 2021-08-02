import base64

def randomText():
    return "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."


def enterPassword():
    return "SummerBeavers"

def enterCode():
    return encryptText()

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
        





def main():
    data = encryptText()
    decryptText(data)






if __name__ == "__main__":
    main()