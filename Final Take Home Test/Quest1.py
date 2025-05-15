import requests
import xmltodict
import json
import random
import threading
import os
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

def download(date, base):

    # URL of the XML data
    url = f"https://www.floatrates.com/historical-exchange-rates.html?operation=rates&pb_id=1775&page=historical&currency_date={date}&base_currency_code={base}&format_type=xml"
    # Fetch the XML data
    response = requests.get(url)
    response.raise_for_status()  # Ensure we notice bad responses

    # Parse the XML data to a Python dictionary
    data_dict = xmltodict.parse(response.text)

    # Convert the dictionary to a JSON string
    json_data = json.dumps(data_dict, indent=4)

    os.makedirs(f"Rates/{base}", exist_ok=True) ## Create a directory to organize the base currency by

    # Optionally, write the JSON data to a file
    with open(f"Rates/{base}/{date}_exchange_rates_{base}.json", "w") as json_file:
        json_file.write(json_data)

def worker(work_queue):
    while not work_queue.empty():
        try:
            date, base = work_queue.get(block=False)
        except Empty:
            break
        else:
            download(date, base)
            work_queue.task_done()

def thread_pool(dates, base, size=20):
    work_queue = Queue()

    for date in dates:
        work_queue.put((date, base))

    threads = []
    for _ in range(size):
        thread = threading.Thread(target=worker, args=(work_queue,))
        threads.append(thread)

    for thread in threads:
        thread.start()

    work_queue.join()

    for thread in threads:
        thread.join()

rates = ["EUR", "GBP", "USD", "DZD", "AUD", "BWP", "BND", "CAD", "CLP", "CNY", "COP", "CZK", "DKK", "HUF", "ISK", "INR", "IDR", "ILS", "KZT", "KRW", "KWD", "LYD", "MYR", "MUR", "NPR", "NZD", "NOK", "OMR", "PKR", "PLN", "QAR", "RUB", "SAR", "SGD", "ZAR", "LKR", "SEK", "CHF", "THB", "TTD"]
ratesForBase = [r for r in rates if r != "USD" and r != "EUR" and r != "GBP"]


def main():
    dates = listofDates()
    base = random.choice(ratesForBase)

    thread_pool(dates, base)


