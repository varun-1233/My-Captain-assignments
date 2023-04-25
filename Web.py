import requests
from bs4 import BeautifulSoup
import pandas
url = "https://news.ycombinator.com/"

req = requests.get(url)
content = req.content

soup = BeautifulSoup(content, "html.parser")

all_title = soup.find_all("tr", {"class": "athing"})
scrapped_info_list=[]

for title in all_title:
    title_dict = {}
    title_dict["name"] = title.find("span", {"class": "titleline"}).text
    for line in soup.find_all("td", {"class": "subtext"}):
        try:
            title_dict["rating"] = line.find("span", {"class": "score"}).text
            title_dict["age"] = line.find("span", {"class": "age"}).text
        except AttributeError:
            pass

    scrapped_info_list.append(title_dict)






data_Frame = pandas.DataFrame(scrapped_info_list)
data_Frame.to_csv("news.csv")