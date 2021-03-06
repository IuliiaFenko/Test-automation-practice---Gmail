from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def logon(browser, dictionary):
    email = dictionary['email'].lower()

    id_email = 'identifierId'
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, id_email)))
    element = browser.find_element(by=By.ID, value=id_email)
    element.send_keys(email)

    # validate inserted text is correct
    wait.until(EC.text_to_be_present_in_element_value((By.ID, id_email), email))
    assert element.get_attribute('value').lower() == email

    id_next_identifier = 'identifierNext'
    wait = WebDriverWait(browser, 10)
    wait.until(EC.element_to_be_clickable((By.ID, id_next_identifier)))
    browser.find_element(by=By.ID, value=id_next_identifier).click()

    #validate we are opening right profile
    id_profile = 'profileIdentifier'
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, id_profile)))
    element = browser.find_element(by=By.ID, value=id_profile)
    assert element.text.lower() == email

    name_password = 'password'
    wait = WebDriverWait(browser,10)
    wait.until(EC.visibility_of_element_located((By.NAME, name_password)))
    browser.find_element(by=By.NAME, value=name_password).send_keys(dictionary['password'])

    id_next_password = 'passwordNext'
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, id_next_password)))
    browser.find_element(by=By.ID, value=id_next_password).click()


def exit_account(browser):
    css_selector = "span.gb_7a.gbii"
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))
    browser.find_element(by= By.CSS_SELECTOR, value= css_selector).click()

    id_button_exit = "gb_71"
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, id_button_exit)))
    browser.find_element(by=By.ID, value=id_button_exit).click()