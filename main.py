import sys
from time import sleep

#Have to be installed
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

COFFEE_PRICE = 3

coffees = 0

username = "iicofficial" if len(sys.argv) <= 1 else sys.argv[1]
base_url = "https://www.buymeacoffee.com/"

driver = webdriver.Firefox()
driver.get(f"{base_url}{username}")
driver.maximize_window()

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
sleep(3)

while True:
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        sleep(3)
        driver.find_element(By.ID, "load-more-recent").click()
    except NoSuchElementException:
        donations = driver.find_elements(By.XPATH, "/html/body/div[3]/div/div[5]/div[1]/div/div[3]/div/div[2]/div[1]/div/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/span[2]")
        for donation in donations:
            if donation.text.split(" ")[-2] == "a":
                coffees += 1
            else:
                coffees += int(donation.text.split(" ")[-2])
        print(f"The user {username} had a total of {len(donations)} donations having a whole revenue of {coffees * COFFEE_PRICE}")
        break
    except Exception as e:
        try:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            sleep(3)
            driver.find_element(By.ID, "load-more-recent").click()
        except Exception as e:
            break
driver.close()