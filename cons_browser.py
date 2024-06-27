from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome()
browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
assert "Википедия" in browser.title

request = input("Введите начальный запрос: ")
search_box = browser.find_element(By.ID, "searchInput")
search_box.send_keys(request)
search_box.send_keys(Keys.RETURN)

firstLink = browser.find_element(By.CLASS_NAME, "mw-search-result-heading").find_element(By.TAG_NAME, "a").click()

while True:
    title = browser.find_element(By.CLASS_NAME, "mw-page-title-main").text
    print(f"\n{title}\n")
    print("1. Листать параграфы")
    print("2. Перейти по случайной ссылке")
    print("3. Выход")
    choice = input("Ваш выбор: ").strip()

    if choice == "1":
        paragraphs = browser.find_elements(By.TAG_NAME, "p")
        for paragraph in paragraphs:
            print()
            print(paragraph.text)
            if input("\nДля продолжения нажмите Enter: ").strip() == "": continue
            break
    elif choice == "2":
        links = []
        for element in browser.find_elements(By.TAG_NAME, "a"):
            link = element.get_attribute("href")
            if link is not None:
                if link.startswith("https://ru.wikipedia.org/wiki/"):
                    links.append(element.get_attribute("href"))
        if len(links) > 0:
            sucsess = False
            while not sucsess:
                link = random.choice(links)
                try:
                    browser.get(link)
                    sucsess = True
                except:
                    pass

    elif choice == "3":
        break