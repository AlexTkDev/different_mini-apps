### CAPTCHA Generation Script Documentation

#### Description
This script generates CAPTCHA images with random text. The CAPTCHA text consists of uppercase letters and digits. The generated image is saved to a specified file path.

#### Installation of Dependencies
The script requires the following packages:
- `captcha`: to generate CAPTCHA images
- `Pillow (PIL)`: to work with images

Create a `requirements.txt` file with the following dependencies:
```text
captcha==0.4
Pillow==9.2.0
```

##### Installing Dependencies:
1. Ensure you have Python 3.6 or higher installed.
2. Install the dependencies using `pip`:

```bash
pip install -r requirements.txt
```

#### How to Use the Script
Once the dependencies are installed, you can run the script to generate a CAPTCHA image.

##### Example Usage:
1. **Default Usage**:
   Generate a CAPTCHA with a default length of 10 characters, image size 500x100 pixels, and save it to `CAPTCHA.png`:
   ```bash
   python captcha_generator.py
   ```

2. **Specify CAPTCHA Length**:
   Generate a CAPTCHA with a text length of 6 characters:
   ```bash
   python captcha_generator.py --length 6
   ```

3. **Change Image Size**:
   Generate a CAPTCHA with 8 characters, an image size of 400x120 pixels:
   ```bash
   python captcha_generator.py --length 8 --width 400 --height 120
   ```

4. **Save CAPTCHA to a Different Path**:
   Generate a CAPTCHA with 6 characters and save the file to a specific directory:

   ```bash
   python captcha_generator.py --length 6 --save_path ./output/captcha_image.png
   ```

   If the `output` directory does not exist, the script will create it automatically.

5. **Complex Example**:
   Generate a CAPTCHA with 8 characters, image size 600x150 pixels, and save the file to `./images/captcha.png`:
   ```bash
   python captcha_generator.py --length 8 --width 600 --height 150 --save_path ./images/captcha.png
   ```

#### Parameter Description
- `--length`: The length of the CAPTCHA text (default: 10 characters). You can specify any integer.
- `--width`: The width of the CAPTCHA image in pixels (default: 500).
- `--height`: The height of the CAPTCHA image in pixels (default: 100).
- `--save_path`: The file path to save the CAPTCHA image (default: `CAPTCHA.png`). If the directory does not exist, it will be created automatically.

#### Logging
The script uses standard logging to output information about the process:
- Successful CAPTCHA file creation.
- Errors during image generation or file saving.

#### Example Log Output:
```bash
INFO:root:Captcha successfully saved to ./output/captcha_image.png
INFO:root:Captcha text: X7C9D2
```
---

### Документация для скрипта генерации CAPTCHA
Этот скрипт генерирует изображения CAPTCHA с произвольным текстом. Текст CAPTCHA состоит из заглавных букв и цифр. Изображение сохраняется в указанный файл.

#### Установка зависимостей
Для работы скрипта требуются следующие пакеты:
- `captcha`: для генерации изображения CAPTCHA
- `Pillow (PIL)`: для работы с изображениями

Создайте файл `requirements.txt` со следующими зависимостями:
```text
captcha==0.4
Pillow==9.2.0
```

##### Установка зависимостей:
1. Убедитесь, что у вас установлен Python версии 3.6 или выше.
2. Установите зависимости с помощью `pip`:
```bash
pip install -r requirements.txt
```

#### Как использовать скрипт
После установки зависимостей вы можете запустить скрипт для генерации CAPTCHA.

##### Примеры вызова:
1. **По умолчанию**:
   Сгенерировать CAPTCHA длиной 10 символов с изображением размером 500x100 пикселей и сохранить в файл `CAPTCHA.png`:
   ```bash
   python captcha_generator.py
   ```

2. **С указанием длины CAPTCHA**:
   Сгенерировать CAPTCHA длиной 6 символов:
   ```bash
   python captcha_generator.py --length 6
   ```

3. **Изменение размеров изображения**:
   Сгенерировать CAPTCHA с длиной текста 8 символов, изображением размером 400x120 пикселей:
   ```bash
   python captcha_generator.py --length 8 --width 400 --height 120
   ```

4. **Сохранение CAPTCHA в другой путь**:
   Сгенерировать CAPTCHA длиной 6 символов и сохранить файл в указанную директорию:
   ```bash
   python captcha_generator.py --length 6 --save_path ./output/captcha_image.png
   ```

   Если директория `output` не существует, скрипт создаст её автоматически.

5. **Комплексный пример**:
   Сгенерировать CAPTCHA длиной 8 символов, изображением размером 600x150 пикселей, и сохранить файл в `./images/captcha.png`:
   ```bash
   python captcha_generator.py --length 8 --width 600 --height 150 --save_path ./images/captcha.png
   ```

#### Описание параметров
- `--length`: Длина текста CAPTCHA (по умолчанию: 10 символов). Можно указать любое целое число.
- `--width`: Ширина изображения CAPTCHA в пикселях (по умолчанию: 500).
- `--height`: Высота изображения CAPTCHA в пикселях (по умолчанию: 100).
- `--save_path`: Путь для сохранения изображения (по умолчанию: `CAPTCHA.png`). Если директория не существует, она будет создана автоматически.

#### Логирование
Скрипт использует стандартное логирование для вывода информации о ходе выполнения:
- Успешное сохранение CAPTCHA.
- Ошибки при генерации изображения или создании файлов.

#### Пример вывода логов:
```bash
INFO:root:Captcha успешно сохранена в ./output/captcha_image.png
INFO:root:Captcha text: X7C9D2
```
