from Dowload import DownloadFunction


if __name__ == '__main__':
    name = input('Nombre del video: ')

    search = DownloadFunction.search_video(name)
    
    download = DownloadFunction.download_video(search[0]['id'])
