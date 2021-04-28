import requests

class ThumbSnapClient:

    def __init__(self, key):
        self.api_key = key
        self.upload_url = "https://thumbsnap.com/api/upload"

    def upload_image(self, path):
        files = {
            'key': (None, self.api_key),
            'media': (path, open(path, 'rb'))
        }
        
        response = requests.post(self.upload_url, files=files)

        return response