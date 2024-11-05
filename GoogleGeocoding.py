import os
import googlemaps
import pandas as pd
from tabulate import tabulate

class GoogleGeocoding:
    def __init__(self):
        self.api_key = os.environ['GOOGLE_API_KEY']
   
    def validateInput(self,user_input):
        return user_input.strip()    
    
    def geocode(self, user_input):
        gmaps = googlemaps.Client(self.api_key)
        user_input = self.validateInput(user_input=user_input)
        geocoder_response = gmaps.geocode(user_input)
        return geocoder_response
            


    
