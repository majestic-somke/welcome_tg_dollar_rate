import requests


def get_usd_rub():
    url = "https://api.exchangerate-api.com/v4/latest/USD"

    response = requests.get(url)

    if response.status_code == 200:  # succes
        data = response.json()
        print(data)
        
        usd_to_rub = data['rates'].get('RUB')
        if usd_to_rub:
            print(f"Курс USD/RUB: {usd_to_rub}")
            
            return usd_to_rub
        else:
            print("Курс рубля к доллару не найден.")
    else:
        print("Ошибка при запросе API:", response.status_code)
        