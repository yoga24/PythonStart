from robobrowser import RoboBrowser
import re

browser = RoboBrowser(parser='html.parser')
browser.open('http://ww2.readsnk.com/')

chapterList = browser.find_all('a')
chapter97 = ''

for chapter in chapterList:
    if '099' in chapter['href']:
        chapter97 = chapter#['href']
        break

if chapter97 == '':
    print('No Link found. Exiting :(')
    exit()

browser.follow_link(chapter97)
chapterHead = browser.find('h1', {'class': 'chapter__title'})
print(chapterHead.text)




# print(chapterList[0])
# browser.follow_link('Shingeki No Kyojin Chapter 097')
#
# titleTag = browser.find('chapter__title')
# print(titleTag.text())
