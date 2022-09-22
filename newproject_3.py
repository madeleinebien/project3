import requests

#Get the user's current IP Address using API64 API
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]

#Get the ip, ip version, city, region, country, and country code of the user's current IP Address using IPAPI API 
def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = { 
        #Get the IP Address
        "ip": ip_address,
        #Get the Version of the IP  Address
        "version": response.get("version"),
        #Get the city of the IP Address
        "city": response.get("city"),
        #Get the region of the IP Address
        "region": response.get("region"),
        #Get the country of the IP Address
        "country": response.get("country_name"),
        #Get the country code of the IP Address
        "country_code": response.get("country_code")
        
        
    }
    return location_data


print(get_location())
