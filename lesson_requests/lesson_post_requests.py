import requests

"""
Отправь POST-запрос на https://httpbin.org/post, передав в теле простой 
JSON (например, {"name": "John"}), и проверь, что он вернулся в ответе.
"""
# # Передеаем JSON через параметр json=
# payload = {'name': 'Mike'}
# response = requests.post('https://httpbin.org/post', json=payload)
# # json=payload, правильно сериализует JSON и отправляет в Content-Type
#
# if response.status_code == 200:
#     print(f"Статус код: {response.status_code}")
#
#     data = response.json()  # response.json() - возвращает JSON-ответ сервера
#     # Проверяем, что отправленный JSON вернулся в ответе
#     if data.get('json') == payload:
#         print(f"JSON в ответе совпадает: {data.get('json')}")
#     else:
#         print(f"JSON в ответе не совпадает: {data.get('json')}")
# else:
#     print(f"Неверный статус код: {response.status_code}")

"""
Отправь POST-запрос с JSON и проверь, что ответ возвращает 200, 
а также что сервер корректно распарсил поля (например, имя и возраст).
"""

# # Передаем информацию с JSON телом через параметр json=
# payload = {'name': 'Yoda', 'age': 19}
# response = requests.post('https://httpbin.org/post', json=payload)
# # json=payload, правильно сериализует JSON и отправляет в Content-Type
#
# if response.status_code == 200:
#     print(f"Статус код: {response.status_code}")
#
#     data = response.json()
#     if data.get('json') == payload:
#         print("Правильно распарсил поля")
#     else:
#         print("Неправильно распарсил поля")
#
#     json_body = data.get('json', {})
#     name = json_body.get('name')
#     age = json_body.get('age')
#
#     if name == payload['name'] and age == payload['age']:
#         print("Поля распарсены корректно по ключам")
#     else:
#         print("Ошибка, поля неверно распарсены")
#
# else:
#     print(f"Неверный статус код: {response.status_code}")

"""
Отправь POST-запрос с form-data вместо JSON. Убедись, что поля попали в form-часть ответа и не в json.
"""
# form_data = {
#     'obj': 'values',
#     'obj2': 'values2'
# }
#
# response = requests.post('https://httpbin.org/post', data=form_data)
# data = response.json()
#
# if data['form'].get('obj') == 'values':
#     print("form содержит нужные поля")
# else:
#     print("form не содержит нужное значение")
#
# if data['json'] is None:
#     print("json == None")
# else:
#     print(f"json содержит данные {data['json']}")

"""
Создай requests.Session, сделай POST-запрос с куками и заголовками. Убедись, что состояние сохраняется между запросами.
"""
# # Создаем сессию
# session = requests.Session()
#
# # Устанавливаем заголовки и куки
# session.headers.update({'Authorization': 'Beaver token'})
# session.cookies.update({'session_token': 'token111'})
#
# # Делаем POST-запрос, сессия должна отправить все данные
# response = session.post('https://httpbin.org/post')
#
# # Проверяем, что куки и заголовки сохраняются
# response1 = session.get('https://httpbin.org/headers')
# response2 = session.get('https://httpbin.org/cookies')
#
# # Печатаем для проверки
#
# print("Заголовки:", response1.json())
# print("Куки:", response2.json())

"""
Задача:
Используя requests.Session, отправь POST-запрос на сайт http://httpbin.org/post с пользовательскими данными 
(например, имя и возраст). Затем сделай GET-запрос на http://httpbin.org/cookies, чтобы проверить, что куки, 
установленные при POST-запросе, сохраняются в сессии.

Условия:
Создай сессию (requests.Session).
Отправь POST-запрос, передав в теле запроса данные в form-data (например, name и age).
Убедись, что сессия сохраняет куки (например, смотри на response.cookies).
Сделай GET-запрос на URL http://httpbin.org/cookies и проверь, что куки действительно были переданы.
Выведи на экран куки, полученные в ответе.
"""

# Создаем сессию
session = requests.Session()

# Передаем информацию в теле запроса через form-data
form_data = {'name': 'Jack', 'age': 20}

# Устанавливаем куки
session.cookies.update({'session_token': 'fresh_token'})

# Делаем POST-запрос, сессия должна отправить все данные
response = session.post('http://httpbin.org/post', data=form_data)
data = response.json()

# Проверка полей form
if data['form'].get('name') == 'Jack' and data['form'].get('age') == '20':
    print("form содержит нужные поля")
else:
    print("form не содержит нужное значение")

# Проверка, что JSON не передавался
if data['json'] is None:
    print("json == None")

# GET-запрос для проверки куков
cookies_response = session.get('http://httpbin.org/cookies')
cookies_data = cookies_response.json().get('cookies', {})

# Проверка сохранения куки
if cookies_data.get('session_token') == 'fresh_token':
    print("Кука успешно передана и сохранена")
else:
    print("Кука не передана")

print("Кука сервера:", cookies_data)