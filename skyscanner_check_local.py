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


def gen():
    with open("data_demo.json") as f:
        data = json.load(f)
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

        if prijt_int > 1100:
            sendemail.emailuser(email, wachtwoord, bericht)
            print("Email gestuurd!")
            sys.exit()
        else:
            time.sleep(interval)


if __name__ == "__main__":
    while True:
        gen()
        time.sleep(interval)
