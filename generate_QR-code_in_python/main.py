import qrcode
import cv2

# Создаем объект QRCode с заданными параметрами
qr = qrcode.QRCode(
    version=1,  # Определяем размер QR-кода. Версия 1 создает минимальный QR-код.
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Уровень коррекции ошибок (L - Low)
    box_size=10,  # Размер каждого квадратика (бокселя) в пикселях
    border=4,  # Размер границы вокруг QR-кода (количество бокселей)
)

# Добавляем данные в QR-код
qr.add_data('Some data')  # Здесь можно заменить строку на нужные данные
qr.make(fit=True)  # Генерируем QR-код, подгоняя размеры

# Создаем изображение QR-кода с заданными цветами
img = qr.make_image(fill_color="black", back_color="white")
img.save('QR-code.png', 'PNG')  # Сохраняем изображение в файл

# Чтение QR-кода из изображения
img_qrcode = cv2.imread('QR-code.png')  # Загружаем изображение
detector = cv2.QRCodeDetector()  # Создаем объект для обнаружения и декодирования QR-кода

# Декодируем данные из QR-кода
data, bbox, clear_qr = detector.detectAndDecode(img_qrcode)
print(f'{data=}, {bbox=}')  # Выводим декодированные данные и координаты рамки

# Если QR-код был распознан, отображаем изображение QR-кода
if clear_qr is not None:
    cv2.imshow('QR-code', img_qrcode)  # Отображаем изображение QR-кода
    cv2.waitKey(0)  # Ждем нажатия любой клавиши
    cv2.destroyAllWindows()  # Закрываем все окна
else:
    print("QR-код не распознан")
