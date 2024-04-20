import sqlite3
import openpyxl

# Создание базы данных NAD
conn_nad = sqlite3.connect('NAD.db')
cur_nad = conn_nad.cursor()

# Создание базы данных POD
conn_pod = sqlite3.connect('POD.db')
cur_pod = conn_pod.cursor()

# Создание таблиц для каждого дня недели в базе NAD
for day in ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]:
    group_table_name = f"{day}"
    print(f"Creating table: {group_table_name}")
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {group_table_name} (
        "Закреплённая кафедра" TEXT,
        "Группа" TEXT,
        "Дисциплина, вид учебной работы" TEXT,
        "Вид занятий" TEXT,
        "Часы" INTEGER,
        "Преподаватель" TEXT,
        "День недели" TEXT,
        "Счет недель" TEXT,
        "Время" TEXT,
        "Корпус" TEXT,
        "Аудитория" TEXT
    );
    """
    cur_nad.execute(create_table_query)

# Создание таблиц для каждого дня недели в базе POD
for day in ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]:
    group_table_name = f"{day}"
    print(f"Creating table: {group_table_name}")
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {group_table_name} (
        "Закреплённая кафедра" TEXT,
        "Группа" TEXT,
        "Дисциплина, вид учебной работы" TEXT,
        "Вид занятий" TEXT,
        "Часы" INTEGER,
        "Преподаватель" TEXT,
        "День недели" TEXT,
        "Счет недель" TEXT,
        "Время" TEXT,
        "Корпус" TEXT,
        "Аудитория" TEXT
    );
    """
    cur_pod.execute(create_table_query)

# Открываем файл иксельку
wb = openpyxl.load_workbook(r'DB\schedule\saver_raspis\v2\raspisanie_o_itm_22.xlsx')
sheet = wb.active

# Проходим по каждой строке в иксельке
for row in sheet.iter_rows(min_row=2, values_only=True):
    # забираем данные строчки
    Закрепленная_кафедра, Группа, Дисциплина_вид_учебной_работы, Вид_занятий, Часы, Преподаватель, День_недели, Счет_недель, Время, Корпус, Аудитория = row

    # Определяем в какую бд писать
    if Счет_недель == 'знам' or Счет_недель.isdigit():
        cur_pod.execute(f"INSERT INTO {День_недели} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (Закрепленная_кафедра, Группа, Дисциплина_вид_учебной_работы, Вид_занятий, Часы, Преподаватель, День_недели, Счет_недель, Время, Корпус, Аудитория))
    if '/' in Счет_недель:
        cur_nad.execute(f"INSERT INTO {День_недели} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (Закрепленная_кафедра, Группа, Дисциплина_вид_учебной_работы, Вид_занятий, Часы, Преподаватель, День_недели, Счет_недель, Время, Корпус, Аудитория))
        cur_pod.execute(f"INSERT INTO {День_недели} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (Закрепленная_кафедра, Группа, Дисциплина_вид_учебной_работы, Вид_занятий, Часы, Преподаватель, День_недели, Счет_недель, Время, Корпус, Аудитория))
    if Счет_недель == 'числ' or Счет_недель.isdigit():
        cur_nad.execute(f"INSERT INTO {День_недели} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (Закрепленная_кафедра, Группа, Дисциплина_вид_учебной_работы, Вид_занятий, Часы, Преподаватель, День_недели, Счет_недель, Время, Корпус, Аудитория))


# Сохраняем изменения в бд
conn_nad.commit()
conn_pod.commit()
conn_nad.close()
conn_pod.close()
