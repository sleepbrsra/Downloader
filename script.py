import yt_dlp

url = input("Введите ссылку для скачивания: ")  # Укажите URL видео

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',  # Загрузить видео в наилучшем доступном качестве
    'outtmpl': '%(title)s.%(ext)s',  # Сохранить видео с названием
    'noplaylist': True,  # Не загружать плейлисты
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
