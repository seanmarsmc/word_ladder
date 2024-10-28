from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from ladder_solver import *

MAX_GAMES = 964

def lots_of_solver():
    class_start_tag = "startWordRowContainer"
    class_end_tag = "endWordRowContainer"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    possible_words = get_words(WORD_FILE)

    for i in range(1, 964):
        url = "https://wordwormdormdork.com/#/game/" + str(i)
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        start_letters = soup.find_all("div", class_=class_start_tag)
        start_word = start_letters[0].text
        end_letters = soup.find_all("div", class_=class_end_tag)
        end_word = end_letters[0].text

        length,path = ladder_length(start_word,end_word,possible_words)
        print(f"{i}. ",end="")
        print_path(length,path)

    driver.quit()

def ladder_solver():
    url = "https://wordwormdormdork.com/"
    class_start_tag = "startWordRowContainer"
    class_end_tag = "endWordRowContainer"

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    start_letters = soup.find_all("div", class_=class_start_tag)
    start_word = start_letters[0].text

    end_letters = soup.find_all("div", class_=class_end_tag)
    end_word = end_letters[0].text

    driver.quit()

    possible_words = get_words(WORD_FILE)
    length,path = ladder_length(start_word,end_word,possible_words)
    print_path(length,path)


if __name__ == "__main__":  
    #lots_of_solver()
    print("Today's Puzzle:")
    ladder_solver()
