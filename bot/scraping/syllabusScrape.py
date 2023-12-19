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
    branch_href = [branch.web_element.get_attribute('href') for branch in branches]
    b = {'CSE','ECE','IT','EEE','ME'}
    for i,branch in enumerate(branch_list):
            z = ""
            for item in b:
                if item in branch:
                    z = item
            data.append(('R18',year,z,branch,branch_href[i]))
    s = find_all(S('#intro > section > nav1 > span > a:nth-child(3)'))[0].web_element
    print(s)
    click(s)

kill_browser()
pqp = pd.DataFrame.from_records(data,columns=['Regulation','Year','Branch','branch_n','Link'])
print(pqp)
pqp.to_excel('Syllabus(list).xlsx')