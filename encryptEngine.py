import base64

def randomText():
    return "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."


def enterPassword():
    return "SummerBeavers"

def enterCode():
    return encryptText()

def encryptText():
    randomtext = randomText()
    randompass = enterPassword()
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
    print ('OG TEXT BIN: ' + textBinary)
    print ('PASS BIN: ' + passBinary)
    print("XOR BIN: " + bin_str)
    print( 'HEX STR BIN: ' + hex_str)
    hex_byte = bytes.fromhex(hex_str)
    encoded_data = base64.b64encode(hex_byte)
    print('ENCODED BIN: ', encoded_data)
    return encoded_data

    
def decryptText(enc_Base64):    
    password = enterPassword()
    codedText = enterCode()
    hex_str = ''
    decoded_data_bin = ''
    final_text = ''
    decoded_data = base64.b64decode(enc_Base64)
    # num = bin(int.from_bytes(decoded_data, byteorder='big'))
    # print(num)
    lengthxor = len(decoded_data)

    for my_byte in range(0, lengthxor):
        print(f'{decoded_data[my_byte]:0>8b}', end=' ')
        j = my_byte % len(password)
        new = decoded_data[my_byte] ^ ord(password[j])
        final_text += chr(new) 
    print(final_text)
        







def main():
    data = encryptText()
    decryptText(data)




















if __name__ == "__main__":
    main()