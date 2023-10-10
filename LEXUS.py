from bs4 import BeautifulSoup
import requests
import json

url = 'https://www.lexus.ua/new-cars'

headers = {'Accept': '*/*', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}

req = requests.get(url, headers=headers)
src = req.text
# print(src)

links = []

# with open('LEXUS.html', 'w', encoding='utf-8') as file:
#     file.write(src)

with open('LEXUS.html', encoding='utf-8') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')


hrefs = soup.find(class_='ModelResultStyles__Grid-sc-1whsw5o-0 eLBxLK').find_all('a')
for href in hrefs:
    href_text = href.text
    href_url = href.get('href')
    link = {'Lexus': href_text, 'Url': href_url}
    links.append(link)
    print('Lexus', href_text, ':', href_url)

with open('C:/Users/TVOYO/Desktop/Новая папка (2)/Python/tasks/Euler_project/data/work/Lexus.json', 'a', encoding='utf-8', newline='') as file:
    json.dump(links, file, indent=4, ensure_ascii=False)


