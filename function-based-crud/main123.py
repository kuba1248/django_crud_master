database = {
     296: {'name': 'Бекзат', 'password': 'скала', 'info': '...'},
     134: {'name': 'Эртай', 'password': 'пароль', 'info': '...'},
     987: {'name': 'Оомат', 'password': 'Кыргызстан', 'info': '...'},
     273: {'name': 'Имран', 'password': '12345', 'info': '...'},
     596: {'name': 'Жийде', 'password': 'return', 'info': '...'},
     514: {'name': 'Манас', 'password': 'Маке', 'info': '...'},
     912: {'name': 'Арафат', 'password': '54321', 'info': '...'},
     801: {'name': 'Элжаз', 'password': 'парол', 'info': '...'},
     518: {'name': 'Гулсана', 'password': '312', 'info': '...'},
     366: {'name': 'Эркайым', 'password': 'Айдин', 'info': '...'},
     861: {'name': 'Бекназ', 'password': 'Арёль', 'info': '...'},
     599: {'name': 'Эдиль', 'password': 'ьлорап', 'info': '...'},
     567: {'name': 'Айгул', 'password': 'май', 'info': '...'},
     394: {'name': 'Закир', 'password': '@@@', 'info': '...'},
     672: {'name': 'Бегайым', 'password': 'makers', 'info': '...'},
     182: {'name': 'Мырзайым', 'password': 'Bootcamp2221', 'info': '...'},
     770: {'name': 'Даниэл', 'password': 'covid19', 'info': '...'},
     420: {'name': 'Жибек', 'password': '1404', 'info': '...'},
     556: {'name': 'Калысбек', 'password': 'стол', 'info': '...'},
     570: {'name': 'Ырыс', 'password': 'suuuuuuuuiiiiiiiiiiii', 'info': '...'},
     954: {'name': 'Айканыш', 'password': 'qwerty', 'info': '...'},
     149: {'name': 'Арген', 'password': '11172332', 'info': '...'},
     267: {'name': 'Нурмухамед', 'password': 'Не верный', 'info': '...'},
     209: {'name': 'Бектур', 'password': '0101', 'info': '...'},
     731: {'name': 'Алан', 'password': 'душу питона', 'info': '...'},
     718: {'name': 'Куба', 'password': '1', 'info': '...'},
     653: {'name': 'Жаангер', 'password': 'ох блин', 'info': '...'},
     405: {'name': 'Богдан', 'password': 'Кудайберген', 'info': '...'},
     698: {'name': 'Айгерим', 'password': 'синий маркер', 'info': '...'},
     744: {'name': 'Настя', 'password': 'Python21', 'info': '...'},
     689: {'name': 'Жаркынай', 'password': 'Мафия', 'info': '...'}
}

def read12(u_id):
     """
     принимает id usera
     выводит его имя и инфо
     если такого юзера нету вызывает exception
     """
    if u_id not in database:
        raise Exception('такого юзера нету')

    name = database[u_id]["name"]
    info = database[u_id]["info"]

    print(f'''
************************
name: {name} 
info: {info}
************************
''')


def create12():
     from utils import *
     name = input('имя:')
     password = input('пароль:')
     password2 = input('повтор пароль:')
     validate_password(password,password2)

     info = input('инфо:')
     id_ = generate_id(database.keys())

     database[id_] = {
          'name': name,
          'password': password,
          'info': info

     }
print('успешно добавлены')




# read12(5)
#
# read12(134)


# from random import *
#
#
# ids = []
#
# for key, value in database.copy().items():
#     id = random.randint(100, 999)
#     while id in ids:
#         id = random.randint(100, 999)
#     ids.append(id)
#
#     database[id] = {
#         'name': key,
#         'password': value,
#         'info': '...'
#     }
#     del database[key]
#
# print(database)