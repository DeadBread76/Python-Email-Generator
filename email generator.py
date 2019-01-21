import pyperclip
import os
from selenium import webdriver


while 1<5:
    driver = webdriver.Chrome()
    driver.get("https://emailfake.com/")
    button = driver.find_element_by_id('copbtn')
    button.click()

    s = pyperclip.paste() 
    with open('emails.txt','a') as g:
     g.write(s +  '\n')           

    driver.close()
    os.system("TASKKILL /F /IM chromedriver.exe")
    print(s)



