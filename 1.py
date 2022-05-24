from curses.ascii import isalpha
from hashlib import new


def run():
    MESSAGE = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

    for letter in MESSAGE:
        if  isalpha(letter):
            letter_char = int(ord(letter))
            new_letter_char = letter_char + 2
            if new_letter_char > 122:
                new_letter_char = (new_letter_char - 123) + int(ord('a'))

            letter = chr(new_letter_char)

        print(letter, end='')
    
    print('')


if __name__ == '__main__':
    run()
