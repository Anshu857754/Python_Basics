"""Real-World Example: Multithreading for I/0-bound Tasks
Scenario: Web Scraping
Web scraping often involves making numerous network requests to
fetch web pages. These tasks are I/0-bound because they spend a lot of
time waiting for responses from servers. Multithreading can significantly
improve the performance by allowing multiple web pages to be fetched concurrently."""


''' https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/concepts/

https://python.langchain.com/v0.2/docs/tutorials/ '''



# import the bs4 libararay means BeautifulSoup4 (BS4)  

"""BS4 = Website ka HTML tod ke data nikalne ka tool
(Web Scraping ke liye use hota hai)"""
import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://python.langchain.com/v0.2/docs/introduction/',
    'https://python.langchain.com/v0.2/docs/concepts/',
    'https://python.langchain.com/v0.2/docs/tutorials/ '
]

def fetch_contents(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f"fetched data {len(soup.text)} characters from {url}")

threads = []


for url in urls:
    thread = threading.Thread(target=fetch_contents,args=(url,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print("All webpages fetched data")