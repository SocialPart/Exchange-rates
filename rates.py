import requests
import xml.etree.ElementTree as ET

# URL-адрес по которому будет выполняться HTTP-запрос

URL= "https://cbr.ru/scripts/XML_daily.asp"

# Выполняем HTTP-запрос методом get по указанному URL
response = requests.get(URL)
print(response.content)
