### Project: QR Code Generation and Reading

#### Project Description
This project is a simple application for creating and reading QR codes using 
the `qrcode` and `opencv-python` (OpenCV) libraries. The program generates a QR code based on
provided data, saves it as an image, and then reads and decodes the data from that image.

#### Key Features:
1. **QR Code Generation**:
   - Users can input data to create a QR code.
   - The size and parameters of the QR code can be adjusted through `version`, `error_correction`, `box_size`, and `border` settings.
   - The generated QR code image is saved in PNG format.

2. **QR Code Reading**:
   - The program loads the saved image and decodes the data from the QR code.
   - It displays the decoded data and the coordinates of the QR code's bounding box.
   - If the QR code is successfully recognized, it is displayed on the screen.

#### Requirements
The project requires the following dependencies:

`Python 3.x`, `qrcode`, `opencv-python`

You can install all dependencies by running the command:

```bash
pip install -r requirements.txt
```

#### How to Use
1. **QR Code Generation**:
   - Edit the line `qr.add_data('Some data')` to specify the data you want to encode in the QR code.
   - Run the program to generate and save the QR code.

2. **QR Code Reading**:
   - Run the program to recognize the QR code from the generated image.
   - If the QR code is successfully recognized, it will be displayed on the screen, and the data will be printed to the console.

#### License
This project is licensed under the MIT License. You are free to use, copy, modify, and distribute 
the code under the terms of this license.

***

### Проект: Генерация и чтение QR-кодов

#### Описание проекта
Этот проект представляет собой простое приложение для создания и чтения QR-кодов с использованием 
библиотек `qrcode` и `opencv-python` (OpenCV). Программа генерирует QR-код на основе 
предоставленных данных, сохраняет его как изображение, а затем считывает и декодирует данные из 
этого изображения.

#### Основные возможности:
1. **Генерация QR-кода**:
   - Пользователь может задавать данные для создания QR-кода.
   - Размер и параметры QR-кода настраиваются через параметры `version`, `error_correction`, `box_size` и `border`.
   - Генерируемое изображение QR-кода сохраняется в формате PNG.

2. **Чтение QR-кода**:
   - Программа загружает сохраненное изображение и декодирует данные из QR-кода.
   - Выводит данные и координаты рамки QR-кода.
   - Отображает QR-код, если он был успешно распознан.

#### Требования
Для работы проекта необходимы следующие зависимости:

`Python 3.x`, `qrcode`,`opencv-python`

Вы можете установить все зависимости, выполнив команду:

```bash
pip install -r requirements.txt
```

#### Как использовать
1. **Генерация QR-кода**:
   - Отредактируйте строку `qr.add_data('Some data')`, указав данные, которые вы хотите закодировать в QR-код.
   - Запустите программу для генерации и сохранения QR-кода.

2. **Чтение QR-кода**:
   - Запустите программу, чтобы распознать QR-код из сгенерированного изображения.
   - Если QR-код успешно распознан, он будет отображен на экране, а данные будут выведены в консоль.

#### Лицензия
Этот проект распространяется под лицензией MIT. Вы можете использовать, копировать, 
изменять и распространять код в соответствии с условиями этой лицензии.

---