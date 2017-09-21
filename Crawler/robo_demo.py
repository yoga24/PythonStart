from robobrowser import RoboBrowser
import re

browser = RoboBrowser(parser='html.parser')
browser.open('http://ww2.readsnk.com/')

chapterList = browser.find_all('a')

for chapter in chapterList:
    if '97' in chapter['href']:
        print(chapter.text, "Chap 97 Link", chapter['href'])
        print('----------------------')

# print(chapterList[0])
# browser.follow_link('Shingeki No Kyojin Chapter 097')
#
# titleTag = browser.find('chapter__title')
# print(titleTag.text())
