import sqlite3
from datetime import datetime, timedelta

# функция для определения текущей недели
def current_week():
    current_date = datetime.now()
    week_number = current_date.isocalendar()[1]
    return "NAD" if week_number % 2 == 1 else "POD"

# функция для выполнения запроса к базам данных
def get_schedule(day_of_week, group, weeks_forward=0, weeks_backward=0):
    current_week_type = current_week()

    desir_date = datetime.now() + timedelta(weeks=weeks_forward)
    desir_date -= timedelta(weeks=weeks_backward)

    week_number = desir_date.isocalendar()[1]
    current_week_type = "NAD" if week_number % 2 == 1 else "POD"

    if current_week_type == "NAD":
        database_name = "NAD.db"
    else:
        database_name = "POD.db"

    conn = sqlite3.connect(database_name)
    c = conn.cursor()

    c.execute("SELECT * FROM {} WHERE \"День недели\" = ? AND \"Группа\" = ?".format(day_of_week), (day_of_week, group))

    results = c.fetchall()

    conn.close()

    return results

# то что передается в функцию
day_of_week = "Понедельник"  # День недели также название таблицы
group = "1-МГ-14"
weeks_forward = 0 # сколько недель вперед и если = 0 то будет только текущая короче потыкай поймешь
weeks_backward = 0 #т оже самое но назад

for d in range(-weeks_backward, weeks_forward + 1):
    schedule = get_schedule(day_of_week, group, weeks_forward=d, weeks_backward=weeks_backward)
    if d == 0:
        print("Текущая неделя:")
    elif d > 0:
        print(f"\nЧерез {d} {'неделю' if d == 1 else 'недели'}:")
    else:
        print(f"\n{d * -1} {'неделю' if d * -1 == 1 else 'недели'} назад:")
    print(schedule)
