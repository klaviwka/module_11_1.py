import requests
import numpy as np

# Замените 'user' и 'pass' на ваши учетные данные GitHub
r = requests.get('https://api.github.com', auth=('klaviwka', '487055Scd!'))

# Выводим статус-код и тип контента
print("Статус-код GitHub API:", r.status_code)
print("Тип контента:", r.headers['content-type'])

# Проверка доступности другого сайта, например, Google
response_google = requests.head('https://www.google.com')
if response_google.status_code == 200:
    print("Ресурс Google доступен.")
else:
    print("Ошибка при доступе к Google:", response_google.status_code)

# Создание массива чисел
array = np.array([1, 2, 3, 4, 5])

# Выполнение математических операций
array_squared = array ** 2          # Квадрат каждого элемента
array_sum = np.sum(array)           # Сумма всех элементов
array_mean = np.mean(array)         # Среднее значение
array_max = np.max(array)           # Максимальное значение
array_min = np.min(array)           # Минимальное значение

# Вывод результатов в консоль
print("Исходный массив:", array)
print("Квадраты элементов:", array_squared)
print("Сумма элементов:", array_sum)
print("Среднее значение:", array_mean)
print("Максимальное значение:", array_max)
print("Минимальное значение:", array_min)

# Выполняем запрос OPTIONS к httpbin.org
response = requests.options('https://httpbin.org/anything')

# Выводим статус-код и доступные методы
print("Статус-код:", response.status_code)
print("Заголовки ответа:")
for header, value in response.headers.items():
    print(f"{header}: {value}")
