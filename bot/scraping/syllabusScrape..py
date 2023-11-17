from helium import *
from bs4 import BeautifulSoup
import pandas as pd

print("skdjlf")
data = []
br = start_chrome("https://studentservices.jntuh.ac.in")
click('Syllabus')
click('B.Tech')
click('R18')

Years = find_all(S("#intro > section > nav1 > p > a"))
year_list = [sem.web_element.text for sem in Years]

for year in year_list:
    print(year)
    click(year)
    branches = find_all(S("#intro > section > nav1 > p > a"))
    branch_list = [branch.web_element.text for branch in branches]
 
    b = {'CSE','ECE','IT','EEE','ME'}
    a = b.copy()
    for branch in branch_list:
            for item in b:
                  if item in a and item in branch:
                        print(branch)
                        a.discard(item)
    s = find_all(S('#intro > section > nav1 > span > a:nth-child(3)'))[0].web_element
    print(s)
    click(s)

kill_browser()
