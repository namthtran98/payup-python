import json


def ReadFile():
    # Opening JSON file
    f = open('Data/data.json')
    # returns JSON object as
    # a dictionary
    data = json.load(f)
    return data
