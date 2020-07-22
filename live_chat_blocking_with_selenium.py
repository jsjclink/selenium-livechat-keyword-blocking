from selenium import webdriver
import time
from bs4 import BeautifulSoup


def findSpam(input_chat):





driver=webdriver.Chrome('C:\\Users\\jsjcl\\Downloads\\chromedriver_win32\\chromedriver.exe')

driver.implicitly_wait(10)

#########login

driver.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
#driver.maximize_window()
time.sleep(5)
a=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys('jsjclink@naver.com')
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div').click()
# a.submit() it will not work in this login page
time.sleep(5)
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input').send_keys('MyPwd')
driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div').click()

driver.get('https://www.youtube.com')

driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/a/paper-button').click()

driver.get('https://www.youtube.com/watch?v=d1-pid2mzrA&list=LLgqBx56goSbr96DA-I46H-w&index=12&t=700s')

#########get live chats

time.sleep(5)
#change to iframe 'chatframe'
driver.switch_to.frame("chatframe")

last_index = 0


while(True):
    chattings = driver.find_elements_by_css_selector('#message')
    for i in range(last_index, len(chattings)):
        print(chattings[i].text)
        if(chattings[i].text == "1557"):
            """
            driver.switch_to.default_content()
            player = driver.find_element_by_css_selector('#movie_player > div.html5-video-container > video')
            player.click()
            driver.switch_to.frame("chatframe")
            """

            hover_elem = driver.find_element_by_xpath("/html/body/yt-live-chat-app/div/yt-live-chat-renderer/iron-pages/div/div[1]/div[3]/div[1]/yt-live-chat-item-list-renderer/div/div[1]/div/div/yt-live-chat-text-message-renderer[%d]" %(i-1))
            hover_elem.click()
            button1 = driver.find_element_by_xpath("/html/body/yt-live-chat-app/div/yt-live-chat-renderer/iron-pages/div/div[1]/div[3]/div[1]/yt-live-chat-item-list-renderer/div/div[1]/div/div/yt-live-chat-text-message-renderer[%d]/div[2]/yt-icon-button/button/yt-icon" %(i-1))
            button1.click()
            button2 = driver.find_element_by_xpath("/html/body/yt-live-chat-app/iron-dropdown/div/ytd-menu-popup-renderer/paper-listbox/ytd-menu-navigation-item-renderer/a/paper-item")
            button2.click()
            button3 = driver.find_element_by_xpath("/html/body/yt-live-chat-app/paper-dialog/yt-confirm-dialog-renderer/div[2]/div/yt-button-renderer[2]/a/paper-button")
            button3.click()

    last_index = len(chattings)




