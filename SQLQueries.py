def create_database_default(name):
    COMMAND = fr"CREATE DATABASE {name};"
    return COMMAND

def create_table_fruits_vegetables(name):
    COMMAND = fr"""CREATE TABLE {name}
                (Id int IDENTITY(1,1) PRIMARY KEY,
                Name nvarchar(50) UNIQUE,
                Type nvarchar(10),
                Color nvarchar(20),
                Calories int,
                Description nvarchar(100));"""
    return COMMAND

def insert_data_fruits_vegetables(name):
    COMMAND = fr"""INSERT INTO {name} (Name, Type, Color, Calories, Description)
                VALUES
                ('Яблоко', 'фрукт', 'красный', 52, 'Сладкий и сочный фрукт'),
                ('Банан', 'фрукт', 'желтый', 89, 'Энергетический фрукт'),
                ('Морковь', 'овощ', 'оранжевый', 41, 'Хрустящий овощ'),
                ('Брокколи', 'овощ', 'зеленый', 34, 'Питательный овощ'),
                ('Апельсин', 'фрукт', 'оранжевый', 47, 'Цитрусовый фрукт'),
                ('Помидор', 'овощ', 'красный', 18, 'Сочный овощ'),
                ('Виноград', 'фрукт', 'фиолетовый', 69, 'Сладкие ягоды'),
                ('Огурец', 'овощ', 'зеленый', 15, 'Освежающий овощ'),
                ('Клубника', 'фрукт', 'красный', 32, 'Сладкая ягода'),
                ('Картофель', 'овощ', 'коричневый', 77, 'Крахмалистый овощ');"""
    return COMMAND

def insert_single_record(table, columns, data):
    COMMAND = fr'''INSERT INTO {table} {columns}
                VALUES
                {data}'''
    return COMMAND

def select_all_from_table(table):
    COMMAND = fr"SELECT * FROM {table};"
    return COMMAND