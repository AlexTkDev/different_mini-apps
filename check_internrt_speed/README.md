# Project: Internet Speed Test
This project provides a simple way to measure internet connection speed with a progress bar displayed during the test. The project outputs download speed, upload speed, and ping.

## Functionality
- Measures **Download speed**, **Upload speed**, and **Ping** using the `speedtest` library.
- Displays an animated progress bar that lasts throughout the measurement and automatically completes at 100% when the test finishes.

## Installation

### Requirements
- Python version 3.7 or above
- Required libraries:
  - `speedtest-cli` - to measure internet speed
  - `tqdm` - to display the progress bar

### Installing Dependencies
1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # for Linux and macOS
   .venv\Scripts\activate     # for Windows
   ```

2.Install dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the script, execute the following command in the terminal:
```bash
python main.py
```

The script will start the measurement process and display results:
- **Download speed**: speed in Mbps
- **Upload speed**: speed in Mbps
- **Ping**: latency in milliseconds

Example output:
```
Testing download speed: 100%|███████████████████████████████████████████| 100/100 [00:10<00:00,  9.50it/s]
Testing upload speed: 100%|█████████████████████████████████████████████| 100/100 [00:10<00:00,  9.70it/s]

Download speed: 93.68 Mbps
Upload speed: 91.67 Mbps
Ping: 2.9 ms
```

## Code Structure
- **`show_progress_bar(description, stop_event)`**: Displays a progress bar with the provided description. Uses an `Event` object to complete at the end of the measurement and sets the bar to 100% once finished.
- **`perform_speedtest()`**: Runs the speed test using the `speedtest` library. `show_progress_bar` is called in separate threads for download and upload measurements.
- **`display_results(down_speed, up_speed, ping)`**: Formats and prints the results.
- **`main()`**: Main function that calls the speed test process and displays the results.

## Error Handling
- In case of errors, such as an unavailable internet connection or issues with the `speedtest` library, an error message will be displayed.

## Notes
This project can be further developed for automatic internet speed testing or real-time connection quality monitoring.

## License
This project is distributed under the MIT License.

***

# Проект: Измерение скорости интернет-соединения
Этот проект предоставляет простой способ замера скорости интернет-соединения, отображая прогресс выполнения с помощью анимированного прогресс-бара. С его помощью можно получить показатели загрузки, выгрузки и пинга.

## Функциональность
- Измерение **скорости загрузки** (Download speed) и **скорости выгрузки** (Upload speed) с использованием библиотеки `speedtest`.
- Определение значения **пинга** (Ping).
- Отображение прогресс-бара, который длится весь процесс замера и автоматически завершается на 100% по завершении замера.

## Установка

### Требования
- Python версии 3.7 или выше
- Установленные зависимости:
  - `speedtest-cli` - для замера скорости интернета.
  - `tqdm` - для отображения прогресс-бара.

### Установка зависимостей
1. Создайте виртуальное окружение и активируйте его:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # для Linux и macOS
   .venv\Scripts\activate     # для Windows
   ```

2. Установите зависимости из `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Использование
Для запуска скрипта выполните следующую команду в терминале:
```bash
python main.py
```
Скрипт начнёт процесс измерения и выведет результаты в виде:
- **Download speed**: скорость загрузки в Мбит/с
- **Upload speed**: скорость выгрузки в Мбит/с
- **Ping**: пинг в миллисекундах

Пример вывода:
```
Testing download speed: 100%|███████████████████████████████████████████| 100/100 [00:10<00:00,  9.50it/s]
Testing upload speed: 100%|█████████████████████████████████████████████| 100/100 [00:10<00:00,  9.70it/s]

Download speed: 93.68 Mbps
Upload speed: 91.67 Mbps
Ping: 2.9 ms
```

## Структура кода
- **`show_progress_bar(description, stop_event)`**: Отображает прогресс-бар для заданного описания. Использует объект `Event` для завершения при окончании замера. Останавливает прогресс-бара на 100% после завершения.
- **`perform_speedtest()`**: Выполняет тест скорости с помощью библиотеки `speedtest`. Вызов `show_progress_bar` осуществляется в отдельных потоках для замеров скорости загрузки и выгрузки.
- **`display_results(down_speed, up_speed, ping)`**: Форматирует и выводит результаты измерений.
- **`main()`**: Основная функция, которая вызывает процесс замера и выводит результаты.

## Исключения и ошибки
- При возникновении ошибок, например, отсутствии интернет-соединения или проблемах с библиотекой `speedtest`, на экране будет выведено сообщение об ошибке.

## Примечания
Проект можно доработать для использования в автоматических тестах скорости интернет-соединения или для мониторинга качества соединения в реальном времени.

## Лицензия
Этот проект распространяется под лицензией MIT.