from selenium.webdriver import ActionChains

def test_booking(browser):
    browser.implicitly_wait(100000)

    search = browser.find_element_by_name("destination")
    search.click()
    search.send_keys("Jumeirah Emirates Towers, Dubai, The United Arab Emirate")
    browser.implicitly_wait(100)

    result = browser.find_element_by_id("js-value-0")
    result.click()

    openDate = browser.find_element_by_xpath("//input[@name='dates']")
    openDate.click()
    browser.implicitly_wait(100)

    '''next = browser.find_element_by_class_name('calendar-style__arrows calendar-style__arrow__next')
    action = ActionChains(browser)
    action.move_to_element(next).perform()
    browser.implicitly_wait(100)
    next.click()'''

    browser.find_element_by_xpath("//span[contains(text(),'March')]/following-sibling::span[contains(text(),'14')]").click()
    browser.find_element_by_xpath("//span[contains(text(),'March')]/following-sibling::span[contains(text(),'17')]").click()
    browser.implicitly_wait(100)

    submit = browser.find_element_by_xpath("//button[@type='submit']")
    submit.click()
    browser.implicitly_wait(100000)

    assert (browser.find_element_by_xpath("//div[@class='breadcrumbs']/following-sibling::h3")).text != "No accommodations available"