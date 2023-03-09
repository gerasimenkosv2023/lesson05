from pprint import pprint

import pymysql.cursors


from pymysql import *

# Делаем connect к базе данных

def update(cur):
    title = input("Введите название авто у которой меняем стоимость")
    price = int(input(f"Введите новую стоимость для {title}"))
    sql_update = f"UPDATE goods SET price={price} WHERE title='{title}'"
    cur.execute(sql_update)

def show_data(cur):
    cur.execute('select * from goods')
    rows = cur.fetchall()  # получаем все данные из таблицы в виде списка словарей
    # pprint(rows)
    for item in rows:
        print(f"Автомобиль {item['title']} стоит {item['price']}")

connect = connect(host="localhost",
                  user="root",
                  password="root",
                  db="lesson11",
                  cursorclass=pymysql.cursors.DictCursor #для возможности получать данные в виде словаря
                  )
with connect:
    cur = connect.cursor()#получили объект с помощью которого можно запускать запросы к базе данных
    show_data(cur)
    update(cur)
    connect.commit() #для подтверждения сохранения изменений в базе
    show_data(cur)