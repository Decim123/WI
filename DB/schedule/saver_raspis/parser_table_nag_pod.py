import sqlite3
from openpyxl import load_workbook

conn = sqlite3.connect('raspis.db')
cursor = conn.cursor()