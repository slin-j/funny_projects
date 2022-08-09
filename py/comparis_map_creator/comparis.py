from geopy.geocoders import Nominatim

class advert:
    def __init__(self, address:str, link:str) -> None:
        self.address = address
        self.latlon = tuple()
        self.link = link
        self.address_to_geopoint()
        
    def address_to_geopoint(self):
        geolocator = Nominatim(user_agent="example app")
        data = geolocator.geocode(self.address).raw
        self.latlon = (float(data['lat']), float(data['lon']))
        del data, geolocator
        
    def get_latlon(self):
        return self.latlon
    
    def get_address(self):
        return self.address
    
    def get_link(self):
        return self.link
        
        