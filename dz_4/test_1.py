import time
from testpage import OperationsHelpers
import logging
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step1(browser, send_email):
    logging.info("Test1 starting")
    testpage = OperationsHelpers(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401"


def test_step2(browser, send_email):
    logging.info("Test2 starting")
    testpage = OperationsHelpers(browser)
    testpage.go_to_site()
    testpage.enter_login("pov")
    testpage.enter_pass("26f005fa86")
    testpage.click_login_button()
    assert testpage.get_user() == "Home"


def test_step3(browser, send_email):
    logging.info("Test3 starting")
    testpage = OperationsHelpers(browser)
    testpage.go_to_site()
    testpage.enter_login("pov")
    testpage.enter_pass("26f005fa86")
    testpage.click_login_button()
    testpage.click_new_post_btn()
    time.sleep(testdata['sleep_time'])
    testpage.title_post("Test_3")
    testpage.description_post("Description")
    testpage.content_post("Hello World!")
    time.sleep(testdata['sleep_time'])
    testpage.click_save_post_btn()
    assert testpage.success_save_post() == "Hello World!"


def test_step4(browser, send_email):
    logging.info("Test4 starting")
    testpage = OperationsHelpers(browser)
    testpage.go_to_site()
    testpage.enter_login("pov")
    testpage.enter_pass("26f005fa86")
    testpage.click_login_button()
    testpage.click_contact_btn()
    testpage.contact_name("Ilya")
    testpage.contact_email("ilya@mail.ru")
    testpage.contact_content("support_test_4")
    testpage.click_contact_us_btn()
    time.sleep(testdata['sleep_time'])
    assert testpage.contact_alert() == "Form successfully submitted"