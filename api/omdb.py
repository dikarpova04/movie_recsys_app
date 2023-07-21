import requests
from typing import Optional, List


class OMDBApi:

    def __init__(self, api_key):
        self.api_key = api_key
        self.url = "https://www.omdbapi.com"

    def _images_path(self, title: str) -> Optional[str]:
        api_url = f'{self.url}?apikey={self.api_key}&t={title}'
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            poster_url = data.get("Poster")
            if poster_url:
                return poster_url
            else:
                return 'Poster not available'
        else:
            return f'Error while processing: {response.status_code}'


    def get_posters(self, titles: List[str]) -> List[str]:
        posters = []
        for title in titles:
            path = self._images_path(title)
            if path:  # If image isn`t exist
                posters.append(path)
            else:
                posters.append('assets/none.jpeg')  # Add plug

        return posters

