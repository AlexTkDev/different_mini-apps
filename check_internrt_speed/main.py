import speedtest as st
from tqdm import tqdm
import threading
import time


def show_progress_bar(description, stop_event):
    """Функция для отображения прогресс-бара."""
    with tqdm(desc=description, total=100) as pbar:
        while not stop_event.is_set():
            if pbar.n < 99:
                pbar.update(1)
            time.sleep(0.1)  # Скорость обновления прогресс-бара
        # Устанавливаем прогресс на 100% после завершения замера
        pbar.n = pbar.total
        pbar.refresh()


def perform_speedtest():
    """Выполняет замеры скорости интернета."""
    try:
        test = st.Speedtest()

        # Прогресс-бар для загрузки
        download_stop_event = threading.Event()
        download_thread = threading.Thread(target=show_progress_bar,
                                           args=("Testing download speed", download_stop_event))
        download_thread.start()
        down_speed = test.download()
        download_stop_event.set()  # Останавливаем прогресс-бар после завершения замера
        download_thread.join()

        # Прогресс-бар для выгрузки
        upload_stop_event = threading.Event()
        upload_thread = threading.Thread(target=show_progress_bar,
                                         args=("Testing upload speed", upload_stop_event))
        upload_thread.start()
        up_speed = test.upload()
        upload_stop_event.set()  # Останавливаем прогресс-бар после завершения замера
        upload_thread.join()

        ping = test.results.ping

        return round(down_speed / 10 ** 6, 2), round(up_speed / 10 ** 6, 2), ping
    except Exception as e:
        print("Error performing speed test:", e)
        return None, None, None


def display_results(down_speed, up_speed, ping):
    if down_speed is None or up_speed is None or ping is None:
        print("Speed test failed. Please check your internet connection.")
    else:
        print(f"\nDownload speed: {down_speed} Mbps")
        print(f"Upload speed: {up_speed} Mbps")
        print(f"Ping: {ping} ms")


def main():
    down_speed, up_speed, ping = perform_speedtest()
    display_results(down_speed, up_speed, ping)


if __name__ == "__main__":
    main()
