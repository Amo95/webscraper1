import urllib.request as req
from bs4 import BeautifulSoup as bs
import os

def scraper(url):
    res = req.urlopen(url)
    html = res.read()

    sp = bs(html, "html.parser")
    
    for i in sp("a"):
        url = i.get("href")
        print(f"\n{i}")


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    try:
        clear()
        url = input("Enter url: ")
        part = "https://"

        if url[0:8] == part:
            scraper(url)
        elif part not in url:
            new_url = f"{part}{url}"
            scraper(new_url)
        else:
            print("Wrong Url Format")
        
    except ValueError:
        print("Unknown URL, please try again")
        input("Press enter to go back>>>\n")


if __name__ == "__main__":
    main()
        
    


