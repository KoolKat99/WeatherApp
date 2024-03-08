import requests
import json
import geopy
from geopy.geocoders import Nominatim




def get_current_location():
    geolocator = Nominatim(user_agent="my_geocoder")
    #location = geolocator.geocode("")
    location = geolocator.geocode("1202 Sidonia st CA")

    if location:
        latitude, longitude = location.latitude, location.longitude
        return latitude, longitude
    else:
        return None


def write_to_json(data, filename):
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)




def main():

    try:
        latitude, longitude = get_current_location()
        print(latitude, longitude)
    except Exception as e:
        print(e)


    """[\"AKQ\",\"ALY\",\"BGM\",\"BOX\",\"BTV\",\"BUF\",\"CAE\",\"CAR\",\"CHS\",\"CLE\",\"CTP\",
    \"GSP\",\"GYX\",\"ILM\",\"ILN\",\"LWX\",\"MHX\",\"OKX\",\"PBZ\",\"PHI\",\"RAH\",\"RLX\",\"RNK\",
    \"ABQ\",\"AMA\",\"BMX\",\"BRO\",\"CRP\",\"EPZ\",\"EWX\",\"FFC\",\"FWD\",\"HGX\",\"HUN\",\"JAN\",
    \"JAX\",\"KEY\",\"LCH\",\"LIX\",\"LUB\",\"LZK\",\"MAF\",\"MEG\",\"MFL\",\"MLB\",\"MOB\",\"MRX\",
    \"OHX\",\"OUN\",\"SHV\",\"SJT\",\"SJU\",\"TAE\",\"TBW\",\"TSA\",\"ABR\",\"APX\",\"ARX\",\"BIS\",
    \"BOU\",\"CYS\",\"DDC\",\"DLH\",\"DMX\",\"DTX\",\"DVN\",\"EAX\",\"FGF\",\"FSD\",\"GID\",\"GJT\",
    \"GLD\",\"GRB\",\"GRR\",\"ICT\",\"ILX\",\"IND\",\"IWX\",\"JKL\",\"LBF\",\"LMK\",\"LOT\",\"LSX\",
    \"MKX\",\"MPX\",\"MQT\",\"OAX\",\"PAH\",\"PUB\",\"RIW\",\"SGF\",\"TOP\",\"UNR\",\"BOI\",\"BYZ\",
    \"EKA\",\"FGZ\",\"GGW\",\"HNX\",\"LKN\",\"LOX\",\"MFR\",\"MSO\",\"MTR\",\"OTX\",\"PDT\",\"PIH\",
    \"PQR\",\"PSR\",\"REV\",\"SEW\",\"SGX\",\"SLC\",\"STO\",\"TFX\",\"TWC\",\"VEF\",\"AER\",\"AFC\",
    \"AFG\",\"AJK\",\"ALU\",\"GUM\",\"HPA\",\"HFO\",\"PPG\",\"STU\",\"NH1\",\"NH2\",\"ONA\",\"ONP\"]"""

    #print(latitude, longitude)
        
    #https://api.weather.gov/gridpoints/SGX/55,30/forecast

    #office = "SGX"

    
    #im not sure why this is even an option???
    #api_URL = f"https://api.weather.gov/gridpoints/{office}/{latitude},{longitude}/forecast"

    api_URL = "https://api.weather.gov/zones/forecast/CAZ043/forecast"

    response = requests.get(api_URL)


    if response.status_code == 200:
        data = response.json()
        
        #print(data)
        write_to_json(data, "NWS_Weather_Report.json")
    else:
        print(f"Error: {response.status_code}, {response.text}")



if __name__ == '__main__':
    main()

