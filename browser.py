from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep


class Browser:

    def __init__(self, download_dir="/tmp/firefox_testing"):
        options = Options()
        # options.add_argument("--headless")
        options.set_preference("browser.download.folderList", 2)  # download files in the last specified directory
        options.set_preference("browser.download.manager.showWhenStarting", False)  # doesnt display pop window at download
        options.set_preference("browser.download.dir", download_dir)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk",
                               "audio/mpeg")
        self.driver = webdriver.Firefox(firefox_options=options)
        self.driver.get("https://www.mp3juices.cc/")

    def get_song(self, song_name):
        print("Loading song", song_name)
        count = 0
        while True:
            count += 1
            try:
                self.search_song(song_name)
                self.download_song()
            except:
                print("Error loading this song")
                sleep(5)
                if count <= 1:
                    print("Trying one more time")
                else:
                    print("Fail, moving to the next one")
                    return
            else:
                print("Song downloaded, moving to the next one")
                return

    def search_song(self, song_name):
        search_bar = self.driver.find_element_by_id("query")
        search_bar.clear()
        search_bar.send_keys(song_name)
        search_button = self.driver.find_element_by_id("button")
        search_button.click()
        # waits 2 seconds for page to load, add more if internet is slow
        sleep(2)

    def download_song(self):
        songs_class = self.driver.find_elements_by_class_name("download")
        song_class = songs_class[0]
        song_class.click()
        sleep(20)
        download = self.driver.find_element_by_class_name("url")
        download.click()


if __name__ == "__main__":
    browser = Browser()
    browser.get_song("Counting stars")
    browser.get_song("Secrets Imagine Dragons")

