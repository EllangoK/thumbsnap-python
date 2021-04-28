import requests
import os

class ThumbSnapClient:
    def __init__(self, key):
        self.api_key = key
        self.upload_url = "https://thumbsnap.com/api/upload"
        self.valid_exts = ["jpg", "png", "jpeg", "gif", "mp4", "avi", "mov", "qt", "mkv", "webm"]

    def fix_path(self, path):
        path = path[:-2] if path.endswith('//') else path
        path = path[:-1] if path.endswith('/') else path

        path = path[:-2] if path.endswith("\\\\") else path
        path = path[:-1] if path.endswith("\\") else path

        path = path.encode('unicode_escape')
        return path

    def validate_file(self, path):
        path = self.fix_path(path)
        print(path)
        print(os.path.isfile(path), not os.path.isfile(path))

        if not os.path.isfile(path):
            raise FileNotFoundError

        filename = os.path.basename(path).decode("utf-8")
        ext = filename.split('.')[-1]

        if ext not in self.valid_exts:
            raise InvalidExtensionError

        return (filename, open(path, 'rb'))

    def upload_image(self, path):
        files = {
            'key': (None, self.api_key),
            'media': self.validate_file(path)
        }
        
        response = requests.post(self.upload_url, files=files)
        return response

    def upload_album_image(self, path, album):
        files = {
            'key': (None, self.api_key),
            'media': self.validate_file(path),
            'album': (None, album)
        }
        
        response = requests.post(self.upload_url, files=files)
        return response

class InvalidExtensionError(Exception):
    pass