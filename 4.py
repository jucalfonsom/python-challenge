"""
This program solves the challenge of: http://www.pythonchallenge.com/pc/def/linkedlist.php
"""

import urllib.request


def url_request(url):
    with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
    
    return content

def get_info(NOTHING_START, url, content):
    while NOTHING_START in content:
        nothing_id = content.split(NOTHING_START)[1].strip()
        content = url_request(url + nothing_id)
        # print(nothing_id)
    
    return content, nothing_id

def run():
    # <!-- urllib may help. DON'T TRY ALL NOTHINGS, since it will never end. 400 times is more than enough. -->

    # Get origin pate

    url_origin = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
    page_origin = url_request(url_origin)
    nothing_id = page_origin.split('nothing=')[1].split('"')[0]

    # Get multiple nothing
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    NOTHING_START = 'nothing is'

    # print(nothing_id)
    content = url_request(url + nothing_id)

    content, nothing_id = get_info(NOTHING_START, url, content)  
    print(f'Nothing id: {nothing_id} - Content: {content}') # Yes. Divide by two and keep going.

    nothing_id = str(int(nothing_id) / 2)
    content = url_request(url + nothing_id)
    content, nothing_id = get_info(NOTHING_START, url, content)  
    print(f'Nothing id: {nothing_id} - Content: {content}') # peak.html


if __name__ == '__main__':
    run()
