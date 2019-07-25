from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
import re
import urllib
import string

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
#        print("Start tag:", tag)
        for attr in attrs:
#            print("     attr[0]:", attr[0])
#            print("     attr[1]:", attr[1])
            if attr[0] == 'href':
#                print(attr[1])
                match = re.search(r'http://.*\.mp3$', attr[1], re.I)
                if match:
#                    print(attr[1])
                    filename = attr[1].split('/')[-1]
                    str = ""
                    for char in filename.lower():
                        if char in string.ascii_lowercase:
                            str += char
                        else:
                            str += " "
                    str = str[:-20]
                    str = str + ".mp3"
                    print str.replace(' ','')
                
                    download = urllib.URLopener()
                    download.retrieve(attr[1],filename)
    

parser = MyHTMLParser()
parser.feed(open('kj.html').read())
parser.close()
