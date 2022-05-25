"""
This program solves the challenge of: http://www.pythonchallenge.com/pc/def/equality.html
"""

import re


def run():
    message = ''
    with open('./data/message_3.txt', 'r') as f:
        message = f.read()
    
    # Regex for: One small letter, surrounded by <b>EXACTLY</b> three big bodyguards on each of its sides.
    pattern = re.compile(r'[a-z]{1}[A-Z]{3}([a-z]{1})[A-Z]{3}[a-z]{1}')
    matches = re.findall(pattern, message)

    message_uncrypted = ''.join(matches)

    print(message_uncrypted)


if __name__ == '__main__':
    run()