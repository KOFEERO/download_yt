from pytube import YouTube
from youtube_search import YoutubeSearch

class DownloadFunction:
    @classmethod
    ############# (Metodo para buscar los videos, es la misma que usas en tu erp, solo la agregue para obtener el id del video) #############
    def search_video(self, name):
        results = YoutubeSearch(name, max_results=1).to_dict()
        return results
    

    @classmethod
    ############# (Metodo Youtube para que busque el video y que no requiera auntenticacion para descargar) #############
    def download_video(self, id_video):
        search_youtube = YouTube(
            f'https://www.youtube.com/watch?v={id_video}',
            use_oauth=False,
            allow_oauth_cache=True
            
        )
        ############# (Filtramos por el video con mas resolucion) #############
        video = search_youtube.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

        ############# (Aqui obtenemos el tag, representa la resolucion del video) #############
        video_tag = video.itag

        ############# (Comprobamos que sea el hd y el numero 22 representa la resolucion 720p = HD) #############
        if video_tag == 22:
            ############# (Filtramos el video con el tag 22) #############
            stream = search_youtube.streams.get_by_itag(video_tag)

            ############# (Descargamos el video) #############
            # Para descargar en otra ruta, debes agregarla en dentro del metodo download(ruta)
            stream.download()