import time
from selenium import webdriver
from utils import extract_content, extract_list, extract_join

query = "i have been".replace(" ", "+").strip()
URL = "https://www.playphrase.me/#/search?q={}".format(query)

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)

selector_sentences = "//div[@id='search-result']/table/tbody/tr"
selector_phrase = "//td[@class='phrase-text']/a/span/text()"
selector_video = "//div[@class='video-player-box'][1]/video[@class='video-player']/@src"

page_source = driver.page_source.encode("utf-8")

def download_video(phrase):
    q = phrase.replace(" ", "+")
    URL_VIDEO = "https://www.playphrase.me/#/search?q={}".format(q)
    driver.get(URL_VIDEO)
    time.sleep(2)
    link_video = extract_content(driver.page_source.encode("utf-8"), selector_video)
    driver.get(link_video)
    print("\nFAZENDO DOWNLOAD...\n")


for row in extract_list(page_source, selector_sentences):
    download_video(extract_join(row, selector_phrase))
    driver.quit()