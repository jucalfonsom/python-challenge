"""
This program solves the challenge of: http://www.pythonchallenge.com/pc/def/peak.html
"""

import pickle
import urllib.request


def run():
    # <!-- peak hell sounds familiar ? -->
    URL = 'http://www.pythonchallenge.com/pc/def/banner.p'
    raw_content = urllib.request.urlopen(URL)

    # Use pickle to serialize
    info = pickle.load(raw_content) # List of list of tuples ('char', int)

    for i in info:
        message = ''.join([key * value for key, value in i]) # Get message line by line
        print(message)


if __name__ == '__main__':
    run()
