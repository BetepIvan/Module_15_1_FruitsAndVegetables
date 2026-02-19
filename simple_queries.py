import os
from dotenv import load_dotenv
import pyodbc

import SQLQueries

load_dotenv()

DRIVER = os.getenv('MS_SQL_DRIVER')
SERVER = os.getenv('MS_SQL_SERVER')
PAD_DATABASE = os.getenv('MS_SQL_PAD_DATABASE')
DATABASE = os.getenv('MS_SQL_DATABASE')
USER = os.getenv('MS_SQL_USER')
PASSWORD = os.getenv('MS_SQL_KEY')

"""
Строка подключения для SQL Server
"""
connection_string = f"""DRIVER={{SQL Server}};
                        SERVER={SERVER};
                        DATABASE={PAD_DATABASE};
                        UID={USER};
                        PWD={PASSWORD};"""

"""
1. СОЗДАНИЕ НОВОЙ БАЗЫ ДАННЫХ FruitsAndVegetables
"""
print("=" * 50)
print("1. СОЗДАНИЕ БАЗЫ ДАННЫХ")
print("=" * 50)

database_name = 'FruitsAndVegetables'
conn = pyodbc.connect(connection_string)
conn.autocommit = True

try:
    SQL_Query = SQLQueries.create_database_default(database_name)
    conn.execute(SQL_Query)
    print(f'✅ База данных {database_name} успешно создана')
except pyodbc.ProgrammingError as ex:
    print(f'❌ Ошибка при создании БД: {ex}')
finally:
    conn.close()

"""
2. СОЗДАНИЕ НОВОЙ ТАБЛИЦЫ В БД FruitsAndVegetables
"""
print("\n" + "=" * 50)
print("2. СОЗДАНИЕ ТАБЛИЦЫ")
print("=" * 50)

# Обновляем строку подключения для работы с созданной БД
connection_string_with_db = f"""DRIVER={{SQL Server}};
                                SERVER={SERVER};
                                DATABASE={database_name};
                                UID={USER};
                                PWD={PASSWORD};"""

conn = pyodbc.connect(connection_string_with_db)
conn.autocommit = True
cursor = conn.cursor()
table_name = 'FruitsAndVegetables'

try:
    SQL_QUERY = SQLQueries.create_table_fruits_vegetables(table_name)
    cursor.execute(SQL_QUERY)
    print(f'✅ Таблица {table_name} успешно создана')
except pyodbc.ProgrammingError as ex:
    print(f'❌ Ошибка при создании таблицы: {ex}')
finally:
    conn.close()

"""
3. ЗАПОЛНЕНИЕ ТАБЛИЦЫ ДАННЫМИ
"""
print("\n" + "=" * 50)
print("3. ЗАПОЛНЕНИЕ ТАБЛИЦЫ ДАННЫМИ")
print("=" * 50)

conn = pyodbc.connect(connection_string_with_db)
conn.autocommit = True
cursor = conn.cursor()

try:
    SQL_QUERY = SQLQueries.insert_data_fruits_vegetables(table_name)
    cursor.execute(SQL_QUERY)
    print(f'✅ Данные в таблицу {table_name} успешно добавлены')
except pyodbc.ProgrammingError as ex:
    print(f'❌ Ошибка при добавлении данных: {ex}')
except pyodbc.IntegrityError as ex:
    print(f'❌ Ошибка целостности данных: {ex}')
finally:
    conn.close()

"""
4. ВЫВОД ВСЕХ ДАННЫХ ИЗ ТАБЛИЦЫ (в виде списка словарей)
"""
print("\n" + "=" * 50)
print("4. ВЫВОД ДАННЫХ ИЗ ТАБЛИЦЫ")
print("=" * 50)

conn = pyodbc.connect(connection_string_with_db)
cursor = conn.cursor()

try:
    SQL_QUERY = SQLQueries.select_all_from_table(table_name)
    cursor.execute(SQL_QUERY)

    # Получаем названия колонок
    columns = [column[0] for column in cursor.description]

    # Получаем все строки и преобразуем в список словарей
    rows = cursor.fetchall()
    result_list = []

    print("\nДанные из таблицы FruitsAndVegetables:")
    print("-" * 80)

    for row in rows:
        # Создаем словарь для каждой строки
        row_dict = {}
        for i, col in enumerate(columns):
            row_dict[col] = row[i]
        result_list.append(row_dict)

        # Выводим строку в читаемом формате
        print(f"ID: {row.Id}, Название: {row.Name}, Тип: {row.Type}, "
              f"Цвет: {row.Color}, Калорийность: {row.Calories}, "
              f"Описание: {row.Description}")

    print("-" * 80)
    print(f"✅ Всего записей: {len(result_list)}")
    print("\n📋 Результат в виде списка словарей:")
    for item in result_list:
        print(item)

except pyodbc.ProgrammingError as ex:
    print(f'❌ Ошибка при чтении данных: {ex}')
finally:
    conn.close()

print("\n" + "=" * 50)
print("✅ ВСЕ ОПЕРАЦИИ УСПЕШНО ВЫПОЛНЕНЫ")
print("=" * 50)