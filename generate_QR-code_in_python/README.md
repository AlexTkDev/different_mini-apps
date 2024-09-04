## Project: QR Code Generation

#### Project Description
This project is a simple application for generating QR codes using the `qrcode` and `Pillow (PIL)`
libraries. The application features a graphical user interface that allows users to enter or paste 
text to generate a QR code based on that text. The generated QR code is saved as an image and 
displayed within the application window.

#### Key Features
- **QR Code Generation:**
  - Users can input text or paste copied text from the clipboard to create a QR code through the graphical interface.
  - The size and parameters of the QR code can be adjusted using version, error_correction, box_size, and border settings.
  - The generated QR code image is saved in PNG format and displayed in the application window.
  
- **Clipboard Integration:**
  - Users can paste text directly from the clipboard into the text entry field using the "Paste from Clipboard" button.
  
- **Notification System:**
  - Users are notified with a success message once the QR code is successfully generated and saved.

#### Requirements
The project requires the following dependencies:
- `Python 3.x`
- `qrcode`
- `Pillow (PIL)`

You can install all dependencies by running:
```sh
  pip install -r requirements.txt
```

#### How to Use
1. **QR Code Generation:**
   - Run the application.
   - Enter the text you want to encode in the QR code into the text entry field, or click the "Paste from Clipboard" button to insert copied text.
   - Click the "Generate QR Code" button.
   - The QR code will be generated, saved as `QR-code.png`, and displayed in the application window.

2. **Clipboard Integration:**
   - Click the "Paste from Clipboard" button to paste any copied text into the text entry field from the system clipboard.

#### License
This project is licensed under the MIT License. You are free to use, copy, modify, and distribute 
the code under the terms of this license.

---

## Проект: Генератор QR-кодов

#### Описание проекта
Этот проект представляет собой простое приложение для генерации QR-кодов с использованием 
библиотек `qrcode` и `Pillow (PIL)`. Приложение имеет графический интерфейс, который позволяет 
пользователям вводить или вставлять текст для создания QR-кода на основе этого текста. 
Сгенерированный QR-код сохраняется в виде изображения и отображается в окне приложения.

#### Основные функции
- **Генерация QR-кодов:**
  - Пользователи могут ввести текст или вставить скопированный текст из буфера обмена в графический интерфейс для создания QR-кода.
  - Размер и параметры QR-кода могут быть настроены с помощью версии, уровня коррекции ошибок, размера ячейки и границы.
  - Сгенерированный QR-код сохраняется в формате PNG и отображается в окне приложения.
  
- **Интеграция с буфером обмена:**
  - Пользователи могут вставлять текст прямо из буфера обмена в поле ввода текста с помощью кнопки "Вставить из буфера обмена".
  
- **Система уведомлений:**
  - После успешной генерации и сохранения QR-кода пользователи получают уведомление с подтверждением.

#### Требования
Для работы проекта необходимы следующие зависимости:
- `Python 3.x`
- `qrcode`
- `Pillow (PIL)`

Все зависимости можно установить с помощью команды:
```sh
  pip install -r requirements.txt
```

#### Как пользоваться
1. **Генерация QR-кода:**
   - Запустите приложение.
   - Введите текст, который вы хотите закодировать в QR-код, в поле ввода текста, или нажмите кнопку "Вставить из буфера обмена", чтобы вставить скопированный текст.
   - Нажмите кнопку "Генерировать QR-код".
   - QR-код будет сгенерирован, сохранен как `QR-code.png` и отображен в окне приложения.

2. **Интеграция с буфером обмена:**
   - Нажмите кнопку "Вставить из буфера обмена", чтобы вставить любой скопированный текст в поле ввода из системного буфера обмена.

#### Лицензия
Этот проект лицензируется под лицензией MIT. Вы можете использовать, копировать, изменять и 
распространять код на условиях этой лицензии.
