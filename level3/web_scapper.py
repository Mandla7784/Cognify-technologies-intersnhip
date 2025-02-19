from bs4 import BeautifulSoup
import requests

URL = "https://realpython.github.io/fake-jobs/"
PAGE =  requests.get(URL)


print(PAGE.text)

def main():
    pass




if __name__=="__main__":
    main()