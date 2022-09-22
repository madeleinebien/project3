import requests

#Get the user's current IP Address using API64 API
def get_ip():
    response = requests.get('https://api64.ipify.org?format=json').json()
    return response["ip"]


def get_location():
    ip_address = get_ip()
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = { 
        "ip": ip_address,
        "version": response.get("version"),
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name"),
        "country_code": response.get("country_code")
        
        
    }
    return location_data


print(get_location())

def get_current_ipv6():
    try:
        return requests.get("https://api6.ipify.org", timeout=5).text
    except requests.exceptions.ConnectionError as ex:
        return None

print(get_current_ipv6())
  