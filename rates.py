import requests
import xml.etree.ElementTree as ET

# URL-адрес по которому будет выполняться HTTP-запрос

URL= "https://cbr.ru/scripts/XML_daily.asp"

# Выполняем HTTP-запрос методом get по указанному URL
response = requests.get(URL)
tree = ET.fromstring(response.text) # Преобразуем строку с XML-данными в объект
user_case = int(input("Вывести информацию по коду валюты - введите 1\n"
                      "Вывести таблицу курсов всех валют к рублю - введите 2\n"))

if user_case == 1:

    code_currency = "USD" # Например, доллар
    value_currency = None # Курс

    for element_currency in tree.findall(".//Valute"):
        char_code = element_currency.find("CharCode").text
        if char_code == code_currency:
            nominal = element_currency.find("Nominal").text # Например 10
            name_currency = element_currency.find("Name").text # Например Евро
            value_currency = element_currency.find("Value").text # Например 55,55 рублей

    if value_currency:
        print(f"{nominal} {name_currency} ({code_currency}) = {value_currency} рублей")
    else:
        print(f"Курс {code_currency} на текущий день неизвестен")

elif user_case == 2:
    # Здесь должен быть наш новый функционал, который выводит таблицу курсов в сех валют
    print("ok")
    
    currency_rates = {}

    for element_currency in tree.findall(".//Valute"):
        char_code = element_currency.find("CharCode").text
        value = element_currency.find("Value").text
        currency_rates[char_code] = value

        # Выводим таблицу с курсами всех валют
        print("Курсы валют к рублю:")
        print("--------------------")
        for char_code, value in currency_rates.items():
            print(f"{char_code}, {value}")
