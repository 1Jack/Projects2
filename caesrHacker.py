# Caeser Cipher Hacker
# http://inventwithpython.com/hacking (BSD Licensed) 

message = 'GUVF VF ZL FRERG ZRFFNTR.'
LETTERS = 'ABCEDFGHIJKLMNOPQRSTUVWXYZ'

# loop through every possible key
for key in range(len(LETTERS)):

# It is important to ser tranlated to the blank string so that the
# previous iteration's value for translated is cleared.

    translated = ''

# The rest of the program is the same as the original Caeser program:

# run the encryption / decryption code on each symbol in the message
for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)  # get the number of the symbol
        num = num - key
        # handle the wrap around if num is 26 0r larger or less than 0
        if num < 0:
            num = num + len(LETTERS)

            # add number's symbol at the end of translated
    translated = translated + LETTERS[num]

else:
    # just add the symbol without encrpting / decrypting
    translated = translated + symbol

            # display the current key being tested, along with its decrypyion
print ('Key #%s: %s' % (key, translated)) 

