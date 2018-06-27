#/usr/bin/python

#import urllib2
import sys
import urllib
import os
from bs4 import BeautifulSoup

def download_file(download_url):
    print(download_url)
    try:
        pdfdata = urllib.request.urlopen(download_url)
        datainfile = pdfdata.read()
        filename = download_url.rsplit('/',1)[-1]
        print(filename)

        with open (str(filename), 'wb') as f:
            f.write(datainfile)

    except urllib.error.HTTPError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
        print('HTTP Error')


def process_pdfs(url):
    #asssign url to internal variable
    my_url = url
    #print("The URL you are trying to process is:" + my_url)
    html=urllib.request.urlopen(my_url)
    tags = BeautifulSoup(html, 'html.parser')
    current_link = ''
    for link in tags.find_all('a'):
        current_link = link.get('href')
        #print(str(current_link))
        if str(current_link).endswith('.pdf') == True:
            #print(' pdf: ' + str(current_link))
            download_file(current_link)


if __name__ == '__main__':
    process_pdfs(sys.argv[1]) 
