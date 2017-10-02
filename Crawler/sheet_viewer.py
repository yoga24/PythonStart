from splinter import Browser
import time

# Replace <<GDRIVE_FOLDER_URL>>, <<USER_MAIL>>, <<USER_MAIL>> with appropriate values.
# This pgm will goto the provided GoogleDrive URL and display the name of all its contents

DRIVE_FLDR_LINK = '<<GDRIVE_FOLDER_URL>>'

browser = Browser('chrome')
browser.visit(DRIVE_FLDR_LINK)

if 'accounts.google.com/signin' in browser.url:
    user = browser.find_by_xpath('//*[@id="identifierId"]')[0]
    user_next = browser.find_by_xpath('//*[@id="identifierNext"]')[0]
    user.fill('<<USER_MAIL>>')
    user_next.click()

    time.sleep(5)  # To make sure all elements are loaded before searching using XPath
    pwd = browser.find_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')[0]
    pwd_next = browser.find_by_xpath('//*[@id="passwordNext"]')[0]

    pwd.fill('<<PASSWORD>>')
    pwd_next.click()

folder_items = browser.find_by_xpath('//span[@class="l-Ab-T-r"]')
for item in folder_items:
    print(item.text)
