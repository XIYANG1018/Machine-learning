import requests
from bs4 import BeautifulSoup

# act as a normal browser

headers = {
    "User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1"
}
# deal with different pages
for start_num in range(0, 250, 25):

    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=headers)
    # store the string content
    html = response.text
        
    # Beautiful soup change the content to a tree-shaped structure
    soup = BeautifulSoup(html, "html.parser")
    all_titles = soup.find_all("span", attrs={"class": "title"})
    for title in all_titles :
        title_string = title.string
        if "/" not in title_string:
            print(title_string)


# print status code
# print(response.status_code)

# print text
# print(response.text)



