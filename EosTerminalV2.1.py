#include <iostream>
import sys
import time as t
from asyncio import timeout
import requests as rq
import json




def checkConnect():
    try:
        print("Connecting...")
        connecttime = t.time()
        response = rq.get("https://www.google.com", timeout=5)
        print("\n" * 100)
        print("Connected to Google in", round((t.time() - connecttime), 3), "s")
        try:
            apiconnect1 = t.time()
            responseapi = rq.get("http://ip-api.com", timeout=5)
            responseapi.raise_for_status()
            print("Connected to IP-API in", round((t.time() - apiconnect1), 3), "s")
        except responseapi.status_code!=200:
            print(f"Ip-API response: {response}", "Status code:", response.status_code)

    except rq.ConnectionError:
        print("Connection Error. Check your internet connection and try again.")
        sys.exit(1)
checkConnect()

def getInfo1(ip):
    url = f"http://ip-api.com/json/{ip}?fields=17035263"
    try:
        response = rq.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get("status") == "fail":
            print(f"{'No information for':<30} {ip}")
            print(f"{'IP-API Response:':<30} {data.get('message'):>10}")
            return

        print("IP-API RESPONSE FOR:", ip)
        print("="*50)
        #todisplay = {"key":"value"}
        weCANfuckingread = {
            "as": "ASN and organization",
            "isp": "ISP",
            "country": "Country",
            "countryCode": "Country Code",
            "region": "Region Code",
            "regionName": "Region",
           #ripdistrict
            "lat": "Latitude",
            "lon": "Longitude",
        }

        for api_field, display_name in weCANfuckingread.items():
            if api_field in data and data[api_field]:
                value = data[api_field]
                if isinstance(value, list):
                    value = ', '.join(str(v) for v in value)
                print(f"{display_name:<30}: {value}")
            else:
                print(f"{display_name:<30}: {'N/A'}")

        print("="*50)

        if data.get("proxy") == True:
            print("This domain is a proxy, VPN, or TOR exit address.")
        elif data.get("hosting") == True:
            print("This domain is a hosting exit address.")
        elif data.get("mobile") == True:
            print("This domain is a cellular connection exit address.")
        return

    except rq.exceptions.RequestException as err:
        print("Error getting data:", err)
    except json.JSONDecodeError as err:
        print("Error reading JSON: ", err)
        print("Oh no! Our API! It's broken! :(")
    except Exception as err:
        print("Unexpected error:", err)
    except response.status_code!=200:
        print(f"API response: {response}", "Status code:", response.status_code)


if __name__ == "__main__":
    recip = input("Input IP/domain: ")
    print("="*50)
    getInfo1(recip)
    # getInfo2(recip)
    print("="*50)

