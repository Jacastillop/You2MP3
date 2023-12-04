# Adaptado de https://dev.to/stokry/download-youtube-video-to-mp3-with-python-26p
import definitions as yt

if __name__ == "__main__":
    path = "C:/Users/jhona/Documents/YoutubeMP3/Canciones"
    totalCanciones = 0

    with open("C:/Users/jhona/Documents/AnalisisSpotify/canciones.txt", "r") as canciones:
        for nombre in canciones:
            totalCanciones += 1
            url = yt.search(f"{nombre.rstrip()} ")
            yt.download_MP3(url, path, nombre.rstrip())
    
    print(f"Total canciones descargadas: {totalCanciones}")