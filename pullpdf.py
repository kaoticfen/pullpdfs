#/usr/bin/python

#import urllib2
import sys
import urllib.request
from bs4 import BeautifulSoup

def process_pdfs(url):
    #asssign url to internal variable
    my_url = url
    print("The URL you are trying to process is:" + my_url)
    html=urllib.request.urlopen(my_url).read()
    sopa = BeautifulSoup(html)
    current_link = ''
    for link in sopa.find_all('a'):
        current_link = link.get('href')
        if current_link.endswith('pdf'):
            print(' pdf: ' + current_link)


if __name__ == '__main__':
    process_pdfs(sys.argv[1]) 
