# реализация сервера для тестирования метода get по заданию - Клиент для отправки метрик
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.bind(('127.0.0.1', 8888))
sock.listen(1)
conn, addr = sock.accept()

print('Соединение установлено:', addr)

# переменная response хранит строку возвращаемую сервером, если вам для
# тестирования клиента необходим другой ответ, измените ее
metric_dict = {'palm.cpu': [], 'palm.usage': [],
               'palm.disk_usage': [], 'palm.network_usage': [],
               'eardrum.cpu': [], 'eardrum.usage': [],
               'eardrum.disk_usage': [], 'eardrum.network_usage': []}
response = b'ok\npalm.cpu 10.5 2\neardrum.cpu 15.3 1\n\n'

while True:
    data = conn.recv(1024)
    if not data:
        break
    request = data.decode('utf-8')
    print(f'Получен запрос: {ascii(request)}')
    print(f'Отправлен ответ {ascii(response.decode("utf-8"))}')
    conn.send(response)

conn.close()
