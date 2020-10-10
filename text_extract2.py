import sys
from keywordextractor.keywordextractor import Crawler

text2 = """
    Hello! I’m Soumil Nitin Shah, a Software and Hardware Developer based 
    in New York City. I have completed by Bachelor in Electronic Engineering and
    my Double master’s in Computer and Electrical Engineering. I Develop Python Based Cross 
    Platform Desktop Application , Webpages , Software, REST API, Database and much more I 
    have more than 2 Years of Experience in Python
    """
text = 'I want to get a cpu cooler'
d = Crawler(text=text)
data = d.get()
print(data)
print(text)

d = Crawler(text=text)
data = d.get()
print(data)
