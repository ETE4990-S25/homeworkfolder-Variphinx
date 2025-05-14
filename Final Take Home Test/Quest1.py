import requests
import xmltodict
import json
import random
import threading
from queue import Queue, Empty
from datetime import datetime, timedelta


def listofDates():
    start_date = datetime.strptime("2011-05-04", "%Y-%m-%d")
    end_date = datetime.today()
    change = end_date - start_date

    dates = []
    for i in range(change.days):
        date = (start_date + (timedelta(i)))
        dates.append(date.strftime("%Y-%m-%d"))
    return dates

def download(date):

    # URL of the XML data
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
    with open(f"Final Take Home Test/Rates/{date}_exchange_rates_{base}.json", "w") as json_file:
        json_file.write(json_data)

def worker(work_queue):
    while not work_queue.empty():
        try:
            date = work_queue.get(block=False)
        except Empty:
            break
        else:
            download(date)
            work_queue.task_done()

def thread_pool(dates, size=15):
    work_queue = Queue()

    for date in dates:
        work_queue.put(date)

    threads = []
    for _ in range(size):
        thread = threading.Thread(target=download, args=(work_queue,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    work_queue.join()

    for thread in threads:
        thread.join()

rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY", "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW", "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]
ratesForBase = [r for r in rates if r != "USD" and r != "EUR" and r != "GBP"]

dates = listofDates()
base = random.choice(ratesForBase)

thread_pool(dates)
