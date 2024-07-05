import yt_dlp
import os

def download_video(url, successful_downloads, failed_urls, print_info=False):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': './video/%(title)s.%(ext)s',  # Сохранить видео в папку video в корневой папке проекта
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if print_info:
                formats = info.get('formats', [info])
                print(f"Доступные форматы для {url}:")
                for f in formats:
                    print(f"Format: {f.get('format_id')}, Extension: {f.get('ext')}, Resolution: {f.get('resolution')}, Note: {f.get('format_note')}, File Size: {f.get('filesize', 'N/A')}")
            
            title = info['title']
            ydl.download([url])
            print(f"Видео '{title}' успешно скачано.")
            successful_downloads.append(url)
    except Exception as e:
        print(f"Ошибка при скачивании видео по ссылке {url}: {str(e)}")
        failed_urls.append(url)

def download_videos_from_file(file_path, print_info=False):
    successful_downloads = []
    failed_urls = []

    with open(file_path, 'r') as f:
        urls = f.readlines()
    
    for url in urls:
        download_video(url.strip(), successful_downloads, failed_urls, print_info)

    print(f"\nУспешно скачано видео: {len(successful_downloads)}")
    print("Не удалось скачать следующие видео:")
    for url in failed_urls:
        print(url.strip())

def main():
    print("Выберите режим скачивания:")
    print("1. Скачать по ссылке")
    print("2. Скачать из list.txt")
    print("3. Скачать с выбором вывода информации о разрешении")
    
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
    elif choice == '3':
        print("Выберите способ скачивания:")
        print("1. Скачать по ссылке")
        print("2. Скачать из list.txt")
        download_choice = input("Введите номер способа скачивания: ")

        print("Вывести информацию о разрешении? (y/n)")
        print_info_choice = input().lower() == 'y'
        
        if download_choice == '1':
            url = input("Введите ссылку для скачивания: ")
            successful_downloads = []
            failed_urls = []
            download_video(url, successful_downloads, failed_urls, print_info_choice)
            print(f"\nУспешно скачано видео: {len(successful_downloads)}")
            if failed_urls:
                print("Не удалось скачать следующие видео:")
                for url in failed_urls:
                    print(url)
        elif download_choice == '2':
            file_path = 'list.txt'  # Укажите путь к файлу list.txt
            download_videos_from_file(file_path, print_info_choice)
        else:
            print("Неверный выбор. Пожалуйста, выберите 1 или 2.")
    else:
        print("Неверный выбор. Пожалуйста, выберите 1, 2 или 3.")

if __name__ == "__main__":
    main()
