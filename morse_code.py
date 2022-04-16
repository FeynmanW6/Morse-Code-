
answer = input("Do you wish to encode or decode? ")

dic = { 'A':'.-', 'B':'-...',
        'C':'-.-.', 'D':'-..', 'E':'.',
        'F':'..-.', 'G':'--.', 'H':'....',
        'I':'..', 'J':'.---', 'K':'-.-',
        'L':'.-..', 'M':'--', 'N':'-.',
        'O':'---', 'P':'.--.', 'Q':'--.-',
        'R':'.-.', 'S':'...', 'T':'-',
        'U':'..-', 'V':'...-', 'W':'.--',
        'X':'-..-', 'Y':'-.--', 'Z':'--..',
        '1':'.----', '2':'..---', '3':'...--',
        '4':'....-', '5':'.....', '6':'-....',
        '7':'--...', '8':'---..', '9':'----.',
        '0':'-----', ', ':'--..--', '.':'.-.-.-',
        '?':'..--..', '/':'-..-.', '-':'-....-',
        '(':'-.--.', ')':'-.--.-' , ' ' :'|'}

dic_reverse = {v: k for k, v in dic.items()}

def encode():

    txt = input("Insert message: ")
    for char in txt:
        print(dic[char.upper()], end = '|')
    print()

def decode():

    txt = input("Insert message: ")
    for char in txt.split():
        print(dic_reverse[char], end = '')
    

if answer == "encode":
    encode()
elif answer == "decode":
    decode()
else:
    print("Your input was not recognized.")