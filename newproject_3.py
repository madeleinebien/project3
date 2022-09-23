import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "ezIgTjzAg29S6AWBUxAiS1MpB3qbTKdi"
#While loop that let's user choose to terminate the system
while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    #Get requests from the API 
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    json_data = requests.get(url).json()
    json_data = requests.get(url).json()
    #Retrieves the status code of the location and destination from the MapQuest API
    json_status = json_data["info"]["statuscode"]
    #If else based on the status code of the inputted location and destination 
    #0 indicates a successful route call
    if json_status == 0:
        print("______________________________________________")
        print("API Status: " + str(json_status) + " = A successful route call.")
        print("______________________________________________")
        print()
    #Displays the entered original location and destination in uppercase 
        message = "Directions from " + (orig)  + " to " + (dest)
        print(message.upper())
    #Displays the distance of the location and destination 
        print("Distance: " + str("{:.2f}".format((json_data["route"]["distance"])*3.78)))
    #Displays the duration of the trip in time format 
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
    #Displays the kilometers 
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
    #Displays the fuel used in Liters
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        
   

        print("=============================================")
        print()

        for each in json_data["route"]["legs"][0]["maneuvers"]:

            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    #402 indicates an invalid location
    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    #611 indicates that only one location has been entered by the user 
    elif json_status == 611:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    #500 indicates that there is an unknown error  
    elif json_status == 500:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Unknown Error.")
        print("**********************************************\n")
    #606 indicates that the user has exceeded the maximum number of locations 
    elif json_status == 606:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Exceeded the maximum search distance.")
        print("**********************************************\n")
    #612 indicates that there are no routes available for the entered locations 
    elif json_status == 612:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; There are no routes available for these locations.")
        print("**********************************************\n")
    else:

        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
        
  

   

  