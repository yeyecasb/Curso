import requests

class DigimonAPI:

    BASE_URL = "https://digimon-api.vercel.app/api/digimon"

    def __init__(self):
        pass

    def get_all_digimon(self):
        response = requests.get(self.BASE_URL)
        return response.json()

    def get_digimon_by_name(self, name):
        url = f"{self.BASE_URL}/name/{name}"
        response = requests.get(url)
        return response.json()

    def get_digimon_by_level(self, level):
        url = f"{self.BASE_URL}/level/{level}"
        response = requests.get(url)
        return response.json()