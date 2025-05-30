import requests

# response = requests.get('https://api.github.com')
# if response.status_code == 200:
#     print("Запрос успешно выполнен")
# else:
#     print(f"Ошибка: {response.status_code}")

"""
Выполни GET-запрос к публичному API (например, https://api.agify.io/?name=michael). 
Проверь, что ответ успешен и что в ответе есть поле age.
"""

# response = requests.get('https://api.agify.io/?name=michael')
#
# if response.status_code == 200:
#     print(f"Код запроса: {response.status_code}")
#     data = response.json()  # Сохраняем JSON-ответ в переменную
#     if 'age' in data:  # Проверка, что в data есть поле 'age'
#         print(f"Возврат: {data['age']}")
#     else:
#         print("Поле 'age' не найдено в ответе")
# else:
#     print(f"Ошибка: {response.status_code}")


"""
Отправь GET-запрос с несколькими query-параметрами (например, country_id, name)
и проверь, что они корректно отражаются в теле ответа.
"""

# params = {'country': 'USA', 'name': 'michael'}
# response = requests.get('https://api.agify.io/', params=params)
#
# if response.status_code == 200:
#     print(f"Код запроса: {response.status_code}")
#     data = response.json()
#
#     # Проверяем, что имя из параметров есть в ответе
#     if data.get('name') == params['name']:
#         print(f"Параметр name в ответе совпадает: {data.get('name')}")
#     else:
#         print(f"Параметр name в ответе НЕ совпадает: {data.get('name')}")
#     # Проверяем, что  API agify.io не поддерживает параметр country и не возвращает его в ответе
#     if data.get('country') == params['country']:
#         print(f"Параметр country в ответе совпадает: {data.get('country')}")
#     else:
#         print(f"Параметр country в ответе НЕ совпадает: {data.get('country')}")
#
# else:
#     print(f"Ошибка: {response.status_code}")

"""
Отправь GET-запрос с кастомными HTTP-заголовками. 
Убедись, что сервер получил эти заголовки (например, через публичный https://httpbin.org/headers).
"""

# headers = {'Authorization': 'JWT Token 123', 'Custom-Header': 'value', 'Name-Site': 'LOL'}
# response = requests.get('https://httpbin.org/headers', headers=headers)
#
# if response.status_code == 200:
#     print(f"Код запроса: {response.status_code}")
#     data = response.json()
#
#     # Проверяем, что кастомные заголовки есть в ответе
#     if data['headers'].get('Authorization') == headers['Authorization']:
#         print(f"Параметр Authorization совпадает: {data['headers'].get('Authorization')}")
#     else:
#         print(f"Не совпадает")
#
#     if data['headers'].get('Custom-Header') == headers['Custom-Header']:
#         print(f"Параметр Custom-Header совпадает: {data['headers'].get('Custom-Header')}")
#     else:
#         print(f"Не совпадает")
#
#     if data['headers'].get('Name-Site') == headers['Name-Site']:
#         print(f"Параметр Name-Site совпадает: {data['headers'].get('Name-Site')}")
#     else:
#         print(f"Не совпадает")

"""
Сделай GET-запрос на URL, который возвращает редирект (например, http://github.com) и обрабатывает таймаут.
Убедись, что ты можешь настроить поведение (следовать/не следовать редиректу, обработать исключение при таймауте).
"""

# site = 'https://github.com/'
#
# try:
#     response = requests.get('http://github.com', allow_redirects=True, timeout=10)
#
#     if response.url == site:
#         print("url совпадает")
#     else:
#         print(f"url не совпадает: {response.url}")
#
# except requests.exceptions.Timeout:
#     print("Истекло время ожидания запроса")
#
# except requests.exceptions.RequestException as error:
#     print(f"Произошла ошибка запроса {error}")







