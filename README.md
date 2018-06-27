# pullpdfs
I neede a quick parser to download pdfs. Short, sweet and quick.

## Prerequisites
Beautiful soup

```Python
pip install beautifulsoup4
```

## How to use

For this program, you simply pass the url that contains the pdfs you are searching for. 
The program using beautiful soup searches the html for <a> tags. Then sends the a tags
through a download function that uses the urllib package to request the urls. There is
Some error catching but it is limited.
```Python
Python pullpdf.py #URL_AS_Parameter
```


