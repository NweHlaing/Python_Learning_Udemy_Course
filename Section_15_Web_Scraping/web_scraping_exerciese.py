import requests
import bs4
res = requests.get("http://quotes.toscrape.com/")
print("Result Text",res.text)
soup = bs4.BeautifulSoup(res.text,'lxml')
print("Soup....",soup)
print("Author class....",soup.select(".author"))
authors = set() 
for name in soup.select(".author"):
    authors.add(name.text)

print("Author.....",authors)

quotes = []
for quote in soup.select(".text"):
    quotes.append(quote.text)

print("Quotes....",quotes)

soup = bs4.BeautifulSoup(res.text,'lxml')
print("Tag class",soup.select('.tag-item'))

for item in soup.select(".tag-item"):
    print(item.text)

