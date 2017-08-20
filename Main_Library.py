from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json

browser = webdriver.Chrome(executable_path=r"C:\Users\Iuliia\PycharmProjects\Project venv\chromedriver.exe")
browser.get("https://gmail.com")


with open('Dictionary.json', encoding='utf-8') as data_file:
    string_data = data_file.read()
    dictionary = json.loads(string_data)


def logon(browser, dictionary):

    id_email = 'identifierId'

    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, id_email)))
    element = browser.find_element(by=By.ID, value=id_email)
    element.send_keys(dictionary['email'])
    # validate inserted text is correct

    assert element.get_attribute('value') == 'Wdjfvhu65@gmail.com'

    id_next = 'identifierNext'

    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, id_next)))
    browser.find_element(by=By.ID, value=id_next).click()

    #validate we are opening right profile

    id_profile = 'profileIdentifier'
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, id_profile)))
    element = browser.find_element(by=By.ID, value=id_profile)
    assert element.text == 'wdjfvhu65@gmail.com'

    name_password = 'password'

    wait = WebDriverWait(browser,10)
    wait.until(EC.visibility_of_element_located((By.NAME, name_password)))
    browser.find_element(by=By.NAME, value=name_password).send_keys(dictionary['password'])

    profile_id = 'profileIdentifier'

logon(browser, dictionary)
