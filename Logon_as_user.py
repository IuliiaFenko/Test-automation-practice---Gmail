from selenium import webdriver

import json
import Main_Library

browser = webdriver.Chrome(executable_path=r"C:\Users\Iuliia\PycharmProjects\Project venv\chromedriver.exe")
browser.get("https://gmail.com")

with open('Dictionary.json', encoding='utf-8') as data_file:
    string_data = data_file.read()
    dictionary = json.loads(string_data)

Main_Library.logon(browser, dictionary)
Main_Library.exit_account(browser)