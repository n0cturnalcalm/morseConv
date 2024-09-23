## change text to morse:    enter a string. for each character, add morse exchange of them. end of the program generate a mp3 file that morse version of entered text.

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
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
                    '(':'-.--.', ')':'-.--.-'}

INV_MORSE_CODE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}

runTheSilentMorse=True

def encrypt(message):
    encryptedV = ''
    words = message.split(' ')
    for word in words:
        for _character in word:
            encryptedV += MORSE_CODE_DICT[_character] + ' '
        encryptedV += '/ '
    encryptedV = encryptedV[:-3]
    print(encryptedV)

def decrypt(message):
    decryptedV = ''
    words = message.split(' / ')
    for word in words:
        for _symbol in word.split(" "):
            decryptedV += INV_MORSE_CODE_DICT.get(_symbol, '')
        decryptedV += ' '
    decryptedV = decryptedV[:-1]
    print(decryptedV.lower())

while runTheSilentMorse:
    encOrDec = input("select the mode:\n\"encrypt\" or \"decrypt\"\n> ")
    encOrDec = encOrDec.lower()
    if encOrDec == "encrypt":
        enteredText = input("normal text: ")
        encrypt(enteredText.upper())
    elif encOrDec == "decrypt":
        _code = input("enter the code: ")
        decrypt(_code)
    else:
        print("invalid mode")
        continue
    doneOrContinue = input("do you want to continue? (yes/no)\n> ")
    doneOrContinue = doneOrContinue.lower()
    if doneOrContinue == "no":
        runTheSilentMorse = False
        print("goodbye!")
    elif doneOrContinue == "yes":
        continue
    else:
        print("invalid input. we will continue.")
        continue