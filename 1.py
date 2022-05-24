"""
This program solves the challenge of: http://www.pythonchallenge.com/pc/def/map.html
"""

from curses.ascii import isalpha
from hashlib import new


def decoding(message):
    message_uncrypted = ''
    for letter in message:
        if  isalpha(letter):
            letter_char = int(ord(letter))
            new_letter_char = letter_char + 2
            if new_letter_char > 122:
                new_letter_char = (new_letter_char - 123) + int(ord('a'))

            letter = chr(new_letter_char)

        message_uncrypted = message_uncrypted + letter
    
    return message_uncrypted


def run():
    MESSAGE = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    message_unencrypted = decoding(MESSAGE)
    print(message_unencrypted)

    print('-' * 40)
    
    url_unencrypted = decoding("map") # http://www.pythonchallenge.com/pc/def/ocr.html
    print(url_unencrypted)


if __name__ == '__main__':
    run()
