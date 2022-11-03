from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())

# freeCodeCamp videos
driver.get(url = 'https://www.youtube.com/c/Freecodecamp/videos')

# scrolls screen to load more videos
def scroll_to_bottom(driver):

    old_position = 0
    new_position = None

    while new_position != old_position:

        old_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))

        time.sleep(1)
        driver.execute_script((
                "var scrollingElement = (document.scrollingElement ||"
                " document.body);scrollingElement.scrollTop ="
                " scrollingElement.scrollHeight;"))

        new_position = driver.execute_script(
                ("return (window.pageYOffset !== undefined) ?"
                 " window.pageYOffset : (document.documentElement ||"
                 " document.body.parentNode || document.body);"))

scroll_to_bottom(driver)

html = driver.page_source
driver.close()

# find video titles
soup = BeautifulSoup(html, 'lxml')
details = soup.find_all('a', id = 'video-title-link')
details.pop()

# write video titles to file
with open('titles.txt', 'wb') as f:
    for x in details:
        f.write(str(x.get('title')+ '\n').encode())