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

# find video titles and view counts
soup = BeautifulSoup(html, 'lxml')
titles = soup.find_all('a', id = 'video-title-link')
metadata = soup.find_all('span', class_ = 'inline-metadata-item style-scope ytd-video-meta-block')
copy = metadata.copy()
for item in copy:
    if str(item.decode_contents()).find('ago') != -1:
        metadata.remove(item)

titles.pop()

# write video titles to file
with open('titles.txt', 'wb') as f:
    for x in range(len(titles)):
        title = titles[x]
        viewCount = metadata[x]
        f.write(str(title.get('title') + '\n').encode())
        f.write(str(viewCount.decode_contents() + '\n').encode())