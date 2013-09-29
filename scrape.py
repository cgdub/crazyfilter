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


            

        
               

#print strip_tags(parse_soup(grab_html('YAP'), 'YAP'))


