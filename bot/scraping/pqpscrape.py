from helium import *
from bs4 import BeautifulSoup
import pandas as pd

data = []
br = start_chrome("https://studentservices.jntuh.ac.in")
click('Previous Question Papers')
click('Btech')
regulation = ['R18']
for reg in regulation:
    click(reg)
    print(reg)
    semesters = find_all(S("#intro > section > nav1 > p > a"))
    sem_list = [sem.web_element.text for sem in semesters]

    for sem in sem_list:
        print(sem)
        click(sem)
        branches = find_all(S("#intro > section > nav1 > p > a"))
        branch_list = [branch.web_element.text for branch in branches]

        for branch in branch_list:
            if branch in ['CSE','ECE','IT','EEE','ME']:
                print(branch)
                click(Link(branch))

                subjects = find_all(S("#intro > section > nav1 > p > a"))
                subject_list = [subject.web_element.text for subject in subjects]

                for subject in subject_list:
                    try:
                        print("     ",subject)
                        click(Link(subject))

                        paperlinks = find_all(S("#intro > section > nav1 > p > a"))
                        for paper in paperlinks:
                            data.append(('R18',sem,branch,subject,paper.web_element.text,paper.web_element.get_attribute('href')))
                            print("         ",paper.web_element.text,paper.web_element.get_attribute('href'))
                        
                        click(Link(branch))
                    except:
                        print('error')

                click(Link(sem))

        click(Link(reg))
    click('Btech')
    break
kill_browser()

pqp = pd.DataFrame.from_records(data,columns=['Regulation','Semester','Branch','Subject','Year','Link'])
print(pqp)
pqp.to_excel('PQP(list).xlsx')