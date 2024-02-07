import os
from PIL import Image

# Путь к папке с изображениями
folder = 'd:/test/'

# Получение списка файлов в папке
files = os.listdir(folder)
# Обход каждого файла в папке
def name(image_name):
    print(image_name)
for file in files:
    # Полный путь к файлу
    file_path = os.path.join(folder, file)
    
    # Проверка, является ли файл изображением
    if os.path.isfile(file_path) and file_path.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
        # Открытие изображения
        image = Image.open(file_path)
        
        # Пример обработки изображения - изменение размера
        new_image = image.resize((500, 500))
        
        # Сохранение обработанного изображения
        new_image.save(f'd:/test/small/{file}')
        name(file)
