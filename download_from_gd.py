import argparse
import shutil
import sys
import urllib.request
from getfilelistpy import getfilelist
from os import path, makedirs, remove, rename
import requests

def download_googledrive_folder(remote_folder, local_dir, gdrive_api_key='AIzaSyDoB_1pkJ0zn-l_t99_uk8EqGlAtEC0_VA', debug_en=None):

    success = True

    if debug_en:
        print('[DEBUG] Downloading: %s --> %s' % (remote_folder, local_dir))
    else:
        try:
            resource = {
                "api_key": gdrive_api_key,
                "id": remote_folder.split('/')[-1].split('?')[0],
                "fields": "files(name,id)",
            }
            res = getfilelist.GetFileList(resource)
            print('Found #%d files' % res['totalNumberOfFiles'])
            destination = local_dir
            # hdr = {
            #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            #     'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            #     'Accept-Encoding': 'none',
            #     'Accept-Language': 'en-US,en;q=0.8',
            #     'Connection': 'keep-alive'}
            # opener = urllib.request.build_opener()
            # opener.addheaders = hdr.items()
            # urllib.request.install_opener(opener)

            for j, file_dict in enumerate(res['fileList']):
                if len(file_dict['files']) > 0:
                    folder_name = f'checkpoint-{((j-2) + 1) * 10000}'
                    if not path.exists(destination + '/' + folder_name):
                        makedirs(destination + '/' + folder_name)
                    print(f'Downloading items for {folder_name}')
                    for file in file_dict['files']:

                        print('Downloading %s' % file['name'])
                        if gdrive_api_key:
                            source = "https://www.googleapis.com/drive/v3/files/%s?alt=media&key=%s" % (file['id'], gdrive_api_key)
                        else:
                            source = "https://drive.google.com/uc?id=%s&export=download" % file['id']  # only works for small files (<100MB)
                        destination_file = path.join(destination, folder_name, file['name'])
                        try:

                            r = requests.get(source, stream=True)
                            if r.status_code == 200:
                                with open(destination_file, 'wb') as f:
                                    r.raw.decode_content = True
                                    shutil.copyfileobj(r.raw, f)

                            # urllib.request.urlretrieve(source, destination_file)
                        except Exception as err:
                            print(err)
                            continue

        except Exception as err:
            print(err)
            success = False

    return success

if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument("-url", type=str, required=True)
    # parser.add_argument("-out_path", type=str, required=True)
    # args = parser.parse_args()
    url, local_dir = sys.argv[1], sys.argv[2]
    download_googledrive_folder(url, local_dir)