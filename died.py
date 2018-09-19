from PIL import Image
# Используем функцию random для выбора картинки
import random
number = random.random()
# Функция отвечающая за вызов картинки
def show():
    if number > 0.5:
        img = Image.open('died.jpg')
    else:
        img = Image.open('safe.jpg')
    img.show()
show()
print(number)