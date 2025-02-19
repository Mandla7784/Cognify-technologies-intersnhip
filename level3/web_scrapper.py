from bs4 import BeautifulSoup
import requests

URL = "https://www.hificorp.co.za/"
PAGE =  requests.get(URL)

print(PAGE.text)

def main():
    soup = BeautifulSoup(PAGE.content , "html.parser")

    content = soup.find(id="maincontent")
    product_cards = content.find_all("div",class_="colums")

    for item in product_cards:
        print(item)


if __name__=="__main__":
    main()