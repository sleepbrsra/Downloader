import yt_dlp
import os

def download_video(url, successful_downloads, failed_urls):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': './video/%(title)s.%(ext)s',  # Сохранить видео в папку video в корневой папке проекта
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info['title']
            ydl.download([url])
            print(f"Видео '{title}' успешно скачано.")
            successful_downloads.append(url)
    except Exception as e:
        print(f"Ошибка при скачивании видео по ссылке {url}: {str(e)}")
        failed_urls.append(url)

def download_videos_from_file(file_path):
    successful_downloads = []
    failed_urls = []

    with open(file_path, 'r') as f:
        urls = f.readlines()
    
    for url in urls:
        download_video(url.strip(), successful_downloads, failed_urls)

    print(f"\nУспешно скачано видео: {len(successful_downloads)}")
    print("Не удалось скачать следующие видео:")
    for url in failed_urls:
        print(url.strip())


def main():
    print("Выберите режим скачивания:")
    print("1. Скачать по ссылке")
    print("2. Скачать из list.txt")
    
    choice = input("Введите номер режима: ")
    
    if choice == '1':
        url = input("Введите ссылку для скачивания: ")
        successful_downloads = []
        failed_urls = []
        download_video(url, successful_downloads, failed_urls)
        print(f"\nУспешно скачано видео: {len(successful_downloads)}")
        if failed_urls:
            print("Не удалось скачать следующие видео:")
            for url in failed_urls:
                print(url)
    elif choice == '2':
        file_path = 'list.txt'  # Укажите путь к файлу list.txt
        download_videos_from_file(file_path)
    else:
        print("Неверный выбор. Пожалуйста, выберите 1 или 2.")


if __name__ == "__main__":
    main()
