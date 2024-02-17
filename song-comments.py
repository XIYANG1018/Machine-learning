# author: Xi Yang

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlencode

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


def get_song_info(keyword):
    headers = {
        "User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
    }

    baseUrl = "https://c.y.qq.com/splcloud/fcgi-bin/smartbox_new.fcg"

    data = urlencode({
        '_': 1708125577180,
        'cv': 4747474,
        'ct': 24,
        'format': 'json',
        'inCharset': 'utf-8',
        'outCharset': 'utf-8',
        'notice': 0,
        'platform': 'yqq.json',
        'needNewCode': 1,
        'uin': 1152921504810845432,
        'g_tk_new_20200303': 1903712151,
        'g_tk': 1903712151,
        'hostUin': 0,
        'is_xml': 0,
        'key': keyword
    })

    r = requests.get(baseUrl, params=data, headers=headers)

    songInfoDict = r.json()
    songList = songInfoDict['data']['song']['itemlist']

    for index, eachSong in enumerate(songList):
        print(index, eachSong['name'], eachSong['singer'])

    choose = int(input("\n请选择歌曲: "))
    song = songList[choose]
    songName = song['name']
    singer = song['singer']
    songID = song['id']
    songMid = song['mid']
    return 'https://y.qq.com/n/ryqq/songDetail/' + songMid


def get_song_comments(songLink):
    
    print(songLink)
    driver=webdriver.Chrome()

    driver.get(songLink)

    # all_comments = driver.find_element(By.CLASS_NAME, "comment__text")
    # for comment in all_comments:
    #     print(comment.text)
    driver.implicitly_wait(1000)
    comments = driver.find_elements(By.CLASS_NAME, "comment__text ")
    for comment in comments:
        comment_texts = driver.find_elements(By.TAG_NAME, 'span')
        for span in comment_texts:
            print(span.text)


    input("Press Enter to close the browser window...")
    driver.quit()
   




if __name__ == '__main__':
    arg = get_song_info('笼')
    get_song_comments(arg)
