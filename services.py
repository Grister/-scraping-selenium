import time

from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

import config
from decorators import social_login_required


class SocialNetworkScraper:
    BASE_URL = f"http://{config.SOCIAL_NETWORK_HOST}:{config.SOCIAL_NETWORK_PORT}"
    LOGIN_URL = f"{BASE_URL}/auth/login"
    BLOG_URL = f"{BASE_URL}/user/blog"
    REGISTER_URL = f"{BASE_URL}/auth/register"

    def __init__(self, driver=None):
        self.driver = driver or self.create_driver()
        self.is_logged_in = False

    def create_driver(self):
        try:
            self.driver = webdriver.Chrome(executable_path=config.CHROME_DRIVER_PATH)
            return self.driver
        except Exception as e:
            print(e.args)

    def social_network_login(self):
        self.social_network_register()
        self.driver.get(self.LOGIN_URL)

        username_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='username']")
        username_elem.send_keys(config.SOCIAL_NETWORK_LOGIN)

        password_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='password']")
        password_elem.send_keys(config.SOCIAL_NETWORK_PASSWORD)

        password_elem.send_keys(keys.Keys.ENTER)

        self.is_logged_in = True

    def social_network_register(self):
        self.driver.get(self.REGISTER_URL)

        username_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='username']")
        username_elem.send_keys(config.SOCIAL_NETWORK_LOGIN)

        email_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='email']")
        email_elem.send_keys(config.SOCIAL_NETWORK_EMAIL)

        password_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='password']")
        password_elem.send_keys(config.SOCIAL_NETWORK_PASSWORD)

        confirm_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='confirm_password']")
        confirm_elem.send_keys(config.SOCIAL_NETWORK_PASSWORD)

        password_elem.send_keys(keys.Keys.ENTER)
        time.sleep(2)

        return self.driver

    @social_login_required
    def social_network_add_post(self, title, content):
        self.driver.get(self.BLOG_URL)

        title_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/input[@id='title']")
        title_elem.send_keys(title)

        content_elem = self.driver.find_element(By.XPATH, "//div[@class='form-group']/textarea[@id='content']")
        content_elem.send_keys(content)

        create_post_elem = self.driver.find_element(By.XPATH, "//form/button[@type='submit']")
        create_post_elem.click()

        time.sleep(2)

        like_elem = self.driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div[1]/div[2]/div/div[1]/a[1]")
        like_elem.click()
        time.sleep(1)

        logout_elem = self.driver.find_element(By.XPATH, "//div[@class='collapse navbar-collapse']"
                                                         "/ul[@class='navbar-nav ms-auto']"
                                                         "/li[@class='nav-item me-2']/a")
        logout_elem.click()

        return self.driver
