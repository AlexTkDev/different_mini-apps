from captcha.image import ImageCaptcha
from PIL import Image
import string
import random
import argparse
import logging
import os

# Настройка логирования
logging.basicConfig(level=logging.INFO)


def generate_text_captcha(length: int) -> str:
    """Генерирует текст для CAPTCHA"""
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


def generate_captcha(captcha_length: int = 10, width: int = 500, height: int = 100,
                     save_path: str = 'CAPTCHA.png') -> str:
    """Генерирует изображение CAPTCHA и сохраняет его"""
    try:
        image = ImageCaptcha(width=width, height=height)
        captcha_text = generate_text_captcha(captcha_length)
        image.write(captcha_text, save_path)
        logging.info(f"Captcha успешно сохранена в {save_path}")
        return captcha_text
    except Exception as e:
        logging.error(f"Ошибка при генерации CAPTCHA: {e}")
        return ""


def validate_save_path(path: str) -> str:
    """Проверяет валидность пути для сохранения файла. Создает директорию,
    если она не существует.
    """
    directory = os.path.dirname(path)
    if directory and not os.path.exists(directory):
        try:
            os.makedirs(directory)
            logging.info(f"Создана директория {directory}")
        except OSError as e:
            raise argparse.ArgumentTypeError(f"Невозможно создать директорию {directory}: {e}")
    return path


if __name__ == '__main__':
    # Парсер аргументов командной строки
    parser = argparse.ArgumentParser(description="Генератор CAPTCHA")
    parser.add_argument(
        '--length', type=int, default=10, help="Длина текста CAPTCHA")
    parser.add_argument(
        '--width', type=int, default=500, help="Ширина изображения CAPTCHA")
    parser.add_argument(
        '--height', type=int, default=100, help="Высота изображения CAPTCHA")
    parser.add_argument(
        '--save_path', type=validate_save_path, default='CAPTCHA.png',
        help="Путь для сохранения CAPTCHA")

    args = parser.parse_args()

    captcha = generate_captcha(args.length, args.width, args.height, args.save_path)
    if captcha:
        logging.info(f"Captcha text: {captcha}")
        Image.open(args.save_path).show()
