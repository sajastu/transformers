import argparse
import sys
import urllib.request
from getfilelistpy import getfilelist
from os import path, makedirs, remove, rename

def download_googledrive_folder(remote_folder, local_dir, gdrive_api_key=None, debug_en=None):

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
            if not path.exists(destination):
                makedirs(destination)
            for file_dict in res['fileList'][0]['files']:
                print('Downloading %s' % file_dict['name'])
                if gdrive_api_key:
                    source = "https://www.googleapis.com/drive/v3/files/%s?alt=media&key=%s" % (file_dict['id'], gdrive_api_key)
                else:
                    source = "https://drive.google.com/uc?id=%s&export=download" % file_dict['id']  # only works for small files (<100MB)
                destination_file = path.join(destination, file_dict['name'])
                urllib.request.urlretrieve(source, destination_file)

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