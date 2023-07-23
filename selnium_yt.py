import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pyautogui import size
width, hieght = size()
def main():
    options = Options()
    # options.headless = True
    options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
                            options=options)

    driver.get("https://www.youtube.com/")
    driver.fullscreen_window()
    while True:
        if driver.get_window_rect()[0] != hieght and driver.get_window_rect()[1] != width:
            if driver.get_window_rect()[-1] != 0:
                driver.set_window_rect(0, 0, width, hieght)

        # print(driver.get_window_rect())

        driver.fullscreen_window()
        if "youtube.com/shorts/" in driver.current_url:
            driver.get("file:///D:/backu/Kids%20Mode/file.html")
        time.sleep(20)
if __name__ == "__main__":
    main()
# exit()
# import os, time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# options = Options()
# options.add_experimental_option('detach', True)
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),
#                           options=options)

# driver.get("http://youtube.com/")
# driver.fullscreen_window()
# # search_bar = driver.find_elements("xpath", "//input[@href]")
# search_bar = driver.find_elements(By.XPATH, "//input[@id='search']")
# for searchs in search_bar:
#     print(searchs.get_attribute("outerHTML"))
#     searchs.send_keys("BLACKZEESH")

# search_button = driver.find_elements(By.XPATH, "//button[@id='search-icon-legacy']")

# for searchbtn in search_button:
#     print(searchbtn.get_attribute("outerHTML"))
#     searchbtn.click()

# time.sleep(1)
# channellink = driver.find_elements(By.XPATH, "//a[@href]")

# for searchbtn in channellink:
#     print(searchbtn.get_attribute("outerHTML"))
#     if "@blackzeesh" in searchbtn.get_attribute("outerHTML"):
#         searchbtn.click()

# driver.execute_script("alert('Hello World');")