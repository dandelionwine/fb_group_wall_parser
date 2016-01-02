from bs4 import BeautifulSoup
from urllib2 import urlopen
import time

def check(item):
    try:
        html_doc = urlopen(item).read()
        soup = BeautifulSoup(html_doc, "html.parser")
        for j in soup.findAll('td', {"class": "a-color-price"}):  # find the pattern
            if "0.00" in j.contents[0]:  # if there is no price that equals zero, remove the items from the list
                return True
            else:
                return False
    except:
        pass



# def check(item):
#     attempts = 0
#     for i in range(20):
#         try:
#             print i
#             html_doc = urlopen(item).read()
#             soup = BeautifulSoup(html_doc, "html.parser")  # parse the page
#
#             for j in soup.findAll('td', {"class": "a-color-price"}):  # find the pattern
#                 if "0.00" in j.contents[0]:  # if there is no price that equals zero, remove the items from the list
#                     print "True"
#                 else:
#                     print "False"
#         except:
#             print "Attempt unsuccessful"
#             attempts = attempts + 1
#         finally:
#             print attempts, "unsuccessful attempts."


