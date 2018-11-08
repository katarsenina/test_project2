# Тестовое приложение с REST API  http://pulse-rest-testing.herokuapp.com/
# Создаём один скрипт:
#     • Создаёт персонажа POST /roles/, вы запоминаете его id.
#     • Проверяете, что он создался и доступен по ссылке GET /roles/[id]
#     • Проверяете, что он есть в списке пользователей по GET /roles/
#     • Изменяете этого пользователя методом PUT roles/[id]/
#     • Проверяете, что он изменился и доступен по ссылке /roles/[id]
#     • Проверяете, что он есть в списке пользователей по GET /roles/ с новой инфой
#     • Удаляете этого пользователя методом DELETE roles/[id]
# Второй скрипт: тоже самое с книгами
# ** Попробуйте воспользоваться http.client вместо requests.


import requests

url = "http://pulse-rest-testing.herokuapp.com/"
roles = "roles/"
books = "books/"
edit_data = {"title": "LAMA"}

"""Скрипт для книги - создание, изменение, удаление"""

resp = requests.post(url + books,  data={"title": "FOX", "author": "Nik Brasil"})
b_dict = resp.json()

resp_id = requests.get(url+books+str(b_dict["id"]))
if resp_id.ok is False:
    print("There is no such book")

resp_list = requests.get(url+books)
books_str = resp_list.text
id_book = str(b_dict["id"])

if books_str.find(id_book) < 0:
    print("There is no such book")

resp_edit = requests.put(url + books + str(b_dict["id"]), edit_data)

if books_str.find(edit_data["title"]) > 0:
    print("There is no such book")

r = requests.delete(url+books+str(b_dict["id"])+"/")



"""Скрипт для роли - создание, изменение, удаление"""

role_data = {"name": "Lindge", "type": "ork","level": 32}
edit_role = {"name": "Bella", "type": "bird"}

resp = requests.post(url + roles, role_data)
r_dict = resp.json()
resp_id = requests.get(url + roles + str(r_dict["id"]))

if resp_id.ok is False:
    print("There is no such role")

resp_roles = requests.get(url + roles)
roles_str = resp_roles.text
id_role = str(r_dict["id"])

if roles_str.find(id_role) < 0:
    print("There is no such role")

resp_edit = requests.put(url + roles + str(r_dict["id"]), edit_role)

if roles_str.find(edit_role["name"]) < 0:
    print("There is no such role")

r = requests.delete(url + roles + str(r_dict["id"])+"/")


