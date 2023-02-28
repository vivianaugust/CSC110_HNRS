import json

def main():
    data = json.load(open('data/hourly.json'))
    print(data["properties"]["periods"][0]["shortForecast"])
    #for p in data["properties"]["periods"]:
    #    print(p["number"], p["temperature"])

main()