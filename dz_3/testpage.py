from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (By.XPATH, """//*[@id="login"]/div[1]/label/input""")
    LOCATOR_PASS_FIELD = (By.XPATH, """//*[@id="login"]/div[2]/label/input""")
    LOCATOR_LOGIN_BTN = (By.XPATH, """//*[@id="login"]/div[3]/button""")
    LOCATOR_ERROR_FIELD = (By.XPATH, """//*[@id="app"]/main/div/div/div[2]/h2""")
    LOCATOR_USER_FIELD = (By.XPATH, """//*[@id="app"]/main/nav/a/span""")


class TestSearchLocatorsPosts:
    LOCATOR_NEW_POST = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITLE_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_TEXT_FIELD = (By.XPATH, """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_BTN = (By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_POST = (By.XPATH, """//*[@id="app"]/main/div/div[1]/div/div[3]""")


class TestSearchLocatorsContact:
    LOCATOR_CONTACT_BTN = (By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_NAME_FIELD = (By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_EMAIL_FIELD = (By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTENT_FIELD = (By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_US_BTN = (By.XPATH, """//*[@id="contact"]/div[4]/button/span""")


class OperationsHelpers(BasePage):
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def enter_pass(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASS_FIELD[1]}")
        login_field = self.find_element(TestSearchLocators.LOCATOR_PASS_FIELD)
        login_field.clear()
        login_field.send_keys(word)

    def click_login_button(self):
        logging.info("Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=3)
        text = error_field.text
        logging.info(f"find text {text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return text

    def get_user(self):
        logging.info("User")
        user = self.find_element(TestSearchLocators.LOCATOR_USER_FIELD, time=2)
        text = user.text
        return text

    def click_new_post_btn(self):
        logging.info("Click create new post")
        self.find_element(TestSearchLocatorsPosts.LOCATOR_NEW_POST).click()

    def title_post(self, word):
        logging.info("new title post")
        title_field = self.find_element(TestSearchLocatorsPosts.LOCATOR_TITLE_FIELD, time=3)
        title_field.clear()
        return title_field.send_keys(word)

    def description_post(self, word):
        logging.info("new description post")
        description_field = self.find_element(TestSearchLocatorsPosts.LOCATOR_DESCRIPTION_FIELD, time=3)
        description_field.clear()
        return description_field.send_keys(word)

    def content_post(self, word):
        logging.info("new content post")
        content_field = self.find_element(TestSearchLocatorsPosts.LOCATOR_TEXT_FIELD, time=3)
        content_field.clear()
        return content_field.send_keys(word)

    def click_save_post_btn(self):
        logging.info("Click create new post")
        self.find_element(TestSearchLocatorsPosts.LOCATOR_SAVE_BTN).click()

    def success_save_post(self):
        logging.info("success save post")
        post = self.find_element(TestSearchLocatorsPosts.LOCATOR_POST, time=2)
        text = post.text
        return text

    def click_contact_btn(self):
        logging.info("Click contact button")
        self.find_element(TestSearchLocatorsContact.LOCATOR_CONTACT_BTN).click()

    def contact_name(self, word):
        logging.info("input contact name")
        name_contact = self.find_element(TestSearchLocatorsContact.LOCATOR_NAME_FIELD)
        name_contact.clear()
        return name_contact.send_keys(word)

    def contact_email(self, word):
        logging.info("input contact email")
        email_contact = self.find_element(TestSearchLocatorsContact.LOCATOR_EMAIL_FIELD)
        email_contact.clear()
        return email_contact.send_keys(word)

    def contact_content(self, word):
        logging.info("input contact content")
        content_contact = self.find_element(TestSearchLocatorsContact.LOCATOR_CONTENT_FIELD)
        content_contact.clear()
        return content_contact.send_keys(word)

    def click_contact_us_btn(self):
        self.find_element(TestSearchLocatorsContact.LOCATOR_CONTACT_US_BTN).click()

    def contact_alert(self):
        alert = self.driver.switch_to.alert
        return alert.text