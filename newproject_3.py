import requests
import socket
from requests import get

# API data's URL and API key for access
BASE_URL = "http://api.ipstack.com/"
API_KEY = "?access_key=5e9135d065d6ffcebcb24622c4ea84ea"

def main():
    #For Loop for User's Choice 
    while True:
        #Asks users to input their choice
        print(f"Please input your choice: ")
        #Asks if user want to manually input an IP Address
        print(f"M - Input manually an IP Address")
        #Asks if the user wants to automatically retrieve their IP Address
        print(f"A - Automatically get your IP Address")
        #Terminates the system
        print(f"Q - Quit")
        choice_user = input("Enter: ")

        # Get the device's IP address through the API's website 
        if choice_user == "A" or choice_user == "a":
            ip_address = get('https://api.ipify.org').content.decode('utf8')
            get_location(ip_address)
        # User Manually enters an IP Address
        elif choice_user == "M" or choice_user == "m":
            ip_address = input("Enter an IP address: ")
        #Requests the information of the IP Address through the API
            get_location(ip_address)
        # Terminates the system
        elif choice_user == "Q" or choice_user == "q":
            break
        # User input is invalid
        else:
            continue

def get_location(choice_user):
    try:
        # Validates if IPV4/IPV6 Address is valid
        socket.inet_aton(choice_user)
        # Request from the API 
        api_request = BASE_URL + choice_user + API_KEY
        data = requests.get(api_request).json()

        # Displays the data output
        print()
        #Displays the IP Address
        print(f"IP Address: {(data['ip'])}")
        #Displays the type of the IP Address (IPV4/IPV6)
        print(f"Version: {(data['type'])}")
        #Displays the continent name based on the IP Address
        print(f"Continent: {(data['continent_name'])}")
        #Displays the country name based on the IP Address
        print(f"Country Name: {(data['country_name'])}")
        #Displays the country code based on the IP Address
        print(f"Country Code: {(data['country_code'])}")
        #Displays the region code based on the IP Address
        print(f"Region Code: {(data['region_code'])}")
        #Displays the region name based on the IP Address
        print(f"Region Name: {(data['region_name'])}")
        #Displays the city based on the IP Address
        print(f"City: {(data['city'])}")
        #Displays the zip code based on the IP Address
        print(f"Zip Code: {(data['zip'])}")
        #Added Data Outputs:
        #Displays the latitude of the IP Address
        print(f"Latitude: {(data['latitude'])}")
        #Displays the longitude of the IP Address
        print(f"Longitude: {(data['longitude'])}")
        #Displays the location of the IP Address
        print(f"Location: {(data['location'])}")
        print()

    # An error message if IP Address is not valid
    except socket.error:
        print("Error! IP Address is not valid.")

if __name__=="__main__":
    main()