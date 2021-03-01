import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


@pytest.fixture
def browser():
    PATH = "/Users/nikolaeva31/PycharmProjects/yoshinogari/UI/chromedriver"
    driver = webdriver.Chrome(PATH)
    driver.get("https://dev.happytravel.com")
    driver.implicitly_wait(100000)
    return driver

@pytest.fixture(autouse=True)
def auth(browser):
    username = browser.find_element_by_name("Input.UserName")
    password = browser.find_element_by_id('Input_Password')
    username.click()
    # add your personal data
    username.send_keys("")
    password.send_keys("")
    username.send_keys(Keys.RETURN)
    title = browser.title
    return title

    browser.close()