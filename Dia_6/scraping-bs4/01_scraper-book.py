from bs4 import BeautifulSoup
import requests

url = 'https://books.toscrape.com/'
response=requests.get(url)
if response.status_code==200:
    soup=BeautifulSoup(response.content,'html.parser')
    books=soup.find_all('article',class_='product_pod')
    for book in books:
        title=book.find('h3').find('a')['title']
        price=book.find('p',class_='price_color').get_text() #get_text solo trae el texto del parafo "p"
        stock=book.find('p',class_='instock availability').get_text()
        image=book.find('img')['src']
        print(title)
        print(price)
        print(stock)
        print(image)
        print('--------------')
else:
    print(f'Error:{response.status_code}')