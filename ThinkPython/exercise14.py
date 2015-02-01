#!/usr/bin/python

def print_secret_message():
    import urllib

    conn = urllib.urlopen('http://thinkpython.com/secret.html')

    for line in conn:
        print line.strip()

def get_zip_info(zipcode):
    import urllib

    url = 'http://www.uszip.com/zip/' + str(zipcode)

    conn = urllib.urlopen(url)

    for line in conn:
        if line.strip()

if __name__ == '__main__':

    get_zip_info(80126)