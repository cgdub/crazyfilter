import urllib2
from HTMLParser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def grab_html(acronym):
	'''input acronym to find, returns list of strings
	of possible definitions'''
	req = urllib2.urlopen("http://www.acronymfinder.com/" + acronym + ".html")
	return req.read()

def parse_soup(clean_html, acronym):
    add = 0
    for i in clean_html:
        if i == '*'
            add = 1
        

            

        
               

print strip_tags(parse_soup(grab_html('YAP'), 'YAP'))


