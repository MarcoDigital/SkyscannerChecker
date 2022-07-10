import requests
import json
import time
import sendemail
import sys

email = str(input("Wat is je Gmail account? "))
wachtwoord = str(input("Wat is je wachtwoord? "))
key = str(input("RapidAPI key? "))
kosten = int(input("Voer een minimale kosten in voor een ticket: "))
interval = int(input("Om de hoeveel seconden moet er gecheckt worden? "))

##### RAPID API ###
departure_date = ("2022-12-01")
return_date = ("2022-12-10")
origin = ("AMS")
destination = ("CUN")

url = "https://skyscanner44.p.rapidapi.com/search"

querystring = {"adults": "2", "origin": origin, "destination": destination, "departureDate": departure_date,
               "returnDate": return_date, "cabinClass": "economy", "currency": "EUR"}

headers = {
    "X-RapidAPI-Key": key,
    "X-RapidAPI-Host": "skyscanner44.p.rapidapi.com"
}

response = requests.request(
    "GET", url, headers=headers, params=querystring)
##### RAPID API ###


def gen():
    data = response.json()

    buckets = data["itineraries"]["buckets"]

    for info in buckets:
        try:
            soort = info["id"]
            prijs = info["items"][0]["price"]["raw"]
            prijt_int = int(prijs)
            link_en = info["items"][0]["deeplink"]
            link_nl = link_en.replace(".net", ".nl")
            bericht = (
                f"Klasse: {soort}\nPrijs: {prijs} EUR\nLink: {link_nl}\n")

        except:
            print("Geen data gevonden in JSON")
            time.sleep(interval)

        if prijt_int > kosten:
            sendemail.emailuser(email, wachtwoord, bericht)
            print("Email gestuurd!")
            sys.exit()
        else:
            pass


if __name__ == "__main__":
    while True:
        gen()
        time.sleep(interval)
