import requests


class TMDBApi:

    def __init__(self, api_key):
        self.api_key = api_key

    def get_video_data(self, movie_id):
        base_url = "https://api.themoviedb.org/3/movie/"
        endpoint = f"{movie_id}/videos"
        params = {
            "api_key": self.api_key,
        }
        try:
            response = requests.get(base_url + endpoint, params=params)
            response.raise_for_status()
            data = response.json()
            return data["results"]
        except requests.exceptions.RequestException as e:
            print("Error:", e)
            return None