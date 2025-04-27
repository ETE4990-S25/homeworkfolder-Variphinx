import re
import json
from collections import defaultdict
from Logger import path


def read(path):
    try: 
        with open(path, 'r') as f:
            lines = f.readlines()
        return lines
    
    except FileNotFoundError:
        print(f"{path} could not be found")

    return []

def levels(lines):
    parsed_logs = []
    pattern = r"^(.*?) \| (.*?) \| (.*?) \| (.*)$"
    for line in lines:
        match = re.match(pattern, line)
        timestamp, level, filename, message = match.groups()
        log_dict = {
                "Level": level,
                "Time": timestamp,
                "File": filename,
                "Message": message
        }
        parsed_logs.append(log_dict)
    return parsed_logs

def countlogs(parsed_logs):
    infocount = 0
    errorcount = 0
    warningcount = 0
    criticalcount = 0
    logs = [["INFO", infocount], ["WARNING",warningcount], ["ERROR", errorcount], ["CRITICAL", criticalcount]]
    for i in parsed_logs:
        for n in logs:
            if i["Level"] == n[0]:
                n[1] +=1
    print("Log Level Summary:")
    for i in logs:
        print(f"{i[0]}: {i[1]}")


def specificlogcount(parsed_logs):
    dict_count = defaultdict(lambda: defaultdict(int)) ## From chatgpt to create empty dictionary if level doesnt exist yet and to start message count as 0
    for log in parsed_logs:
        message = log["Message"]
        level = log["Level"]
        dict_count[level][message] +=1


    with open("log_summary.json", 'w') as j:
        json.dump(dict_count, j, indent = 4)
              

def __main__():

    lines = read(path)
    parsed_logs = levels(lines)
    print(parsed_logs)
    countlogs(parsed_logs)
    specificlogcount(parsed_logs)