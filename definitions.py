from youtube_search import YoutubeSearch
import yt_dlp

def download_MP3(video_url,output_path="C:/",name=""):

    #video_info = yt_dlp.YoutubeDL().extract_info(url = video_url,download=False)
    #video_title = video_info['title'].replace("/", "IoI")
    #filename = f"{output_path}/{name}--{video_title}.mp3"
    filename = f"{output_path}/{name}.mp3"
    options={
        # 'ffmpeg_location': 'C:/ffmpeg/bin',
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':filename,
    #     'postprocessors': [{
    #         'key': 'FFmpegExtractAudio',
    #         'preferredcodec': 'mp3',
    #         'preferredquality': '320',
    # }]        
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        #ydl.download([video_info['webpage_url']])
        ydl.download(video_url)

    print(f"Download complete... {filename}")

def search(search_terms):
    results = YoutubeSearch(search_terms, max_results=1).to_dict()
    return f"https://www.youtube.com/{results[0]['url_suffix']}"

