import codecs


def decoding(text2):
    decoded_text = codecs.decode(text2, encoding="rot13", errors='strict')
    print("Decrypted Message -> ", decoded_text)


def encoding():
    text = input("Your message to encode -> ")
    encoded_text = codecs.encode(text, encoding="rot13", errors='strict')
    print("Encrypted Message -> ", encoded_text)
    x = input("Do you want to decode your text -> (Yes or No) ")
    if x == "yes" or x == "Yes":
        decoding(encoded_text)
    else:
        print("Thank you for using ROT-13 Encryption Program :)")
        exit()


encoding()
