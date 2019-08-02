import time
from selenium import webdriver
from selenium.webdriver import ChromeOptions
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
    filename = phrase.replace(" ", "_")

    FILE_PATH = "/home/antoniozechin/Documents/videos/{}.mp4".format(filename)
    options = ChromeOptions()
    options.set_capability("download.dir", FILE_PATH)
    options.set_capability("download.directory_upgrade", True)
    options.set_capability("download.extensions_to_open",
                           "")
    options.set_capability("download.prompt_for_download", False)

    driver = webdriver.Chrome(chrome_options=options)


    q = phrase.replace(" ", "+")
    URL_VIDEO = "https://www.playphrase.me/#/search?q={}".format(q)
    driver.get(URL_VIDEO)
    time.sleep(2)
    link_video = extract_content(driver.page_source.encode("utf-8"), selector_video)
    driver.get(link_video)
    print("\nFAZENDO DOWNLOAD...\n")
    driver.quit()


for row in extract_list(page_source, selector_sentences):
    driver.quit()
    download_video(extract_join(row, selector_phrase))