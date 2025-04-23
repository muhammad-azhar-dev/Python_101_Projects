"""
First Get your API key from https://opencagedata.com/
then Install these packages using pip:
# pip install requests
# pip install phonenumbers
# pip install opencage
# pip install folium
"""

import phonenumbers
import opencage
import folium
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
from dotenv import load_dotenv
import os

# load the environment variables from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")

def get_location_from_number(number):
    try:
        # parse the phone number
        parsed_number = phonenumbers.parse(number)

        # get the country code (e.g. +92 for Pakistan)
        location = geocoder.description_for_number(parsed_number, 'en')
        print(location)

        # get the service provider (Zong,Telenor, etc.)
        service_provider = carrier.name_for_number(parsed_number, 'en')
        print(service_provider)

        # get the location using OpenCage API
        open_cage_geocoder = OpenCageGeocode(API_KEY)
        query = str(location)
        result = open_cage_geocoder.geocode(query)
        # print(result)

        if result:
            lat = result[0]['geometry']['lat']
            lng = result[0]['geometry']['lng']
            print(lat, lng)

        myMap = folium.Map(location=[lat, lng], zoom_start=13)
        folium.Marker([lat, lng], popup=location).add_to(myMap)
        myMap.save("location.html")
        print("Map has been saved to location.html")
    except Exception as e:
        print(f"Error: {e}")
        return None
    
if __name__ == "__main__":
    # Example phone number
    print("-"*20, "Get location from phone number", "-"*20)
    phone_number = input("Enter the phone number with country code (e.g. +923001234567): ")
    if phone_number:
        get_location_from_number(phone_number)