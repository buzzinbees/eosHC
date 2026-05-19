#include <iostream>
import time as t
import requests as rq
import json


def getInfo(ip):
    url = f"http://ip-api.com/json/{ip}"
    try:
        response = rq.get(url)
        response.raise_for_status()
        data = response.json()
        if data.get("status") == "fail":
            print("No information for: ", ip)
            print("Unknown error: ", data)
            return
        print("IP INFORMATION:")
        #todisplay = {"key":"value"}
        weCANfuckingread = {
            "query": "IP address",
            "hostname": "Host name",
            "as": "ASN",
            "isp": "ISP",
            "country": "Country",
            "countryCode": "Country Code",
            "region": "Region Code",
            "regionName": "Region",
            "city": "City",
            "lat": "Latitude",
            "lon": "Longitude",
            "timezone": "Timezone"
        }

        for api_field, display_name in weCANfuckingread.items():
            if api_field in data and data[api_field]:
                value = data[api_field]
                if isinstance(value, list):
                    value = ', '.join(str(v) for v in value)
                print(f"{display_name}: {value}")
            else:
                print(f"{display_name}: N/A")

    except rq.exceptions.RequestException as err:
        print("Error getting data:", err)
    except json.JSONDecodeError as err:
        print("Error reading JSON: ", err)
        print("Oh no! Our API! It's broken! :(")
    except Exception as err:
        print("Unexpected error:", err)


if __name__ == "__main__":
    recip = input("Input IP/domain: ")
    getInfo(recip)
