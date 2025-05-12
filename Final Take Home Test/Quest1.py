import requests
import xmltodict
import json
import random
from datetime import datetime, timedelta

def listofDates():
    start_date = datetime.strptime("2025-05-04", "%Y-%m-%d")
    end_date = datetime.today()
    change = end_date - start_date

    global dates
    dates = []
    for i in range(change.days):
        date = (start_date + (timedelta(i)))
        dates.append(date.strftime("%Y-%m-%d"))
    


rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY", "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW", "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]
ratesForBase = [r for r in rates if r != "USD" and r != "EUR" and r != "GBP"]


for date in dates:
    # URL of the XML data
    base = random.choice(ratesForBase)
    url = f"https://www.floatrates.com/historical-exchange-rates.html?operation=rates&pb_id=1775&page=historical&currency_date={date}&base_currency_code={base}&format_type=xml"
    print(url)
    # Fetch the XML data
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses

    # Parse the XML data to a Python dictionary
    data_dict = xmltodict.parse(response.text)

    # Convert the dictionary to a JSON string
    json_data = json.dumps(data_dict, indent=4)

    # Print the JSON data
    print(json_data)

    # Optionally, write the JSON data to a file
    with open(f"{date}_exchange_rates_{base}.json", "w") as json_file:
        json_file.write(json_data)
