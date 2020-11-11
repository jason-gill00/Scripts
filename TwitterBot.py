from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        PATH = "C:\Program Files\chromedriver"
        self.driver = webdriver.Chrome(PATH)
        self.driver.get("https://twitter.com/")
        time.sleep(3)

    def login(self):
        driver = self.driver
        user_field_tag = driver.find_element_by_name("session[username_or_email]")
        user_field_tag.clear()
        user_field_tag.send_keys(self.username)
        password_field_tag = driver.find_element_by_name("session[password]")
        password_field_tag.send_keys(self.password)
        button_tag = driver.find_element_by_class_name("css-18t94o4.css-1dbjc4n.r-1niwhzg.r-p1n3y5.r-sdzlij.r-1phboty.r-rs99b7.r-1w2pmg.r-d0pm55.r-1vuscfd.r-1dhvaqw.r-1ny4l3l.r-1fneopy.r-o7ynqc.r-6416eg.r-lrvibr")
        button_tag.click()

    def like(self, search):
        driver = self.driver
        time.sleep(3)
        search_class_name = "r-30o5oe.r-1niwhzg.r-17gur6a.r-1yadl64.r-deolkf.r-homxoj.r-poiln3.r-7cikom.r-1ny4l3l.r-1sp51qo.r-1lrr6ok.r-1dz5y72.r-fdjqy7.r-13qz1uu"
        search_tag = driver.find_element_by_class_name(search_class_name)
        search_tag.send_keys(search)
        search_tag.send_keys(Keys.RETURN)
        time.sleep(4)

        tweet_list = []

        # for i in range(1,3):
        #     button = driver.find_elements_by_xpath("//div[@data-testid='like']")
        #     for x in range(len(button)):
        #         button[x].click()
            # driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            # time.sleep(3)

        #######################################################################################################
        # list_tweets = []
        # class_name_tag = "r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0 css-4rbku5 css-18t94o4 css-901oao"
        # class_name = class_name_tag.replace(' ', '.')
        # for i in range(1,4):
        #     #tweets = driver.find_elements_by_xpath("//div[@data-testid='tweet']")
        #     tweets = driver.find_elements_by_class_name(class_name)
        #     for tweet in tweets:
        #         print(tweet.get_attribute('href'))
        #         list_tweets.append(tweet.get_attribute('href'))
        #     driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        #     time.sleep(3)
        # for tw in list_tweets:
        #     driver.get(tw)
        #     time.sleep(2)
        #     like_button = driver.find_element_by_xpath("//div[@data-testid='like' or @data-testid='unlike']")
        #     like_button.click()


        ###################################################################################

        class_name_tag = "r-1re7ezh r-1loqt21 r-1q142lx r-1qd0xha r-a023e6 r-16dba41 r-ad9z0x r-bcqeeo r-3s2u2q r-qvutc0 css-4rbku5 css-18t94o4 css-901oao"
        class_name = class_name_tag.replace(' ', '.')
        tweets = driver.find_elements_by_class_name(class_name)
        for x in range(len(tweets)):
            ActionChains(driver).move_to_element(tweets[x]).perform()
            like_button = tweets[x].find_element_by_xpath("//div[@data-testid='like' or @data-testid='unlike']")
            time.sleep(1)
            like_button.click()
            if x == ((len(tweets))-1):
                tweets = driver.find_elements_by_class_name(class_name)
            print(x)






        # for t in list_tweets:
        #     print(t)

        # tweets = driver.find_elements_by_class_name("css-1dbjc4n.r-1d09ksm.r-18u37iz.r-1wbh5a2")
        # print(len(tweets))
        # text_doc = open("htmltext.txt", 'a')
        # text_doc.write(driver.page_source)
        # text_doc.close()

        # tag = tweets[6].find_elements_by_tag_name('a')
        # print("ASJDn")
        # print(tag[1].get_attribute('href'))

        # for tweet in tweets:
        #     tag = tweet.find_elements_by_tag_name('a')
        #     print(len(tag))
        #     tweet_link = tag[1].get_attribute('href')
        #     print(tweet_link)
        #     tweet_list.append(tweet_link)
        #
        #
        # for x in tweet_list:
        #     print(x)








        # driver.find_elem
        # tweets = driver.find_elements_by_class_name("css-1dbjc4n.r-18u37iz")
        # for tweet in tweets:
        #     tweet.find_element_by_class_name("css-901oao.css-16my406.r-1qd0xha.r-ad9z0x.r-bcqeeo.r-qvutc0")
        #     print(tweet.text)
        # button_class_name = "css-1dbjc4n.r-1niwhzg.r-sdzlij.r-1p0dtai.r-xoduu5.r-1d2f490.r-xf4iuw.r-u8s1d.r-zchlnj.r-ipm5af.r-o7ynqc.r-6416eg"
        # like_button = tweets.find_element_by_class_name(button_class_name)
        # like_button.click()



        # for tweet in tweets:
        #     button_class_name = "css-1dbjc4n.r-1niwhzg.r-sdzlij.r-1p0dtai.r-xoduu5.r-1d2f490.r-xf4iuw.r-u8s1d.r-zchlnj.r-ipm5af.r-o7ynqc.r-6416eg"
        #     #button_class = button_class_name.replace(" ", ".")
        #     like_button = tweet.find_element_by_class_name(button_class_name)
        #     like_button.click()


if __name__ == "__main__":
    bot = TwitterBot("jasongilltest@gmail.com", "testpassword123")
    bot.login()
    bot.like("anime")
