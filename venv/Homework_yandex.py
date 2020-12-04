import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        HEADERS = {'Authorization':f'OAuth {self.token}'}
        resp1 = requests.get(
            'https://cloud-api.yandex.net/v1/disk/resources/upload',
            params={'path':file_path, 'overwrite':'true'},
            headers=HEADERS,
        )
        resp1.raise_for_status()
        data = resp1.json()
        href = data['href']
        with open(file_path, 'rb') as f:
            resp2 = requests.put(href, files={'file': f})
        resp2.raise_for_status()
        return 'Загрузка произошла успешно'


if __name__ == '__main__':
    uploader = YaUploader(token)
    result = uploader.upload(file_path)
    print(result)

