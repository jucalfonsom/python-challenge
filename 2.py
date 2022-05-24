"""
This program solves the challenge of: http://www.pythonchallenge.com/pc/def/ocr.html
"""

import string


def run():
    message = ''
    with open('./data/message_2.txt', 'r') as f:
        message = f.read()
    
    letters_message = [letter for letter in message if letter in string.ascii_letters]
    message_uncrypted = ''.join(letters_message)
    
    print(message_uncrypted)


if __name__ == '__main__':
    run()
