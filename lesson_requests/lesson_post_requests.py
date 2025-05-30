import requests

"""
Отправь POST-запрос на https://httpbin.org/post, передав в теле простой 
JSON (например, {"name": "John"}), и проверь, что он вернулся в ответе.
"""
# Передеаем JSON через параметр json=
payload = {'name': 'Mike'}
response = requests.post('https://httpbin.org/post', json=payload)
# json=payload, правильно сериализует JSON и отправляет в Content-Type

if response.status_code == 200:
    print(f"Статус код: {response.status_code}")

    data = response.json()  # response.json() - возвращает JSON-ответ сервера
    # Проверяем, что отправленный JSON вернулся в ответе
    if data.get('json') == payload:
        print(f"JSON в ответе совпадает: {data.get('json')}")
    else:
        print(f"JSON в ответе не совпадает: {data.get('json')}")
else:
    print(f"Неверный статус код: {response.status_code}")

"""
Отправь POST-запрос с JSON и проверь, что ответ возвращает 200, 
а также что сервер корректно распарсил поля (например, имя и возраст).
"""

"""
Отправь POST-запрос с form-data вместо JSON. Убедись, что поля попали в form-часть ответа и не в json.
"""

"""
Создай requests.Session, сделай POST-запрос с куками и заголовками. Убедись, что состояние сохраняется между запросами.
"""
