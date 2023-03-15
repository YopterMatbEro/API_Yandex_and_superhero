import requests
from pprint import pprint


TOKEN = '...'
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_file_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        params = {'path': disk_file_path, 'overwrite': True}
        response = requests.get(upload_url, headers=headers, params=params)
        data = response.json()
        url_to_load = data.get('href')
        return url_to_load

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path)
        response = requests.put(href, data=open(filename, 'rb'))
        # response.raise_for_status()
        if response.status_code == 201:
            print('Success')

if __name__ == '__main__':
    ya = YaUploader(token=TOKEN)
    ya.upload_file_to_disk('/IMG_on_disk.jpg', 'IMG_4603.JPG')

