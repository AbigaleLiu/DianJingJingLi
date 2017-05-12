# _*_ coding:utf-8 _*_
from selenium import webdriver
class Login:
    def login(self):
        driver = webdriver.Firefox()
        driver.get("http://15war.com/user/login?backUrl=%2F16%2Fmatch%2F176")
        driver.find_element_by_name("mobile").send_keys("18708125576")
        driver.find_element_by_name("password").send_keys("123456")
        driver.find_element_by_link_text("立即登录").click()
        driver.quit()

if __name__ == '__main__':
    Login().login()