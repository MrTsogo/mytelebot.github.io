from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

import time

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
actions = {
    "lkoh":"Лукойл",
    "prfn": "ЧЗПСН", 
    "posi": "Positive Technologies",
    "ydex": "Яндекс",
    "sber": "Сбербанк",
    "mtlr": "Мечел",
    "fixp": "FixPrice",
    "aflt": "Айрофлот",
    "rosn": "Роснефть"
}


def check_price() -> list:
    res = []
    for action in actions:
        driver.get(f"https://bcs-express.ru/kotirovki-i-grafiki/{action}")
        time.sleep(1)
        price = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[1]/div/div[1]/div")
        res.append(f"{actions[action]} : {price.text}")
        
    driver.close()
    driver.quit()
    return res


def main():
    print(check_price())


if __name__ == "__main__":
    main()
