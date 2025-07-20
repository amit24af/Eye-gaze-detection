import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
import io
from googleapiclient.http import MediaIoBaseDownload

SERVICE_ACCOUNT_INFO = os.environ.get('GDRIVE_SERVICE_ACCOUNT')

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

FILES_TO_DOWNLOAD = [
    ('1RhSYgXPlrNE--5TxkVQNZhDVrmUFJbBd', 'AnalizaDataseta.ipynb'),
    ('1F-aO-xXCIcC5MLHuQiYrYqRCb3sePkjh', 'Autism_Eyes.ipynb'),
]

def download_file(service, file_id, output_file):
    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(output_file, 'wb')
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Downloading {output_file}: {int(status.progress() * 100)}%")

def main():
    service_account_info = json.loads(SERVICE_ACCOUNT_INFO)
    creds = service_account.Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)

    for file_id, output_file in FILES_TO_DOWNLOAD:
        download_file(service, file_id, output_file)
        print(f"File {output_file} successfully downloaded.")

if __name__ == '__main__':
    main()
